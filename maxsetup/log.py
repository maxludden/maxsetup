from __future__ import annotations
import re

from inspect import currentframe, getframeinfo
from pathlib import Path
from typing import Optional
import random

import ujson as json
from loguru import logger as log
from loguru._logger import Logger as _Logger
from loguru._logger import Core as _Core
from loguru import _defaults
from rich.text import Text, TextType
from rich.console import Console, JustifyMethod, RenderableType
from rich.align import AlignMethod
from rich.padding import PaddingDimensions
from rich.style import StyleType
from rich.box import ROUNDED, Box
from rich.color import Color
from rich.panel import Panel

# from loguru import Logger
from maxsetup.console import console, validate_console, MaxConsole
from maxsetup.setup_files import make_files
from sh import Command

"""This script is used to provide a simple interface to the loguru library based on the standard `logging` library."""


class DirectoryNotFound(FileNotFoundError):
    pass


class RunDictionaryError(OSError):
    pass


# Logging Folder and Filepaths important to logging
BASE = Path.cwd()
run_file = BASE / "logs" / "run.txt"
if not run_file.exists():
    make_files()

# . ─────────────────── Gradient Text ─────────────────────────────────
@log.catch
def gradient(
    message: str | Text,
    num_of_gradients: int = 3,
    justify: Optional[JustifyMethod] = "left",
) -> Text:
    """Generate a gradient text.

    Args:
        message (str): The message to be gradiented.
        num_of_gradients (int, optional): The number of gradients to use. Defaults to 3.

    Returns:
        Text: The gradiented text.
    """
    all_colors = [
        "#ff00ff",
        "#af00ff",
        "#5f00ff",
        "#0000ff",
        "#249df1",
        "#00ffff",
        "#00ff00",
        "#ffff00",
        "#ff8800",
        "#ff0000",
    ]
    if num_of_gradients > len(all_colors):
        raise ValueError(
            f"Number of gradients must be less than or equal to {len(all_colors)}."
        )
    # Set Justification Method for Tet
    text = Text(message, justify=justify)  # type: ignore
    # Get the length of the message
    size = len(message)

    # , Select starting color
    color = random.choice(all_colors)
    chosen_index = all_colors.index(color)  # Get index of chosen color
    color_indexes = [chosen_index]  # Add chosen index to list of indexes
    # console.log(f"Chosen Index: {chosen_index}")  # Log chosen index

    # , Get the indexes of the other colors
    for i in range(1, num_of_gradients + 1):
        next_index = chosen_index + i
        if next_index > len(all_colors):
            next_index = next_index - len(all_colors)
        color_indexes.append(next_index)  # type: ignore
    # console.log(f"Color Indexes: {color_indexes}")

    # , Get the colors for the gradient
    color_range = []  # type: ignore
    for x, i in enumerate(color_indexes):
        next_color = all_colors[i - 1]
        color_range.append(next_color)

    # Determine the size of the gradient
    gradient_size = size // (num_of_gradients - 1)
    gradient_text = Text()

    # , Determine the substring for each gradient
    for index in range(0, num_of_gradients):
        begin = index * gradient_size
        end = begin + gradient_size
        sub_string = text[begin:end]

        if index < num_of_gradients:
            color1 = Color.parse(color_range[index])
            color1_triplet = color1.triplet
            r1 = color1_triplet[0]  # type: ignore
            g1 = color1_triplet[1]  # type: ignore
            b1 = color1_triplet[2]  # type: ignore
            color2 = Color.parse(color_range[index + 1])
            color2_triplet = color2.triplet
            r2 = color2_triplet[0]  # type: ignore
            g2 = color2_triplet[1]  # type: ignore
            b2 = color2_triplet[2]  # type: ignore
            dr = r2 - r1
            dg = g2 - g1
            db = b2 - b1

        # Apply the gradient to each character
        for index in range(gradient_size):
            blend = index / gradient_size
            color = f"#{int(r1 + dr * blend):02X}{int(g1 + dg * blend):02X}{int(b1 + db * blend):02X}"  # type: ignore
            sub_string.stylize(color, index, index + 1)

        gradient_text = Text.assemble(gradient_text, sub_string, justify=justify)

    return gradient_text


def rainbow(message: str, justify: JustifyMethod = "left") -> Text:
    """Generate a rainbow text.

    Args:
        message (str): The message to be rainbowed.
        justify (JustifyMethod, optional): The justification method. Defaults to "left".

    Returns:
        Text: The rainbowed text.
    """
    return gradient(message, num_of_gradients=10, justify=justify)


def gradient_panel(
    message: RenderableType,
    box: Box = ROUNDED,
    title: Optional[TextType] = None,
    title_align: AlignMethod = "center",
    gradient_title: bool = True,
    subtitle: Optional[TextType] = None,
    subtitle_align: AlignMethod = "right",
    expand: bool = True,
    border_style: StyleType = "bold #ffffff",
    width: Optional[int] = None,
    height: Optional[int] = None,
    padding: PaddingDimensions = (0, 1),
    num_of_gradients: int = 3,
    justify_text: JustifyMethod = "left",
) -> Panel:
    """
    Generate a gradient panel.

    Args:
        message (RenderableType): The message to be gradiented.
        box (Box, optional): The box style. Defaults to ROUNDED.
        title (Optional[TextType], optional): The title of the panel. Defaults to None.
        title_align (AlignMethod, optional): The alignment of the title. Defaults to "center".
        subtitle (Optional[TextType], optional): The subtitle of the panel. Defaults to None.
        subtitle_align (AlignMethod, optional): The alignment of the subtitle. Defaults to "right".
        expand (bool, optional): Whether to expand the panel. Defaults to True.
        border_style (StyleType, optional): The border style. Defaults to "bold #ffffff".
        width (Optional[int], optional): The width of the panel. Defaults to None.
        height (Optional[int], optional): The height of the panel. Defaults to None.
        padding (PaddingDimensions, optional): The padding of the panel. Defaults to (0, 1).
        num_of_gradients (int, optional): The number of gradients to use. Defaults to 3.
        justify_text (JustifyMethod, optional): The justification method. Defaults to "left".
    """
    all_colors = [
        "#ff00ff",
        "#af00ff",
        "#5f00ff",
        "#0000ff",
        "#249df1",
        "#00ffff",
        "#00ff00",
        "#ffff00",
        "#ff8800",
        "#ff0000",
    ]
    if num_of_gradients > len(all_colors):
        raise ValueError(
            f"Number of gradients must be less than or equal to {len(all_colors)}."
        )
    # Set Justification Method for Tet
    text = Text(message, justify=justify_text)  # type: ignore
    # Get the length of the message
    size = len(text)

    # , Select starting color
    color = random.choice(all_colors)
    chosen_index = all_colors.index(color)  # Get index of chosen color
    color_indexes = [chosen_index]  # Add chosen index to list of indexes
    # console.log(f"Chosen Index: {chosen_index}")  # Log chosen index

    # , Get the indexes of the other colors
    for i in range(1, num_of_gradients + 1):
        next_index = chosen_index + i
        if next_index > len(all_colors):
            next_index = next_index - len(all_colors)
        color_indexes.append(next_index)  # type: ignore
    # console.log(f"Color Indexes: {color_indexes}")

    # , Get the colors for the gradient
    color_range = []  # type: ignore
    for x, i in enumerate(color_indexes):
        next_color = all_colors[i - 1]
        color_range.append(next_color)

    # Determine the size of the gradient
    gradient_size = size // (num_of_gradients - 1)
    gradient_text = Text()

    # , Determine the substring for each gradient
    for index in range(0, num_of_gradients):
        begin = index * gradient_size
        end = begin + gradient_size
        sub_string = text[begin:end]

        if index < num_of_gradients:
            color1 = Color.parse(color_range[index])
            color1_triplet = color1.triplet
            r1 = color1_triplet[0]  # type: ignore
            g1 = color1_triplet[1]  # type: ignore
            b1 = color1_triplet[2]  # type: ignore
            color2 = Color.parse(color_range[index + 1])
            color2_triplet = color2.triplet
            r2 = color2_triplet[0]  # type: ignore
            g2 = color2_triplet[1]  # type: ignore
            b2 = color2_triplet[2]  # type: ignore
            dr = r2 - r1
            dg = g2 - g1
            db = b2 - b1

        # Apply the gradient to each character
        for index in range(gradient_size):
            blend = index / gradient_size
            color = f"#{int(r1 + dr * blend):02X}{int(g1 + dg * blend):02X}{int(b1 + db * blend):02X}"  # type: ignore
            sub_string.stylize(color, index, index + 1)

        gradient_text = Text.assemble(gradient_text, sub_string, tab_size=4, justify=justify_text)  # type: ignore

    if gradient_title:
        panel_title = gradient(f"{title}")

        gradient_panel = Panel(
            gradient_text,
            box=box,
            title=panel_title,
            title_align=title_align,
            subtitle=f"[grey]{subtitle}[/grey]",
            subtitle_align=subtitle_align,
            expand=expand,
            border_style=border_style,
            width=width,
            height=height,
            padding=padding,
        )
        return gradient_panel
    else:
        gradient_panel = Panel(
            gradient_text,
            box=box,
            title=f"[bold bright_white]{title}[/bold bright_white]",
            title_align=title_align,
            subtitle=f"[grey]{subtitle}[/grey]",
            subtitle_align=subtitle_align,
            expand=expand,
            border_style=border_style,
            width=width,
            height=height,
            padding=padding,
        )
        return gradient_panel


def gradient_panel_demo():
    text = "\tEnim tempor veniam proident. Reprehenderit deserunt do duis laboris laborum consectetur fugiat deserunt officia officia eu consequat. Aute sint occaecat adipisicing eu aute. Eu est laborum enim deserunt fugiat nostrud officia do ad cupidatat enim amet cillum amet. Consectetur occaecat ex quis irure cupidatat amet occaecat ad sit adipisicing pariatur est velit mollit voluptate. Eiusmod deserunt nisi voluptate irure. Sunt irure consectetur veniam dolore elit officia et in labore esse esse cupidatat labore. Fugiat enim irure ipsum eiusmod consequat irure commodo cillum.\n\n\tReprehenderit ea quis aliqua qui labore enim consequat ea nostrud voluptate amet reprehenderit consequat sunt. Ad est occaecat mollit qui sit enim do esse aute sint nulla sint laborum. Voluptate veniam ut Lorem eiusmod id veniam amet ipsum labore incididunt. Ex in consequat voluptate mollit nisi incididunt pariatur ipsum ut eiusmod ut cupidatat elit. Eu irure est ad nulla exercitation. Esse elit tempor reprehenderit ipsum eu officia sint.\n\n\tCupidatat officia incididunt cupidatat minim fugiat sit exercitation ullamco occaecat est officia ut occaecat labore. Id consectetur cupidatat amet aute. Pariatur nostrud enim reprehenderit aliqua. Elit deserunt excepteur aute aliquip."

    console.print(
        gradient_panel(
            text,
            title="Hello World",
            subtitle="The Cake is a Lie",
            num_of_gradients=5,
            justify_text="left",
            gradient_title=True,
        ),
        justify="center",
    )


# . ─────────────────── Run ─────────────────────────────────
@log.catch
def get_last_run() -> int:
    """Get the last run number from the run.txt file."""
    with open("logs/run.txt", "r") as infile:
        last_run = int(infile.read())
        # console.log(f"Last Run: {last_run}")
        return last_run


@log.catch
def update_run(last_run: int, write: bool = True) -> int:
    """Update the run.txt file with the next run number."""
    run = last_run + 1
    if write:
        with open(run_file, "w") as outfile:
            outfile.write(str(run))
    return run


@log.catch
def new_run() -> int:
    """Get the next run number."""
    last_run = get_last_run()
    run = update_run(last_run)
    console.clear()
    run_string = gradient(f"Run {run}")
    console.rule(title=run_string, style="value")
    return run


current_run = new_run()

# . ──────────────────── Log Sinks  ───────────────────────────────
BASE = Path.cwd()
VERBOSE_LOB = BASE / "logs" / "verbose.log"
LOG = BASE / "logs" / "log.log"
def log_init(existing_console: Optional[Console]) -> Logger: # type: ignore
    """
    Configure Loguru Logger Sinks for the module.

    Args:
        `existing_console` (Optional[Console]): An existing console object to use for logging. If None, a new console will be created.add()

    Returns:
        `log` (Logger): A configured Loguru Logger object.
    """
    console = validate_console(console=MaxConsole().console)

    sinks = log.configure(
        handlers=[
            # _. Debug
            # Loguru Logger
            dict(  # . debug.log
                sink=VERBOSE_LOB,
                level="DEBUG",
                format="Run {extra[run]} | {time:hh:mm:ss:SSS A} | {file.name: ^13} |  Line {line: ^5} | {level: <8}ﰲ  {message}",
                rotation="10 MB",
            ),
            # _, INFO
            # Loguru Logger
            dict(
                sink=LOG,
                level="INFO",
                format="Run {extra[run]} | {time:hh:mm:ss:SSS A} | {file.name: ^13} |  Line {line: ^5} | {level: <8}ﰲ  {message}",
                rotation="10 MB",
            ),
            # _, INFO
            # Rich Console Log
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
            #! ERROR
            # Rich Console Log
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

    log.debug(f"Initialized Logger")
