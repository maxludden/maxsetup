# static/setup_files.py
import ujson as json
from pathlib import Path
from typing import List, Optional
from rich import print
from maxsetup.console import console, progress

BASE = Path.cwd()
DOTENV_FILEPATH = BASE / ".env"
LICENSE_FILEPATH = BASE / "LICENSE"
GITIGNORE_FILEPATH = BASE / ".gitignore"
VSCODE_DIR = BASE / ".vscode"
LAUNCH_FILEPATH = VSCODE_DIR / "launch.json"
STATIC_DIR = BASE / "static"
CSS_FILEPATH = STATIC_DIR / "style.css"
CONFIG_DIR = BASE / "config"
CSPELL_FILEPATH = CONFIG_DIR / "cspell.json"
LOGS_DIR = BASE / "logs"
RUN_FILEPATH =  LOGS_DIR / "run.text"
LOG_FILEPATH = LOGS_DIR / 'log.log'
VERBOSE_LOG_FILEPATH = LOGS_DIR / 'verbose.log'

DIRS = [BASE, CONFIG_DIR, LOGS_DIR, VSCODE_DIR]
FILEPATHS = [DOTENV_FILEPATH, LICENSE_FILEPATH, GITIGNORE_FILEPATH, LAUNCH_FILEPATH, CSS_FILEPATH, CSPELL_FILEPATH, RUN_FILEPATH, LOG_FILEPATH,VERBOSE_LOG_FILEPATH]

FILES = [
        {
            "file": "launch.json",
            "type": "json",
            "filepath": LAUNCH_FILEPATH,
            "content": """{\n\t\"version\": \"0.2.0\",\n\t\"configurations\": [\n\t\t{\n\t\t\t\"name\": \"Python: Current File\",\n\t\t\t\"type\": \"python\",\n\t\t\t\"request\": \"launch\",\n\t\t\t\"program\": \"${file}\",\n\t\t\t\"console\": \"integratedTerminal\",\n\t\t\t\"justMyCode\": true\n\t\t}\n\t]\n}""",
        },
        {
            "file": "settings.json",
            "type": "json",
            "filepath": f"{BASE}/.vscode/settings.json",
            "content": """{\n\t\"files.trimFinalNewlines\": true,\n\t\"files.trimTrailingWhitespace\": true,\n\t\"breadcrumbs.showModules\": true,\n\t\"markdown.preview.fontFamily\": \"\'Century Gothic\',\' MesloLGS NF\', \'Ubuntu\', sans-serif\",\n\t\"editor.fontFamily\": \"\'MesloLGS NF\', Menlo, Monaco, \'Courier New\', monospace\",\n\t\"editor.fontSize\": 14,\n\t\"editor.formatOnSave\": true,\n\t\"cSpell.customDictionaries\": {\n\t\t\"project-words\": {\n\t\t\t\"name\": \"cspell\",\n\t\t\t\"path\": \"${workspaceRoot}/config/cspell.txt\",\n\t\t\t\"description\": \"Words used in the configured project.\",\n\t\t\t\"addWords\": true\n\t\t}\n\t},\n\t\"[python]\": {\n\t\t\"editor.defaultFormatter\": \"ms-python.python\"\n\t}\n}"""
        },
        {
            "file": "tasks.json",
            "type": "json",
            "filepath": f"{BASE}/.vscode/tasks.json",
            "content": """{\n\t\"version\": \"2.0.0\",\n\t\"tasks\": [\n\t\t{\n\t\t\t\"label\": \"Get Escaped File\",\n\t\t\t\"command\": \"/Users/maxludden/dev/venvs/maxsetup/bin/python /Users/maxludden/dev/py/maxsetup/tasks/compress.py\",\n\t\t\t\"type\": \"shell\",\n\t\t\t\"group\": {\n\t\t\t\t\"kind\": \"none\",\n\t\t\t\t\"isDefault\": false\n\t\t\t},\n\t\t\t\"presentation\": {\n\t\t\t\t\"echo\": false,\n\t\t\t\t\"reveal\": \"always\",\n\t\t\t\t\"focus\": false,\n\t\t\t\t\"panel\": \"shared\",\n\t\t\t\t\"showReuseMessage\": true,\n\t\t\t\t\"clear\": false\n\t\t\t},\n\t\t\t\"icon\": {\n\t\t\t\t\"id\": \"symbol-type-parameter\",\n\t\t\t\t\"color\": \"terminal.ansiCyan\"\n\t\t\t},\n\t\t\t\"runOptions\": {\n\t\t\t\t\"runOn\": \"default\",\n\t\t\t\t\"instanceLimit\": 1,\n\t\t\t\t\"reevaluateOnRerun\": true\n\t\t\t}\n\t\t}\n\t]\n}"""
        },
        {
            "file": ".env",
            "type": ".env",
            "filepath": f"{BASE}/.env",
            "content": "# Pushover API\nAPI_TOKEN=\'ah886i93nwk9kxoynn8yv2fs7u7hat\'\nUSER_KEY=\'u2e5o1f8rw47xi6hhyfx1j7en2udvr\'\n\n# Push Notifications\n\n## Notion API\nNOTION_API=\'secret_wTizeCKRE5NpC4B2ykexju80BqON4C2NYh3ojRED5lm\'\nNOTION_DB_CHAPTER=\'dbc4f31d755a4c36824630532a831a74\'\n\n# MongoDb Atlas (private)- DB: Supergene\n\n## MongoDB Connection String\nSUPERGENE=\'mongodb+srv://dev:uqt4QTX6fmg*zjb4fej@maxludden.wmopsoc.mongodb.net/SUPERGENE\'\n\n# Data API\nDATA_API_KEY=\'admin\'\nDATA_API_TOKEN=\'K9YPuPXbV5Ts0RUES9cRYNiN9QNM3t05sLAH2RLTyAB61A09IZUrXAUuW6wQheEy\'"
        },
        {
            "file": "CSpell.json",
            "type": "json",
            "filepath": f"{BASE}/config/cspell.json",
            "content": """{\n\t\"version\": \"0.2\",\n\t\"ignorePaths\": [],\n\t\"dictionaryDefinitions\": [\n\t\t{\n\t\t\t\"name\": \"cspell\",\n\t\t\t\"path\": \"${workspaceRoot}/config/cspell.txt\",\n\t\t\t\"description\": \"Custom words for cspell\",\n\t\t\t\"type\": \"S\",\n\t\t\t\"addWords\": true,\n\t\t\t\"useCompounds\": true,\n\t\t\t\"scope\": \"folder\"\n\t\t}\n\t],\n\t\"dictionaries\": [],\n\t\"words\": [],\n\t\"ignoreWords\": [],\n\t\"import\": []\n}\n"""
        },
        {
            "file": "cspell.txt",
            "type": "txt",
            "filepath": f"{BASE}/config/cspell.txt",
            "content": """CKRE\nhhyfx\nkxoynn\nMenlo\nTize\nudvr\nykexju\n"""
        },
        {
            "file": "style.css",
            "type": "css",
            "filepath": f"{BASE}/static/style copy.css",
            "content": "@charset \"utf-8\";\n\n/* This stylesheet was created by Max Ludden to use for ebooks I created. Like everything else in this module, it is under the MIT License, so use it if you like it. */\n:root {\n\t--main-color: #000000;\n\t--main-bg-color: #ffffff;\n\t--main-border-color: #bbbbbb;\n\t--alternate-color: #222222;\n\t--alternate-bg-color: #efefef;\n\t--alternate-border-color: #2e2e2e;\n\t--table-header-bg-color: #222222;\n\t--link-color: #61008e;\n\t--title-color: #61008e;\n}\n\n@media (prefers-color-scheme: dark) {\n\t:root {\n\t\t--main-color: #eeeeee;\n\t\t--main-bg-color: #222222;\n\t\t--main-border-color: #aaaaaa;\n\t\t--alternate-color: #dddddd;\n\t\t--alternate-bg-color: #444444;\n\t\t--alternate-border-color: #2e2e2e;\n\t\t--table-header-bg-color: #aaaaaa;\n\t\t--link-color: #61008e;\n\t\t--title-color: #d98eff;\n\t}\n}\n\n/**** Fonts *******/\n@font-face {\n\tfont-family: \"Urbanist-Thin\";\n\tfont-style: normal;\n\tsrc: \"Urbanist-Thin.ttf\"\n}\n\n@font-face {\n\tfont-family: \"Urbanist-ThinItalic\";\n\tfont-style: normal;\n\tsrc: \"Urbanist-thinItalic.ttf\"\n}\n\n@font-face {\n\tfont-family: \"Urbanist-Regular\";\n\tfont-style: normal;\n\tsrc: \"Urbanist-Regular.ttf\"\n}\n\n@font-face {\n\tfont-family: \"Urbanist-Italic\";\n\tfont-style: italic;\n\tsrc: \"Urbanist-Italic.ttf\"\n}\n\n@font-face {\n\tfont-family: \"Urbanist-Black\";\n\tfont-style: normal;\n\tfont_weight: bold;\n\tsrc: \"Urbanist-Black.ttf\"\n}\n\n@font-face {\n\tfont-family: \"Urbanist-BlackItalic\";\n\tfont-style: normal;\n\tfont_weight: bold;\n\tsrc: \"Urbanist-BlackItalic.ttf\"\n}\n\n@font-face {\n\tfont-family: \"White Modesty\";\n\tfont-style: normal;\n\tsrc: \"White Modesty.ttf\" \";\n\n}\n\n@font-face {\n\tfont-family: \"MesloLGS NF Regular\";\n\tfont-style: normal;\n\tsrc: \"MesloLGS NF Regular.ttf\";\n}\n\n@font-face {\n\tfont-family: \"MesloLGS NF Italic\";\n\tfont-style: italic;\n\tsrc: \"MesloLGS NF Italic.ttf\";\n}\n\n@font-face {\n\tfont-family: \"MesloLGS NF Bold\";\n\tfont-style: normal;\n\tfont-weight: bold;\n\tsrc: \"MesloLGS NF Bold.ttf\";\n}\n\n@font-face {\n\tfont-family: \"MesloLGS NF Bold Italic\";\n\tfont-style: italic;\n\tfont-weight: bold;\n\tsrc: \"MesloLGS NF Bold Italic.ttf\";\n}\n\n@font-face {\n\tfont-family: \"Century Gothic\";\n\tfont-style: normal;\n\tsrc: \"Century Gothic.ttf\";\n}\n\n@font-face {\n\tfont-family: \"Century Gothic Bold\";\n\tfont-style: italic;\n\tsrc: \"Century Gothic Bold.ttf\";\n}\n\n/***** End of Fonts **********/\n\nhtml {\n\tfont-size: 1em;\n\tfont-family: \"Urbanist-Regular\", \"Century Gothic\" -apple-system, BlinkMacSystemFont, \"helvetica neue\", helvetica, roboto, noto, \"segoe ui\", arial, sans-serif;\n\tline-height: 1.2em;\n\tbackground-color: var(--main-bg-color);\n\tcolor: var(--main-color);\n}\n\n/****** Headers *********/\nh1,\nh2,\nh3,\nh4,\nh5 {\n\tdisplay: block;\n\ttext-align: center;\n\tfont-family: \"Urbanist-Regular\", \"Myriad Pro\", helvetica, sans-serif;\n\tfont-style: normal;\n}\n\nh1 {\n\tfont-size: 1.5em;\n\tline-height: 1.2em;\n}\n\nh2 {\n\tfont-size: 1.25em;\n\tline-height: 1.1em;\n\tcolor: var(--alternate-color);\n}\n\nh3 {\n\tfont-size: 1.1em;\n\tline-height: 1em;\n\tfont-family: \"Urbanist-Thin\", \"Myriad Pro\", helvetica, sans-serif;\n\tcolor: var(--title-color);\n}\n\nh4 {\n\tfont-size: 1.1em;\n\tline-height: 1em;\n\tfont-family: \"Urbanist-ThinItalic\", \"Myriad Pro\", helvetica, sans-serif;\n\tcolor: var(--alternate-color);\n}\n\nh5 {\n\tfont-size: 0.9em;\n\tline-height: 1;\n}\n\n/* End of Headers */\n\n/****** Images *********/\nimg {\n\tdisplay: block;\n\tmargin-left: auto;\n\tmargin-right: auto;\n}\n\n/****** End of Images *********/\n\n/************** Body ***************/\nbody {\n\tmargin: 0;\n\tpadding: 1em;\n\tbackground-color: var(--main-bg-color);\n\tcolor: var(--main-color);\n\t-webkit-hyphenate-limit-before: 3;\n\t-webkit-hyphenate-limit-after: 2;\n\t-ms-hyphenate-limit-chars: 6 3 2;\n\t-webkit-hyphenate-limit-lines: 2;\n}\n\n/*********** @media ***********/\n@media(min-width: 390px) {\n\tbody {\n\t\tmargin: auto;\n\t}\n}\n\ntable {\n\tdisplay: table;\n\twidth: 95%;\n\tmargin-left: auto;\n\tmargin-right: auto;\n\tborder: 1px solid var(--main-border-color);\n\tborder-collapse: collapse;\n}\n\nth {\n\tpadding: .5em;\n\tcolor: var(--main-bg-color);\n\tbackground: var(--table-header-bg-color);\n\tfont-family: \"Urbanist-Black\", \"Lemon/Milk\", \"Myriad Pro\", helvetica, sans-serif;\n\tfont-size: 1.5em;\n\ttext-align: center;\n\tborder: 1px solid var(--main-border-color);\n}\n\ntd {\n\tfont-size: 1em;\n\tpadding: 10px;\n\tborder: 1px solid var(--main-border-color);\n\tborder-collapse: collapse;\n\tfont-family: \"Urbanist-Regular\", \"Myriad Pro\", helvetica, sans-serif;\n\ttext-align: center;\n}\n\n.status {\n\tborder: 1px solid var(--main-border-color);\n}\n\n.status td:nth-child(1) {\n\ttext-align: left;\n}\n\n.status td:nth-child(2) {\n\ttext-align: right;\n}\n\n.status tr:nth-child(odd) {\n\tbackground-color: var(--alternate-bg-color);\n}\n\n.status1 {\n\tborder: none;\n}\n\n.status1 td:nth-child(1) {\n\ttext-align: left;\n}\n\n.status1 td:nth-child(2) {\n\ttext-align: right;\n}\n\n.status1 tr:nth-child(odd) {\n\tbackground-color: var(--alternate-bg-color);\n}\n\n.class {\n\ttext-align: center;\n\tfont-family: Urbanist-Thin, Urbanist-Regular, \"Myriad Pro\", helvetica, sans-serif;\n\tfont-size: 0.8em;\n\tbackground-color: var(--main-bg-color);\n\tcolor: var(--main-color);\n\tborder: 1px solid var(--main-border-color);\n}\n\n.geno-r {\n\tborder: 1px solid var(--main-border-color);\n}\n\n.geno-r td:nth-child(1) {\n\ttext-align: left;\n}\n\n.geno-r td:nth-child(2) {\n\ttext-align: right;\n}\n\n.geno {\n\tborder: var(--main-border-color);\n}\n\n.geno td:nth-child(odd) {\n\ttext-align: left;\n}\n\n.geno td:nth-child(even) {\n\ttext-align: right;\n}\n\n.geno tr:nth-child(even) {\n\tbackground-color: var(--alternate-bg-color);\n}\n\n.beast {\n\tborder: none;\n\tborder-top: none;\n\tborder-bottom: none;\n}\n\n.beast td {\n\ttext-align: center;\n}\n\n.type {\n\ttext-align: center;\n\tfont-family: Urbanist-Thin, Urbanist-Regular, \"Myriad Pro\", helvetica, sans-serif;\n\tfont-size: 0.8em;\n\tborder: none;\n}\n\n.beast tr:nth-child(even) {\n\tbackground-color: var(--alternate-bg-color);\n}\n\n.article-reply {\n\twidth: 70%;\n\tpadding: 1.5em;\n\tmargin-left: auto;\n\tmargin-right: auto;\n\tcolor: var(--alternate-color);\n\tbackground-color: var(--alternate-bg-color);\n\tfont-family: Urbanist-Italic;\n\tborder: 1px solid var(--alternate-color);\n\tborder-radius: 5%;\n}\n\n.article {\n\twidth: 70%;\n\tpadding: 1.5em;\n\tmargin-left: auto;\n\tmargin-right: auto;\n\tcolor: var(--alternate-color);\n\tbackground-color: var(--alternate-bg-color);\n\tfont-family: Urbanist-Italic;\n\tborder: 1px solid var(--alternate-color);\n\tborder-radius: 5%;\n}\n\n.alert {\n\tpadding: 1.5em;\n\tmargin-left: auto;\n\tmargin-right: auto;\n\tcolor: var(--alternate-color);\n\tbackground-color: var(--alternate-bg-color);\n\tfont-family: Urbanist-Italic;\n\tborder: 1px solid var(--alternate-color);\n\tborder-radius: 5%;\n}\n\n.article {\n\tpadding: 1.5em;\n\ttext-align: center;\n\tmargin-left: auto;\n\tmargin-right: auto;\n\tcolor: var(--alternate-color);\n\tbackground-color: var(--alternate-bg-color);\n\tfont-family: Urbanist-Italic;\n\tborder: 1px solid var(--alternate-color);\n\tborder-radius: 5%;\n}\n\n.title {\n\tfont-family: \"Urbanist-Black\", \"Lemon/Milk\", \"Myriad Pro\", helvetica, sans-serif;\n\tfont-size: 2em;\n\tline-height: 1.5em;\n\ttext-align: center;\n\ttext-decoration: underline;\n}\n\n.section-title {\n\tfont-family: \"Urbanist-Black\", \"Lemon/Milk\", \"Myriad Pro\", helvetica, sans-serif;\n\tfont-size: 2em;\n\tline-height: 1.5em;\n\ttext-align: center;\n}\n\n.sig {\n\tfont-family: \"White Modesty\";\n\tfont-size: 4em;\n\tline-height: 1.5em;\n\ttext-align: center;\n}\n\n/* Table Div */\n.tables table {\n\tmargin-bottom: 0px;\n\tmargin-top: 0px;\n}\n\n.tables table:last-child {\n\tmargin-bottom: 50px;\n}\n\n.tables table:first-child {\n\tmargin-top: 50px;\n}\n\n.footer {\n\tposition: fixed;\n\tleft: 0;\n\tbottom: 0;\n\twidth: 100%;\n\tbackground-color: var(--main-bg-color);\n\tcolor: var(--main-color);\n\ttext-align: center;\n}\n\n.vertical-center {\n\tmargin: 0;\n\tposition: absolute;\n\ttop: 50%;\n\ttransform: translateY(-50%);\n\t-ms-transform: translateY(-50%);\n}\n\n.center {\n\tdisplay: table;\n\twidth: auto;\n\tmargin-left: auto;\n\tmargin-right: auto;\n}\n\n.center td {\n\ttext-align: center;\n}\n\n.center50 {\n\tdisplay: table;\n\twidth: 50%;\n\tmargin-left: auto;\n\tmargin-right: auto;\n}\n\n.center50 td {\n\ttext-align: center;\n}\n\n.center70 {\n\tdisplay: table;\n\twidth: 70%;\n\tmargin-left: auto;\n\tmargin-right: auto;\n}\n\n.center70 td {\n\ttext-align: center;\n}\n\n.note {\n\tfont-family:\n\t\t\"Urbanist-Thin\",\n\t\t-apple-system,\n\t\tBlinkMacSystemFont,\n\t\t\"helvetica neue\",\n\t\thelvetica,\n\t\troboto,\n\t\tnoto,\n\t\t\"segoe ui\",\n\t\tarial,\n\t\tsans-serif;\n\tfont-size: .8em;\n\ttext-align: center;\n\tmargin-left: auto;\n\tmargin-right: auto;\n}\n\nblockquote {\n\tfont-style: italic;\n\tmargin: 4em 2em;\n\tpadding: 1em;\n\ttext-align: center;\n\tbackground-color: var(--alternate-bg-color);\n\tcolor: var(--alternate-color);\n}\n\nhr {\n\tmargin: 5px;\n}\n\n#titlepage {\n\tcolor: var(--main-bg-color);\n}\n\np.title {\n\ttext-align: center;\n}\n\n/* Styles for cover.xhtml */\nbody.cover {\n\tmargin: 0;\n\tpadding: 0;\n\ttext-align: center;\n}\n\np.cover {\n\tmargin: 0;\n\tpadding: 0;\n\ttext-align: center;\n}\n\nimg.cover {\n\theight: 100%;\n\tmargin: 0;\n\tpadding: 0;\n}\n\nhtml.eob {\n\tmargin: 0;\n\tpadding: margin;\n\ttext-align: center;\n}\n\nbody.eob {\n\t/* margin-left: auto; */\n\t/* margin-right: auto; */\n\tpadding: 0;\n\t/* text-align: center; */\n\tbackground-color: var(--main-bg-color);\n}\n\nh2.eob {\n\tdisplay: block;\n\tmargin-left: auto;\n\tmargin-right: auto;\n\tpadding-top: 30px;\n\ttext-align: center;\n\tcolor: rgba(0, 0, 0, 0);\n}\n\nh3.eob {\n\tmargin-left: auto;\n\tmargin-right: auto;\n\tpadding: 0;\n\ttext-align: center;\n\tcolor: var(--main-color)\n}\n\npicture.eob {\n\tmargin: 0;\n\tpadding: 0;\n\ttext-align: center;\n}\n\nfigure.eob {\n\tdisplay: block;\n\tmargin-left: auto;\n\tmargin-right: auto;\n}\n\np.eob {\n\tmargin: 0;\n\tpadding-bottom: 40px;\n\ttext-align: center;\n\tcolor: rgba(0, 0, 0, 0);\n\tfont-family: \"Urbanist-Thin\", \"Lemon/Milk\", \"Myriad Pro\", helvetica, sans-serif;\n}\n\np.eob-thin {\n\tdisplay: block;\n\ttext-align: center;\n\tfont-family: Urbanist-Thin;\n\tmargin-left: 0;\n\tmargin-right: auto;\n}\n\nimg.eob {\n\twidth: 100%;\n\tmax-height: 200px;\n\tmargin: 0;\n\tpadding: 0;\n}\n\nh1.titlepage {\n\tmargin-left: auto;\n\tmargin-right: auto;\n\ttext-align: center;\n\tcolor: var(--main-color)\n}\n\nh3.titlepage {\n\tmargin-left: auto;\n\tmargin-right: auto;\n\ttext-align: center;\n\tcolor: var(--main-color)\n}\n\nfigure.titlepage-gem {\n\twidth: 120px;\n\theight: 60px;\n\tmargin-left: auto;\n\tmargin-right: auto;\n\ttext-align: center;\n}"
        }
    ]

def test_css():
    """test printing css from setup_files.py"""
    for file in FILES:
        if file["file"] == "style.css":
            content = file["content"]
            filepath = file["filepath"]
            with open (filepath, "w") as outfile:
                outfile.write(content)



def make_files() -> None:
    """Creates the necessary files for logging."""
    # Create directories
    for directory in DIRS:
        if not directory.exists():
            directory.mkdir()

    for file in FILES:
        path = file["path"]
        if not Path(path).exists():
            file_type = file["type"]
            content = file["content"]
            match file_type:
                case "json":
                    with open(path, "w") as outfile:
                        json.dump(file[content], outfile, indent=4)
            filename = file["file"]
