import asyncio
from json.decoder import JSONDecodeError
import aiohttp

from rich import print
import json

from fuzzy.exceptions import InvalidJson, ValidationError
from fuzzy.models import Schema

from pydantic import ValidationError as PydanticValidationError


async def get_schema(url: str) -> dict:
    async with aiohttp.ClientSession() as s:
        async with s.get(url) as r:
            text = await r.text()

    try:
        return json.loads(text)
    except JSONDecodeError:
        raise InvalidJson(f"Unable to decode json from {url}. Is the url valid?")


def generate_strategy_files(url: str) -> None:
    payload = asyncio.run(get_schema(url))

    try:
        schema = Schema(**payload)
    except PydanticValidationError as e:
        raise ValidationError(f"Failed to validate schema:\n{e}") from e

    print(schema)
