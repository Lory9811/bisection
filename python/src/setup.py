import sys
from cx_Freeze import setup, Executable

additional_modules = ['numpy.core._methods', 'numpy.lib.format']
setup(
    name = "Bisection Algorithm",
    version = "0.1",
    options = {'build_exe': {'includes': additional_modules}},
    executables = [Executable(script="bisection.py")]
)
