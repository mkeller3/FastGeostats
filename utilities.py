"""FastGeostats App - Utilities"""
from pygeofilter.backends.sql import to_sql_where
from pygeofilter.parsers.ecql import parse

async def generate_where_clause(info: object, con, no_where: bool=False) -> str:
    """
    Method to generate where clause

    """
    
    query = ""

    if info.filter:
        sql_field_query = f"""
            SELECT column_name
            FROM information_schema.columns
            WHERE table_name = '{info.table}'
            AND column_name != 'geom';
        """

        db_fields = await con.fetch(sql_field_query)

        field_mapping = {}  

        for field in db_fields:
            field_mapping[field['column_name']] = field['column_name']

        ast = parse(info.filter)
        filter = to_sql_where(ast, field_mapping)

        if no_where is False:
            query += f" WHERE "
        else:
            query += f" AND "
        query += f" {filter}"
    
    if info.coordinates and info.geometry_type and info.spatial_relationship:
        if info.filter:
            query += " AND "
        else:
            if no_where is False:
                query += " WHERE "
        if info.geometry_type == 'POLYGON':
            query += f"{info.spatial_relationship}(ST_GeomFromText('{info.geometry_type}(({info.coordinates}))',4326) ,{info.table}.geom)"
        else:
            query += f"{info.spatial_relationship}(ST_GeomFromText('{info.geometry_type}({info.coordinates})',4326) ,{info.table}.geom)"

    return query