from io import StringIO
import re
import os
from secrets import choice
from ujson import load, dump
from io import StringIO
from pathlib import Path
from typing import List, Dict
from rich import print
from rich.style import Style
from rich.text import Text
from rich.pretty import pprint, Pretty
from rich.panel import Panel
from rich.prompt import Prompt
from rich.layout import Layout
from maxsetup.console import console, progress
from alive_progress import alive_bar

BASE = Path.cwd()

layout = Layout(name="root")
layout.split_row(
    Layout(name="left"),
    Layout(name="right"),
)


# choice = Prompt.ask(
#     "Get the escaped content of which file?", default='f"{BASE}/'
#     )


def get_file(path: Path) -> str:
    """Get the file content."""
    console.print(f"Getting file content of [bold green]{path}[/]")
    with open(path, "r") as infile:
        content = infile.read()
    return content


def process_file(content: str) -> str:
    """Escape the file content."""
    content_t = content.replace("    ", r"\t")
    content_n = content_t.replace("\n", r"\n")
    content_q = content_n.replace('"', r"\"")
    escaped_content = content_q.replace("'", r"\'")
    return escaped_content


def get_left_panel(content: str, path: Path) -> Panel:
    pretty_content = Pretty(content)
    filename = path.name
    content_panel = Panel(
        pretty_content,
        title="[#c7c7c7]File Content[/]",
        title_align="left",
        border_style=Style(color="#004416", bold=True),
        expand=True,
        subtitle=f"[#b8b8b8]{filename}[/]",
        subtitle_align="right",
        height=30,
    )
    return content_panel


def get_right_panel(content: str, path: Path) -> Panel:
    pretty_content = Pretty(content)
    filename = path.name
    escaped_panel = Panel(
        pretty_content,
        title="[#aeffa8]File Content[/]",
        title_align="left",
        border_style=Style(color="#00cf41", bold=True),
        expand=True,
        subtitle=f"[#b8b8b8]{filename}[/]",
        subtitle_align="right",
        height=30,
    )
    return escaped_panel


def iterate_files() -> dict:
    """
    compress file content
    """
    BASE = Path.cwd()
    ignore_dirs = ["__pycache__", "maxsetup", "tasks"]
    ignore_files = [".DS_Store", "maxsetup.code-workspace"]
    compressed_content = {}  # compress_content
    files = []
    file_count = 0
    dirs = [BASE]
    dir_count = 0

    for dir in dirs:
        for item in dir.iterdir():
            if item.is_dir():
                if item.name not in ignore_dirs:
                    dir_count += 1
                    dirs.append(Path(item))
            else:
                if item.name not in ignore_files:
                    file_count += 1
                    files.append(Path(item))


    with progress:
        task = progress.add_task("[bold green]Compressing...", total=file_count)
        for file in files:
            filename = file.name
            progress.update(task, advance=1, description=f"[bold green]Compressing {filename}...")
            content = get_file(file)
            escaped_content = process_file(content)
            compressed_content[file.name] = {
                "path": Path(file),
                "content": content,
                "escaped content": escaped_content,
            }
            with open(f"{BASE}/tasks/{filename}.txt", "w") as outfile:
                outfile.write(escaped_content)

        with open(f"{BASE}/tasks/compressed_content.json", "w") as outfile:
            dump(compressed_content, outfile, indent=4)

    return compressed_content


def main():
    compressed_content = iterate_files()
    keys = list(compressed_content.keys())
    for key in keys:
        path = Path(compressed_content[key]["path"])
        content = compressed_content[key]["content"]
        escaped_content = compressed_content[key]["escaped content"]
        left_panel = get_left_panel(content, path)
        right_panel = get_right_panel(escaped_content, path)
        layout["left"].update(left_panel)
        layout["right"].update(right_panel)
        console.print(layout)

if __name__ == "__main__":
    with open (f"{BASE}/static/style.css") as infile:
        lines = infile.readlines()

        new_lines = ""
        for line in lines:
            newlines = f"{new_lines}\n\"{line}\""

        console.print(new_lines)