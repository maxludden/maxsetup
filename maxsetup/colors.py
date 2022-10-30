# maxsetup/colors.py
import colorsys
import re
from pathlib import Path
from typing import Optional, Tuple, Type, Set
from enum import Enum

from functools import lru_cache, singledispatch
from typer import Typer, Argument, Option
from json import load, dump
from inspect import currentframe, getframeinfo
from pathlib import Path
from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.color import Color, ColorSystem, ColorParseError
from rich.color_triplet import ColorTriplet
from maxsetup.console import console, validate_console
from random import choice
from sh import Command


console = validate_console(console)

class InvalidHexColor(ColorParseError):
    pass

class InvalidRGBColor(ColorParseError):
    pass

class InvalidColor(Exception):
    pass

class ColorType (Enum):
    """Enum class for the different color types."""
    hex = "hex"
    rgb = "rgb"
    ansi = "ansi"
    w3 = "w3"
    invalid = "invalid"


# Compile regex patters for color parsing
HEX_REGEX = re.compile(r"^\#([0-9a-fA-F]{6})$|^ ([0-9a-fA-F]{6})$", re.VERBOSE)
ANSI_REGEX = re.compile(r"color\(([0-9]{1,3})\)$", re.VERBOSE)
RGB_REGEX = re.compile(r"rgb\(([\d\s,]+)\)$", re.VERBOSE)
COLOR_REGEX = re.compile(r"^\#([0-9a-fA-F]{6})$|^ ([0-9a-fA-F]{6})$|color\(([0-9]{1,3})\)$|rgb\(([\d\s,]+)\)$", re.VERBOSE)
# Static Files

@lru_cache
def get_ansi_colors() -> dict:
    """Generate a dictionary with using ANSI color integers as keys and the name of the color as the value."""
    ANSI_COLORS = {
    "0": "black",
    "1": "red",
    "2": "green",
    "3": "yellow",
    "4": "blue",
    "5": "magenta",
    "6": "cyan",
    "7": "white",
    "8": "bright_black",
    "9": "bright_red",
    "10": "bright_green",
    "11": "bright_yellow",
    "12": "bright_blue",
    "13": "bright_magenta",
    "14": "bright_cyan",
    "15": "bright_white",
    "16": "gray0",
    "17": "navy_blue",
    "18": "dark_blue",
    "20": "blue3",
    "21": "blue1",
    "22": "dark_green",
    "25": "deep_sky_blue4",
    "26": "dodger_blue3",
    "27": "dodger_blue2",
    "28": "green4",
    "29": "spring_green4",
    "30": "turquoise4",
    "32": "deep_sky_blue3",
    "33": "dodger_blue1",
    "40": "green3",
    "41": "spring_green3",
    "36": "dark_cyan",
    "37": "light_sea_green",
    "38": "deep_sky_blue2",
    "39": "deep_sky_blue1",
    "47": "spring_green2",
    "43": "cyan3",
    "44": "dark_turquoise",
    "45": "turquoise2",
    "46": "green1",
    "48": "spring_green1",
    "49": "medium_spring_green",
    "50": "cyan2",
    "51": "cyan1",
    "88": "dark_red",
    "125": "deep_pink4",
    "55": "purple4",
    "56": "purple3",
    "57": "blue_violet",
    "94": "orange4",
    "59": "gray37",
    "60": "medium_purple4",
    "62": "slate_blue3",
    "63": "royal_blue1",
    "64": "chartreuse4",
    "71": "dark_sea_green4",
    "66": "pale_turquoise4",
    "67": "steel_blue",
    "68": "steel_blue3",
    "69": "cornflower_blue",
    "76": "chartreuse3",
    "73": "cadet_blue",
    "74": "sky_blue3",
    "81": "steel_blue1",
    "114": "pale_green3",
    "78": "sea_green3",
    "79": "aquamarine3",
    "80": "medium_turquoise",
    "112": "chartreuse2",
    "83": "sea_green2",
    "85": "sea_green1",
    "122": "aquamarine1",
    "87": "dark_slate_gray2",
    "91": "dark_magenta",
    "128": "dark_violet",
    "129": "purple",
    "95": "light_pink4",
    "96": "plum4",
    "98": "medium_purple3",
    "99": "slate_blue1",
    "106": "yellow4",
    "101": "wheat4",
    "102": "gray53",
    "103": "light_slate_gray",
    "104": "medium_purple",
    "105": "light_slate_blue",
    "149": "dark_olive_green3",
    "108": "dark_sea_green",
    "110": "light_sky_blue3",
    "111": "sky_blue2",
    "150": "dark_sea_green3",
    "116": "dark_slate_gray3",
    "117": "sky_blue1",
    "118": "chartreuse1",
    "120": "light_green",
    "156": "pale_green1",
    "123": "dark_slate_gray1",
    "160": "red3",
    "126": "medium_violet_red",
    "164": "magenta3",
    "166": "dark_orange3",
    "167": "indian_red",
    "168": "hot_pink3",
    "133": "medium_orchid3",
    "134": "medium_orchid",
    "140": "medium_purple2",
    "136": "dark_goldenrod",
    "173": "light_salmon3",
    "138": "rosy_brown",
    "139": "gray63",
    "141": "medium_purple1",
    "178": "gold3",
    "143": "dark_khaki",
    "144": "navajo_white3",
    "145": "gray69",
    "146": "light_steel_blue3",
    "147": "light_steel_blue",
    "184": "yellow3",
    "157": "dark_sea_green2",
    "152": "light_cyan3",
    "153": "light_sky_blue1",
    "154": "green_yellow",
    "155": "dark_olive_green2",
    "193": "dark_sea_green1",
    "159": "pale_turquoise1",
    "162": "deep_pink3",
    "200": "magenta2",
    "169": "hot_pink2",
    "170": "orchid",
    "207": "medium_orchid1",
    "172": "orange3",
    "174": "light_pink3",
    "175": "pink3",
    "176": "plum3",
    "177": "violet",
    "179": "light_goldenrod3",
    "180": "tan",
    "181": "misty_rose3",
    "182": "thistle3",
    "183": "plum2",
    "185": "khaki3",
    "222": "light_goldenrod2",
    "187": "light_yellow3",
    "188": "gray84",
    "189": "light_steel_blue1",
    "190": "yellow2",
    "192": "dark_olive_green1",
    "194": "honeydew2",
    "195": "light_cyan1",
    "196": "red1",
    "197": "deep_pink2",
    "199": "deep_pink1",
    "201": "magenta1",
    "202": "orange_red1",
    "204": "indian_red1",
    "206": "hot_pink",
    "208": "dark_orange",
    "209": "salmon1",
    "210": "light_coral",
    "211": "pale_violet_red1",
    "212": "orchid2",
    "213": "orchid1",
    "214": "orange1",
    "215": "sandy_brown",
    "216": "light_salmon1",
    "217": "light_pink1",
    "218": "pink1",
    "219": "plum1",
    "220": "gold1",
    "223": "navajo_white1",
    "224": "misty_rose1",
    "225": "thistle1",
    "226": "yellow1",
    "227": "light_goldenrod1",
    "228": "khaki1",
    "229": "wheat1",
    "230": "cornsilk1",
    "231": "gray100",
    "232": "gray3",
    "233": "gray7",
    "234": "gray11",
    "235": "gray15",
    "236": "gray19",
    "237": "gray23",
    "238": "gray27",
    "239": "gray30",
    "240": "gray35",
    "241": "gray39",
    "242": "gray42",
    "243": "gray46",
    "244": "gray50",
    "245": "gray54",
    "246": "gray58",
    "247": "gray62",
    "248": "gray66",
    "249": "gray70",
    "250": "gray74",
    "251": "gray78",
    "252": "gray82",
    "253": "gray85",
    "254": "gray89",
    "255": "gray93"
}
    return ANSI_COLORS

@lru_cache
def get_colors_ansi() -> dict:
    """Generate a dictionary with using W3 colors as keys and their ansi integers values."""
    COLORS_ANSI = {
        "black": 0,
        "red": 1,
        "green": 2,
        "yellow": 3,
        "blue": 4,
        "magenta": 5,
        "cyan": 6,
        "white": 7,
        "bright_black": 8,
        "bright_red": 9,
        "bright_green": 10,
        "bright_yellow": 11,
        "bright_blue": 12,
        "bright_magenta": 13,
        "bright_cyan": 14,
        "bright_white": 15,
        "grey0": 16,
        "gray0": 16,
        "navy_blue": 17,
        "dark_blue": 18,
        "blue3": 20,
        "blue1": 21,
        "dark_green": 22,
        "deep_sky_blue4": 25,
        "dodger_blue3": 26,
        "dodger_blue2": 27,
        "green4": 28,
        "spring_green4": 29,
        "turquoise4": 30,
        "deep_sky_blue3": 32,
        "dodger_blue1": 33,
        "green3": 40,
        "spring_green3": 41,
        "dark_cyan": 36,
        "light_sea_green": 37,
        "deep_sky_blue2": 38,
        "deep_sky_blue1": 39,
        "spring_green2": 47,
        "cyan3": 43,
        "dark_turquoise": 44,
        "turquoise2": 45,
        "green1": 46,
        "spring_green1": 48,
        "medium_spring_green": 49,
        "cyan2": 50,
        "cyan1": 51,
        "dark_red": 88,
        "deep_pink4": 125,
        "purple4": 55,
        "purple3": 56,
        "blue_violet": 57,
        "orange4": 94,
        "grey37": 59,
        "gray37": 59,
        "medium_purple4": 60,
        "slate_blue3": 62,
        "royal_blue1": 63,
        "chartreuse4": 64,
        "dark_sea_green4": 71,
        "pale_turquoise4": 66,
        "steel_blue": 67,
        "steel_blue3": 68,
        "cornflower_blue": 69,
        "chartreuse3": 76,
        "cadet_blue": 73,
        "sky_blue3": 74,
        "steel_blue1": 81,
        "pale_green3": 114,
        "sea_green3": 78,
        "aquamarine3": 79,
        "medium_turquoise": 80,
        "chartreuse2": 112,
        "sea_green2": 83,
        "sea_green1": 85,
        "aquamarine1": 122,
        "dark_slate_gray2": 87,
        "dark_magenta": 91,
        "dark_violet": 128,
        "purple": 129,
        "light_pink4": 95,
        "plum4": 96,
        "medium_purple3": 98,
        "slate_blue1": 99,
        "yellow4": 106,
        "wheat4": 101,
        "grey53": 102,
        "gray53": 102,
        "light_slate_grey": 103,
        "light_slate_gray": 103,
        "medium_purple": 104,
        "light_slate_blue": 105,
        "dark_olive_green3": 149,
        "dark_sea_green": 108,
        "light_sky_blue3": 110,
        "sky_blue2": 111,
        "dark_sea_green3": 150,
        "dark_slate_gray3": 116,
        "sky_blue1": 117,
        "chartreuse1": 118,
        "light_green": 120,
        "pale_green1": 156,
        "dark_slate_gray1": 123,
        "red3": 160,
        "medium_violet_red": 126,
        "magenta3": 164,
        "dark_orange3": 166,
        "indian_red": 167,
        "hot_pink3": 168,
        "medium_orchid3": 133,
        "medium_orchid": 134,
        "medium_purple2": 140,
        "dark_goldenrod": 136,
        "light_salmon3": 173,
        "rosy_brown": 138,
        "grey63": 139,
        "gray63": 139,
        "medium_purple1": 141,
        "gold3": 178,
        "dark_khaki": 143,
        "navajo_white3": 144,
        "grey69": 145,
        "gray69": 145,
        "light_steel_blue3": 146,
        "light_steel_blue": 147,
        "yellow3": 184,
        "dark_sea_green2": 157,
        "light_cyan3": 152,
        "light_sky_blue1": 153,
        "green_yellow": 154,
        "dark_olive_green2": 155,
        "dark_sea_green1": 193,
        "pale_turquoise1": 159,
        "deep_pink3": 162,
        "magenta2": 200,
        "hot_pink2": 169,
        "orchid": 170,
        "medium_orchid1": 207,
        "orange3": 172,
        "light_pink3": 174,
        "pink3": 175,
        "plum3": 176,
        "violet": 177,
        "light_goldenrod3": 179,
        "tan": 180,
        "misty_rose3": 181,
        "thistle3": 182,
        "plum2": 183,
        "khaki3": 185,
        "light_goldenrod2": 222,
        "light_yellow3": 187,
        "grey84": 188,
        "gray84": 188,
        "light_steel_blue1": 189,
        "yellow2": 190,
        "dark_olive_green1": 192,
        "honeydew2": 194,
        "light_cyan1": 195,
        "red1": 196,
        "deep_pink2": 197,
        "deep_pink1": 199,
        "magenta1": 201,
        "orange_red1": 202,
        "indian_red1": 204,
        "hot_pink": 206,
        "dark_orange": 208,
        "salmon1": 209,
        "light_coral": 210,
        "pale_violet_red1": 211,
        "orchid2": 212,
        "orchid1": 213,
        "orange1": 214,
        "sandy_brown": 215,
        "light_salmon1": 216,
        "light_pink1": 217,
        "pink1": 218,
        "plum1": 219,
        "gold1": 220,
        "navajo_white1": 223,
        "misty_rose1": 224,
        "thistle1": 225,
        "yellow1": 226,
        "light_goldenrod1": 227,
        "khaki1": 228,
        "wheat1": 229,
        "cornsilk1": 230,
        "grey100": 231,
        "gray100": 231,
        "grey3": 232,
        "gray3": 232,
        "grey7": 233,
        "gray7": 233,
        "grey11": 234,
        "gray11": 234,
        "grey15": 235,
        "gray15": 235,
        "grey19": 236,
        "gray19": 236,
        "grey23": 237,
        "gray23": 237,
        "grey27": 238,
        "gray27": 238,
        "grey30": 239,
        "gray30": 239,
        "grey35": 240,
        "gray35": 240,
        "grey39": 241,
        "gray39": 241,
        "grey42": 242,
        "gray42": 242,
        "grey46": 243,
        "gray46": 243,
        "grey50": 244,
        "gray50": 244,
        "grey54": 245,
        "gray54": 245,
        "grey58": 246,
        "gray58": 246,
        "grey62": 247,
        "gray62": 247,
        "grey66": 248,
        "gray66": 248,
        "grey70": 249,
        "gray70": 249,
        "grey74": 250,
        "gray74": 250,
        "grey78": 251,
        "gray78": 251,
        "grey82": 252,
        "gray82": 252,
        "grey85": 253,
        "gray85": 253,
        "grey89": 254,
        "gray89": 254,
        "grey93": 255,
        "gray93": 255
    }
    return COLORS_ANSI


# Generate the ANSI dictionaries
ANSI_COLORS = get_ansi_colors()
ANSI_NUMBERS = ANSI_COLORS.keys()
COLORS_ANSI = get_colors_ansi()
W3_COLORS = COLORS_ANSI.keys()

@singledispatch
def valid_ansi(color) -> bool:
    """Check if the color is a valid ANSI color.Color can be an ANSI number or a W3 Color.

    Args:
        color (int | str): The color to check.

    Returns:
        bool: True if the color is valid, False otherwise.
    """
    return False

@valid_ansi.register(int)
def _(color: int) -> bool:
   """
   Check if the color is a valid ANSI color.Color can be an ANSI number or a W3 Color.

    Args:
        color (int): The color to check.

    Returns:
        bool: True if the color is valid, False otherwise.
    """
    if color in ANSI_NUMBERS: # type: ignore
        return True
    else:
        return False

@valid_ansi.register(str) # type: ignore
def _(color: str) -> bool:
    """
    Check if the color is a valid ANSI color.Color can be an ANSI number or a W3 Color.

    Args:
        color (str): The color to check.

    Returns:
        bool: True if the color is valid, False otherwise.
    """
    if color in W3_COLORS: # type: ignore
        return True
    else:
        return False

def valid_hex(color: str) -> bool:
    """Check if the color is a valid HEX Color.

        Args:
            color (str): The color to check.

        Returns:
            bool: True if the color is valid, False otherwise.
    """
    if re.match(HEX_REGEX, color):
        return True
    else:
        return False



@singledispatch
def get_color_type(color: int|str|tuple) -> ColorType:  # type: ignore
    """
    Validate a hex color.

    Args:
        hex (str): The hex color.

    Returns:
        bool: True if the hex color is valid, False otherwise.
    """
    if isinstance(color, int):
        assert color in ANSI_NUMBERS, f'Invalid ANSI color: {color}'
        return ColorType.ansi

    elif isinstance(color, str):
        if HEX_REGEX.match(color):
            return ColorType.hex
        elif color in W3_COLORS:
            return ColorType.w3
        else:
            return ColorType.invalid

    elif isinstance(color, tuple):
        assert len(color) == 3, f'Invalid RGB color: {color}'
        for i in color:
            assert i in range(0, 256), f'Invalid RGB color: {color}'
        return ColorType.rgb

    else:
        raise InvalidColor(f'Invalid color: {color}')


def hex_to_rgb(hex: str) -> Tuple:
    """
    Convert a hex color to rgb.

    Args:
        hex (str): The hex color.

    Returns:
        rgb (tuple): The rgb color.
    """
    if HEX_REGEX.match(hex):
        rgb = []
        for i in (0, 2, 4):
            decimal = int(hex[i:i+2], 16)
            rgb.append(decimal)
        return tuple(rgb)
    else:
        raise InvalidHexColor(f'Invalid hex color: {hex}')


def rgb_to_hex(rgb: Tuple[int,int,int]) -> str:
    """Convert an rgb color to hex."""
    r, g, b = rgb

    return ('{:X}{:X}{:X}').format(r, g, b)



colors = [
    "red",
    "orange_red1",
    "yellow",
    "green",
    "cyan",
    "blue",
    "blue_violet",
    "purple",
    "magenta",
]
true_colors = []
for color in colors:
    true_colors.append(Color.parse(f"{color}"))

for color in true_colors:
    print(f'[bold {color}] {color.name} [/bold {color}]')


shades = [
    "white",
    "light_grey",
    "grey",
    "dark_grey",
    "black",
]
true_shades = []
for shade in shades:
    true_shades.append(Color.parse(shade))
