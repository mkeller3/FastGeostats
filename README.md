# FastGeostats

FastGeostats is a geospatial api to perform math and statistics on tables from a mulititude of PostgreSQL databases. FastGeostats is written in [Python](https://www.python.org/) using the [FastAPI](https://fastapi.tiangolo.com/) web framework. 

---

**Source Code**: <a href="https://github.com/mkeller3/FastGeostats" target="_blank">https://github.com/mkeller3/FastGeostats</a>

---

## Requirements

FastGeostats requires PostGIS >= 2.4.0.

## Configuration

In order for the api to work you will need to edit the `config.py` file with your database connections.

Example
```python
DATABASES = {
    "data": {
        "host": "localhost", # Hostname of the server
        "database": "data", # Name of the database
        "username": "postgres", # Name of the user, ideally only SELECT rights
        "password": "postgres", # Password of the user
        "port": 5432, # Port number for PostgreSQL
    }
}
```

## Usage

### Running Locally

To run the app locally `uvicorn main:app --reload`

### Production
Build Dockerfile into a docker image to deploy to the cloud.

## API

| Method | URL                                                                              | Description                                             |
| ------ | -------------------------------------------------------------------------------- | ------------------------------------------------------- |
| `POST`  | `/api/v1/tables/statistics`                                                     | [Statistics](#statistics)               |
| `POST`  | `/api/v1/tables/bins`                                                           | [Bins](#bins)               |
| `POST`  | `/api/v1/tables/numeric_breaks`                                                 | [Numeric Breaks](#numeric-breaks)               |
| `POST`  | `/api/v1/tables/custom_break_values`                                            | [Custom Break Values](#custom-break-alues)               |
| `GET`  | `/api/v1/health_check`                                                           | Server health check: returns `200 OK`   |

## Endpoint Description's

## Statistics

### Description
The statistics endpoints allows you to performa multitude of common math statistics on your table such as `'distinct', 'avg', 'count', 'sum', 'max', 'min'`.

Example: In the example below we will be searching for the number of parcels, average deed ac, and distinct first names filtered by last name of `DOOLEY`.

### Example Input 
```json
{
    "database": "data",
    "table": "mclean_county_parcels",
    "aggregate_columns": [
        {
            "type": "count",
            "column": "gid"
        },
        {
            "type": "avg",
            "column": "deed_ac"
        },
        {
            "type": "distinct",
            "column": "first_name",
            "group_column": "first_name",
            "group_method": "count"
        }
    ],
    "filter": "last_name LIKE '%DOOLEY%'"
}
```

### Example Output
```json
{
    "results": {
        "count_gid": 19,
        "avg_deed_ac": 64.28666666666666,
        "distinct_first_name_count_first_name": [
            {
                "first_name": "",
                "count": 3
            },
            {
                "first_name": "COLE",
                "count": 3
            },
            {
                "first_name": "% BAS",
                "count": 2
            },
            {
                "first_name": "%FIRST MID AG SERVICES ",
                "count": 2
            },
            {
                "first_name": "COLE & WENDY",
                "count": 1
            },
            {
                "first_name": "EDITH",
                "count": 1
            },
            {
                "first_name": "JAMES R & TERESA",
                "count": 1
            },
            {
                "first_name": "KENNETH",
                "count": 1
            },
            {
                "first_name": "KEVIN",
                "count": 1
            },
            {
                "first_name": "LUCAS",
                "count": 1
            },
            {
                "first_name": "MCCALLA O & DEANA J",
                "count": 1
            },
            {
                "first_name": "THOMAS",
                "count": 1
            },
            {
                "first_name": "WENDY",
                "count": 1
            }
        ]
    },
    "status": "SUCCESS"
}
```

## Bins

### Description

The bins endpoints allows you to help visualize the spread of a data for a numerical column.

Example: Calculate 10 bins for the `deed_ac` column on the `mclean_county_parcels` table.

### Example Input
```json
{
    "database": "data",
    "table": "mclean_county_parcels",
    "column": "deed_ac",
    "bins": 10
}
```

### Example Output
```json
{
    "results": [
        {
            "min": 0.0,
            "max": 145.158,
            "count": 15993
        },
        {
            "min": 145.158,
            "max": 290.316,
            "count": 1088
        },
        {
            "min": 290.316,
            "max": 435.47399999999993,
            "count": 116
        },
        {
            "min": 435.47399999999993,
            "max": 580.632,
            "count": 19
        },
        {
            "min": 580.632,
            "max": 725.79,
            "count": 11
        },
        {
            "min": 725.79,
            "max": 870.9479999999999,
            "count": 1
        },
        {
            "min": 870.9479999999999,
            "max": 1016.1059999999999,
            "count": 0
        },
        {
            "min": 1016.1059999999999,
            "max": 1161.264,
            "count": 0
        },
        {
            "min": 1161.264,
            "max": 1306.4219999999998,
            "count": 0
        },
        {
            "min": 1306.4219999999998,
            "max": 1451.58,
            "count": 1
        }
    ],
    "status": "SUCCESS"
}
```

## Numeric Breaks

### Description
Create bins of data based off of different mathmatical break types.

Break Types: `equal_interval, head_tail, quantile, jenk`

Example: Create 3 breaks based off of the column `population` for the table `zip_centroids` using a quantile break type.

### Example Input
```json
{
    "database": "data",
    "table": "zip_centroids",
    "column": "population",
    "number_of_breaks": 3,
    "break_type": "quantile"
}
```

### Example Output
```json
{
    "results": [
        {
            "min": 0,
            "max": 1470,
            "count": 10301
        },
        {
            "min": 1470,
            "max": 8932,
            "count": 10373
        },
        {
            "min": 8932,
            "max": 133324,
            "count": 10377
        }
    ],
    "status": "SUCCESS"
}
```

## Custom Break Values

### Description
Create bins based off of your own min and max ranges and provide a count back for each bin.

Example: Create 3 custom bins `0 - 1,000`, `1,000 - 9,000`, and `9,000 - 140,000` based 
off of the column `population` for the table `zip_centroids` using a quantile break type.

### Example Input
```json
{
    "database": "data",
    "table": "zip_centroids",
    "column": "population",
    "breaks": [
        {
            "min": 0,
            "max": 1000
        },
        {
            "min": 1000,
            "max": 9000
        },
        {
            "min": 9000,
            "max": 140000
        }
    ]
}
```

### Example Output
```json
{
    "results": [
        {
            "min": 0.0,
            "max": 1000.0,
            "count": 7981
        },
        {
            "min": 1000.0,
            "max": 9000.0,
            "count": 12720
        },
        {
            "min": 9000.0,
            "max": 140000.0,
            "count": 10350
        }
    ],
    "status": "SUCCESS"
}
```