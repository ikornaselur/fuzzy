import typer

from fuzzy.exceptions import catch_exceptions
from fuzzy.strategy import generate_strategy_files

app = typer.Typer(name="Fuzzy", help="An API fuzzing tool")


@app.command()
@catch_exceptions
def generate(url: str) -> None:
    """Generate base strategy files"""
    generate_strategy_files(url)


@app.command()
def foo() -> None:
    pass
