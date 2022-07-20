from functools import wraps
import sys
from typing import Callable, ParamSpec, TypeVar

from rich import print
import typer

R = TypeVar("R")
P = ParamSpec("P")


def catch_exceptions(func: Callable[P, R]) -> Callable[P, R]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        try:
            return func(*args, **kwargs)
        except FuzzyException as e:
            print(f"[red]{e}", file=sys.stderr)
            raise typer.Exit(code=1)

    return wrapper


class FuzzyException(Exception):
    pass


class InvalidJson(FuzzyException):
    pass


class ValidationError(FuzzyException):
    pass
