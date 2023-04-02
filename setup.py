"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from pathlib import Path

from setuptools import setup
import tkinter as tk
import shutil
import os

APP = ['main.py']
DATA_FILES = ['resources']
OPTIONS = {
    'iconfile': 'resources/icon.icns',
    'plist': {
        'CFBundleName': 'SD Prompt Reader',
        'CFBundleDisplayName': 'SD Prompt Reader',
        'CFBundleVersion': '1.1.0 beta',
        'CFBundleIdentifier': 'com.receyuki.sd-prompt-reader',
        'NSHumanReadableCopyright': 'Copyright © 2023 receyuki All rights reserved.',
    },
    'includes': ['pyperclip', 'PIL', 'tkinter', 'tkinterdnd2', 'os', 'customtkinter', 'plyer', 'pyobjus',
                 'plyer.platforms.macosx.notification', 'tcl8', 'tcl8.6']
}

setup(
    name='SD Prompt Reader',
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

root = tk.Tk()
root.overrideredirect(True)
root.withdraw()
tcl_dir = Path(root.tk.exprstring('$tcl_library'))
tk_dir = Path(root.tk.exprstring('$tk_library'))
root.destroy()

os.makedirs("./dist/SD Prompt Reader.app/Contents/lib", exist_ok=True)
print(f"Copying TK from: {tk_dir}")
shutil.copytree(tk_dir, f"./dist/SD Prompt Reader.app/Contents/lib/{tk_dir.parts[-1]}")
print(f"Copying TCL from: {tcl_dir}")
shutil.copytree(tcl_dir, f"./dist/SD Prompt Reader.app/Contents/lib/{tcl_dir.parts[-1]}")