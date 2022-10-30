from __future__ import annotations
import re

from inspect import currentframe, getframeinfo
from pathlib import Path
from random import choice
from time import perf_counter
from typing import List, Optional

import ujson as json
from loguru import Logger
from loguru import logger as log
from maxsetup.console import console, progress
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
