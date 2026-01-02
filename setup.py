"""
Setup script for creating Windows executable for Ses Kayıt Edici
"""
import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": [],
    "include_files": [],
    "excludes": ["unittest"],
}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="SesKayitEdici",
    version="1.0.0",
    description="Basit bir Windows ses kayıt edici programı",
    author="integrumart",
    options={"build_exe": build_exe_options},
    executables=[
        Executable(
            "seskayit.py",
            base=base,
            target_name="SesKayitEdici.exe",
            icon=None
        )
    ],
)
