from PyQt6 import uic

# Convert the .ui file to a .py file
ui_file = ".\\PyQT6_Exercises\\01_HelloWorld\\HelloWorld.ui"
py_file = ".\\PyQT6_Exercises\\02_ui_to_py_vscode\\HelloWorld_UI.py"

uic.ui_to_py(ui_file, py_file)