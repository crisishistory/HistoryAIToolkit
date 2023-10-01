from pathlib import Path

from rich import print
import typer
from typing import Optional
from typing_extensions import Annotated

from .slicer import audio_slicing
from .transcript import transcribe_from_paths

app = typer.Typer()


@app.command()
def slice(
    source: Annotated[
        Path,
        typer.Argument(
            exists=True,
            file_okay=True,
            dir_okay=False,
            readable=True,
            resolve_path=True,
            help="Source audio file",
        ),
    ],
    start: Annotated[str, typer.Argument(help="start time in mins:secs")],
    duration: Annotated[str, typer.Argument(help="duration in mins:secs")],
):
    audio_slicing(source, start, duration)


@app.command()
def transcribe(
    source: Annotated[
        Path,
        typer.Argument(
            exists=True,
            file_okay=True,
            dir_okay=False,
            readable=True,
            resolve_path=True,
            help="Source audio file",
        ),
    ],
    target: Path,
):
    if source.suffix not in [".mp3", ".wav"]:
        raise ValueError("File must be an .mp3 or .wav file")
    transcribe_from_paths(source, target)


if __name__ == "__main__":
    app()
