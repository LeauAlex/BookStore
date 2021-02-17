from cx_Freeze import setup, Executable

exe = Executable( script=r"frontend.py",base="Win32GUI")

setup( name = "BookStore", version = "0.1",description = "An example",executables = [exe])