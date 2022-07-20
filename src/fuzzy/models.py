from typing import Optional
from pydantic import BaseModel, Field


class Parameter(BaseModel):
    name: str
    description: str
    in_: str = Field(..., alias="in")
    required: bool
    type: str
    items: Optional[dict[str, str]]

    class Config:
        fields = {
            "in_": "in",
        }


class Response(BaseModel):
    description: str


class Method(BaseModel):
    description: str
    parameters: list[Parameter]
    responses: dict[str, Response]


class Path(BaseModel):
    get: Optional[Method]


class Schema(BaseModel):
    swagger: str
    host: Optional[str]
    schemes: list[str]
    paths: dict[str, Path]
