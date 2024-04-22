from cx_Freeze import setup, Executable
import sys
import os

# Determine Python installation directory
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
# Set TCL and TK library paths
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

base = None

# Check platform for executable base
if sys.platform == 'win32':
    base = None

# Define executables to be built
executables = [Executable("train.py", base=base)]

# Define required packages
packages = ["idna", "os", "sys", "cx_Freeze", "tkinter", "opencv-python-headless",
            "numpy", "Pillow", "pandas", "datetime", "time"]

# Define build options
options = {
    'build_exe': {
        'packages': packages,
    },
}

# Setup configuration
setup(
    name="ToolBox",
    options=options,
    version="0.0.1",
    description='Vision ToolBox',
    executables=executables
)
