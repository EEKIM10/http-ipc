"""
This script just sets up the server.
"""
import sys
import os
import subprocess
from pathlib import Path

HOME = Path(__file__).parent
os.chdir(HOME)

PYTHON_EXEC = Path(sys.executable).resolve()
PIP_EXEC = None

if not (HOME / "venv"):
    print("Creating a virtual environment...")
    try:
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
    except subprocess.CalledProcessError as e:
        print("Failed to create a virtual environment - exit code %s." % e.returncode)
        sys.exit(e.returncode)

if os.name == "nt":
    PYTHON_EXEC = (HOME / "venv" / "Scripts" / "python").resolve()
    PIP_EXEC = (HOME / "venv" / "Scripts" / "pip").resolve()
else:
    PYTHON_EXEC = (HOME / "venv" / "bin" / "python3").resolve()
    PIP_EXEC = (HOME / "venv" / "bin" / "pip3").resolve()
assert PYTHON_EXEC.exists() is True
assert PIP_EXEC.exists() is True

print("Installing & Updating dependencies...")
try:
    subprocess.run([PIP_EXEC, "install", "-Ur", str(HOME / "requirements.txt").resolve()], check=True)
except subprocess.CalledProcessError as e:
    print("Failed to install dependencies - exit code %s." % e.returncode)
    sys.exit(e.returncode)
