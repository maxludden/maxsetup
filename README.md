---
Title: README.md
Path: README.md
Author: Max Ludden
Date: 2022-11-22
CSS: static/style.css
...

# MaxSetup v0.3.0

## Purpose

This is a module that automates the file structure and settings of a new project.



## Installation

#### Install from Pip

```Python
pip install maxsetup
```

#### Install from Pipx

```Python
pipx install maxsetup
```


#### Install from Pipx

```Python
python add maxsetup
```


## Usage

<br />

All you need from `maxsetup` is the following:


```python
from maxsetup import setup

setup()
```

MaxSetup keeps track of the current run and logs all output to the console and to loguru sinks.

In addition it creates a file structure for the project that looks like this:

<pre style="background-color:#000000;border:1px solid white;border-radius: 2.5%">
<span style="color:cyan;">.</span>
<span style="color:white;">├── .env</span>
<span style="color:white;">├──</span> <span style="color:grey;">.gitignore</span>
<span style="color:white;">├──</span> <span style="color:#0F7473;">.vscode</span>
<span style="color:white;">│   ├──</span> <span style="color:gold;">launch.json</span>
<span style="color:white;">│   ├──</span> <span style="color:gold;">settings.json</span>
<span style="color:white;">│   └──</span> <span style="color:gold;">tasks.json</span>
<span style="color:white;">├──</span> <span style="color:yellow;">LICENSE</span>
<span style="color:white;">├──</span> <span style="color:#0F7473;">logs</span>
<span style="color:white;">│   ├──</span> <span style="color:#00ff00;">log.log</span>
<span style="color:white;">│   ├── run.txt</span>>
<span style="color:white;">│   └──</span> <span style="color:#00ff00;">verbose.log</span>
<span style="color:white;">└──</span> <span style="color:#0F7473;">static</span>
    <span style="color:white;">├──</span> <span style="color:orange;">Century Gothic Bold.ttf</span>
    <span style="color:white;">├──</span> <span style="color:orange;">Century Gothic.ttf</span>
    <span style="color:white;">├──</span> <span style="color:orange;">MesloLGS NF Bold Italic.ttf</span>
    <span style="color:white;">├──</span> <span style="color:orange;">MesloLGS NF Bold.ttf</span>
    <span style="color:white;">├──</span> <span style="color:orange;">MesloLGS NF Italic.ttf</span>
    <span style="color:white;">├──</span> <span style="color:orange;">MesloLGS NF Regular.ttf</span>
    <span style="color:white;">├──</span> <span style="color:orange;">Urbanist-Black.ttf</span>
    <span style="color:white;">├──</span> <span style="color:orange;">Urbanist-BlackItalic.ttf</span>
    <span style="color:white;">├──</span> <span style="color:orange;">Urbanist-Italic.ttf</span>
    <span style="color:white;">├──</span> <span style="color:orange;">Urbanist-Light.ttf</span>
    <span style="color:white;">├──</span> <span style="color:orange;">Urbanist-LightItalic.ttf</span>
    <span style="color:white;">├──</span> <span style="color:orange;">Urbanist-Regular.ttf</span>
    <span style="color:white;">├──</span> <span style="color:orange;">White Modesty.ttf</span>
    <span style="color:white;">└──</span> <span style="color:magenta">style.css
</pre>