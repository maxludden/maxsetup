from __future__ import annotations

from inspect import currentframe, getframeinfo
from pathlib import Path
from typing import Optional
from shutil import rmtree, copytree, ignore_patterns


from loguru import logger as log
from rich.color import Color
from rich.console import Console, JustifyMethod, RenderableType
from rich.align import AlignMethod
from rich.panel import Panel
from rich.repr import rich_repr
from rich.box import Box, ROUNDED
from rich.style import Style, StyleType
from rich.table import Column
from rich.text import Text, TextType
from rich.traceback import install as install_rich_traceback
from sh import Command

from maxconsole import get_theme, get_console
from maxprogress import get_progress
from maxcolor import gradient, gradient_panel
import max_yaml as yaml

console = get_console(get_theme())

CWD = Path.cwd()
template = Path("/Users/maxludden/dev/template")

# ───────────── Set Up File Structure ─────────────────────────
@log.catch
def _copy_files() -> None:
    """Copy files from the template folder to the current working directory."""
    if (CWD / "logs" / "run.txt").exists():
        rmtree(CWD)
    copytree(
        template, CWD, ignore=ignore_patterns("*.pyc", "venv", "__pycache__", ".py")
    )
    console.print("")
    console.print(
        gradient_panel(
            "Copied files from the template directory", title="Copied Files"
        ),
        justify="center",
    )


# ─────────────────── Run ─────────────────────────────────
@log.catch
def _get_last_run() -> int:
    """Get the last run number from the run.txt file."""
    with open("logs/run.txt", "r") as infile:
        last_run = int(infile.read())
        # console.log(f"Last Run: {last_run}")
        return last_run


@log.catch
def _update_run(last_run: int, write: bool = True) -> int:
    """Update the run.txt file with the next run number."""
    run = last_run + 1
    if write:
        with open(Path("logs/run.txt"), "w") as outfile:
            outfile.write(str(run))
    return run


@log.catch
def new_run(console: Console = console) -> int:
    """Get the next run number."""
    if console is None:
        console = get_console(get_theme())

    # Determine the next run
    last_run = _get_last_run()
    run = _update_run(last_run)
    current_run = gradient(f"Run {run}")

    # Update the console
    console.clear()
    console.rule(current_run, style="bold bright_white")

    return run


# ──────────────────── Log Sinks  ───────────────────────────────
BASE = Path.cwd()
VERBOSE_LOG = BASE / "logs" / "verbose.log"
LOG = BASE / "logs" / "log.log"


@log.catch
def log_init(
    console: Optional[Console],
    current_run: int) -> Logger:  # type: ignore
    """
    Configure Loguru Logger Sinks for the module.

    Args:
        `existing_console` (Optional[Console]): An existing console object to use for logging. If None, a new console will be created.add()

    Returns:
        `log` (Logger): A configured Loguru Logger object.
    """
    if console is None:
        console = get_console(get_theme())
    else:
        console = console

    sinks = log.configure(
        handlers=[
            # Debug - Loguru Logger
            dict(  # . debug.log
                sink=f"{VERBOSE_LOG}",
                level="DEBUG",
                format="Run {extra[run]} | {time:hh:mm:ss:SSS A} | {file.name: ^13} |  Line {line: ^5} | {level: <8}ﰲ  {message}",
                rotation="10 MB",
            ),
            # INFO # Loguru Logger
            dict(
                sink=f"{LOG}",
                level="INFO",
                format="Run {extra[run]} | {time:hh:mm:ss:SSS A} | {file.name: ^13} |  Line {line: ^5} | {level: <8}ﰲ  {message}",
                rotation="10 MB",
            ),
            # INFO - Rich Console Log
            dict(
                sink=(
                    lambda msg: console.log(
                        msg, markup=True, highlight=True, log_locals=False
                    )
                ),
                level="INFO",
                format="Run {extra[run]} | {time:hh:mm:ss:SSS A} | {file.name: ^13} |  Line {line: ^5} | {level: ^8} ﰲ  {message}",
                diagnose=True,
                catch=True,
                backtrace=True,
            ),
            # ERROR - Rich Console Log
            dict(
                sink=(
                    lambda msg: console.log(
                        msg, markup=True, highlight=True, log_locals=True
                    )
                ),
                level="ERROR",
                format="Run {extra[run]} | {time:hh:mm:ss:SSS A} | {file.name: ^13} |  Line {line: ^5} | {level: ^8} ﰲ  {message}",
                diagnose=True,
                catch=True,
                backtrace=True,
            ),
        ],
        extra={"run": current_run},  # > Current Run
    )
    log.debug("Initialized Logger")

    return log


def setup() -> dict:
    """Sets up the project by copying files from the template directory (if necessary) setting up Loguru and Rich Logging Sinks, starts a new run and prints it to the console."""
    CWD = Path.cwd()
    run_txt = CWD / "logs" / "run.txt"
    if not run_txt.exists():
        _copy_files()
    console = get_console(get_theme())
    progress = get_progress(console)
    last_run = _get_last_run()
    run = _update_run(last_run)
    log_init(console=console, current_run=run)
    gradient_run = gradient(f"Run {run}")
    console.clear()
    console.rule(gradient_run, style="bold bright_white")

    return log
