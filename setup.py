from cx_Freeze import setup, Executable
import sys

buildOptions = dict(packages=[], excludes=[])


base = None
if sys.platform == "win32":
    base = "Win32GUI"

exe = [Executable("make_GUI.py", base=base)]

setup(
    name='MGRS',
    version='0.1',
    author="hyunmook",
    description="made by hyunmook, in 2021",
    options=dict(build_exe=buildOptions),
    executables=exe
)
