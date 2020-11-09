import sys
import os

from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["os"],
    "excludes": ["tkinter"],
    "includes": "pygame,pygame_gui",
    "include_files": ["images/", "sounds/", "fonts/"],
    "zip_includes": [("src/",".")],
    "zip_include_packages": ["*"],
    "zip_exclude_packages": []
}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "catapult_moonshot",
        version = "0.1",
        description = "Catapult Moonshot!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("main.py", base=base, targetName="catapult_moonshot.exe", icon="images/icon.ico")])
