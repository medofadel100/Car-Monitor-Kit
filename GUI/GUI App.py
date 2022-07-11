import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from UI import Ui_CarDashBoard

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_CarDashBoard()
        self.ui.setupUi(self)
        
if __name__ == '__main__':
    app = QApplication(sys.argv) 
    window = MainWindow()
    window.show()
    
    
    sys.exit(app.exec_())