import subprocess
import sys
import platform
from pathlib import Path
import bpy

# https://blender.stackexchange.com/a/238995
py_exec = str(sys.executable)
lib = Path(py_exec).parent.parent / "lib"
plat=platform.system()

if plat in ['Linux' 'Darwin']:
    subprocess.call([py_exec, "-m", "ensurepip", "--user" ])
    subprocess.call([py_exec, "-m", "pip", "install", "--upgrade", "pip" ])
    subprocess.call([py_exec,"-m", "pip", "install", f"--target={str(lib)}", "PIL"])
elif plat == 'Windows':
    with open (bpy.path.abspath("//install_PIL.ps1"),'wt') as f:
        f.write("# Please run this file in administrator mode\n")
        f.write(f"'cd {sys.exec_prefix}\\bin'\n")
        f.write("./python -m pip install PIL")