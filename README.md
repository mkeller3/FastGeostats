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

Example: 

### Example Input
```json
```

### Example Output
```json
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