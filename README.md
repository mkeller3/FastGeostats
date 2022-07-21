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
| `POST`  | `/api/v1/tables/categorical_breaks`                                             | [Categorical Breaks](#categorical-breaks)               |
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

Example: 

### Example Input
```json
```

### Example Output
```json
```

## Numeric Breaks

### Description

Example: 

### Example Input
```json
```

### Example Output
```json
```

## Categorical Breaks

### Description

Example: 

### Example Input
```json
```

### Example Output
```json
```

## Custom Break Values

### Description

Example: 

### Example Input
```json
```

### Example Output
```json
```