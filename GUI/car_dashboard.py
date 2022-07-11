import sys
from PySide6 import QtWidgets
from UI import Ui_CarDashBoard

class MainWindow(QtWidgets.QMainWindow, Ui_CarDashBoard):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()