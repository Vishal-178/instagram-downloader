import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\ProgramData\Anaconda3\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\ProgramData\Anaconda3\tcl\tk8.6"

executables = [cx_Freeze.Executable("instasave.py", base=base)]
cx_Freeze.setup(
    name = "InstaSave",
    options = {"build_exe": {"packages":["tkinter","os","requests","bs4"], "include_files":['tcl86t.dll','tk86t.dll']}},
    version = "0.01",
    description = "Tkinter Application",
    executables = executables
    )