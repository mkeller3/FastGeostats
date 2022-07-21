from pydantic import BaseModel, Field
from typing import Literal, List, Any, Optional

class AggregateModel(BaseModel):
    type: Literal['distinct', 'avg', 'count', 'sum', 'max', 'min']=None
    column: str
    group_column: Optional[str]
    group_method: Optional[str]


class StatisticsModel(BaseModel):
    table: str = Field(
        title="Name of the table to perform analysis on."
    )
    database: str = Field(
        title="Name of the database the table belongs to."
    )
    coordinates: str = Field(
        default=None, title="A list of coordinates to perfrom statistics in a certain geographical area."
    )
    geometry_type: Literal['POINT', 'LINESTRING', 'POLYGON']=None
    spatial_relationship: Literal['ST_Intersects', 'ST_Crosses', 'ST_Within', 'ST_Contains', 'ST_Overlaps', 'ST_Disjoint', 'ST_Touches']=None
    aggregate_columns: List[AggregateModel]
    filter: str=None