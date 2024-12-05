# **Add custom function to PyQT6.uic**

> Author: Lê Minh Nguyên

Since VSCode doesn't have External Tool function of PyCharm. I have modified the code of the PyQT6 library to have this extra function. This allowed the user to have this custom function inside of the code file.

> [!NOTE]
> PyQT6.uic already have the function compileUI() that do that task, But I will add a extra function to make it easier to execute and remember._ 


Since I use a virtual environment, I will modified PyQT6 code of this virtual environment only. But this can be done easily with the main Python aswell

1. Navigate to ```.venv\Lib\site-packages\PyQt6\uic\compile_ui.py``` 

2. Add this functions to the end of the file and save the file.

``` py
def ui_to_py(ui_file, py_file):
    try:    
        with open(py_file, 'w') as fout:
            compileUi(ui_file, fout)
    except:
        print(f"Error converting {ui_file} to {py_file}\n Check file path or try PyQt6.uic.pyuic 'ui_file.ui' -o 'py_file.py'")
```

3. Modify the ```__init__.py``` in the same directory to have the new function

``` py
from .compile_ui import compileUi, compileUiDir
```
to

``` py
from .compile_ui import compileUi, compileUiDir, ui_to_py
``` 

4. Save the files and now you can use the function ```ui_to_py('ui_file.ui', 'py_file.py')``` to convert the ui file to python file. 

## Example

``` py
from PyQt6.uic import ui_to_py

ui_to_py('ui_file.ui', 'py_file.py')
```


