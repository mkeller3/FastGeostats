from fastapi import APIRouter, Request
from pygeofilter.backends.sql import to_sql_where
from pygeofilter.parsers.ecql import parse


import models
import utilities

router = APIRouter()

@router.post("/statistics/", tags=["Tables"])
async def statistics(info: models.StatisticsModel, request: Request):

    pool = request.app.state.databases[f'{info.database}_pool']

    async with pool.acquire() as con:

        final_results= {}
        cols = []
        col_names = []
        distinct = False
        general_stats = False

        for aggregrate in info.aggregate_columns:
            if aggregrate.type == 'distinct':
                distinct = True
            else:
                general_stats = True
                cols.append(f"""{aggregrate.type }("{aggregrate.column}") as {aggregrate.type}_{aggregrate.column}""")
                col_names.append(f"{aggregrate.type}_{aggregrate.column}")

        if general_stats:
            formatted_columns = ','.join(cols)
            query = f"""
                SELECT {formatted_columns}
                FROM "{info.table}"
            """
            
            query += await utilities.generate_where_clause(info, con)

            data = await con.fetchrow(query)

            for col in col_names:
                final_results[col] = data[col]

        if distinct:
            for aggregrate in info.aggregate_columns:
                if aggregrate.type == 'distinct':
                    query = f"""SELECT DISTINCT("{aggregrate.column}"), {aggregrate.group_method}("{aggregrate.group_column}") FROM "{info.table}" """

                    query += await utilities.generate_where_clause(info, con)

                    query += f""" GROUP BY "{aggregrate.column}" ORDER BY "{aggregrate.group_method}" DESC"""

                    data = await con.fetch(query)

                    final_results[f"distinct_{aggregrate.column}_{aggregrate.group_method}_{aggregrate.group_column}"] = data

        return {
            "results": final_results,
            "status": "SUCCESS"
        }

@router.post("/bins/", tags=["Tables"])
async def bins(info: models.BinsModel, request: Request):

    pool = request.app.state.databases[f'{info.database}_pool']

    async with pool.acquire() as con:
        results = [

        ]
        query = f"""
            SELECT MIN("{info.column}"),MAX("{info.column}")
            FROM "{info.table}"
        """

        query += await utilities.generate_where_clause(info, con)

        data = await con.fetchrow(query)

        group_size = (data['max'] - data['min']) / info.number_of_bins

        for group in range(info.number_of_bins):
            if group == 0:
                min = data['min']
                max = group_size
            else:
                min = group*group_size
                max = (group+1)*group_size
            query = f"""
                SELECT COUNT(*)
                FROM "{info.table}"
                WHERE "{info.column}" > {min}
                AND "{info.column}" <= {max}
            """

            query += await utilities.generate_where_clause(info, con, True)

            data = await con.fetchrow(query)

            results.append({
                "min": min,
                "max": max,
                "count": data['count']
            })

        return {
            "results": results,
            "status": "SUCCESS"
        }