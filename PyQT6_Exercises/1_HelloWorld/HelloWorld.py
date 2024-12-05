from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

Form, Window = uic.loadUiType(".\\PyQT6_Exercises\\1_HelloWorld\\HelloWorld.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec()