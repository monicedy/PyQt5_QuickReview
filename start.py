from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initMainUI()
        
    def initMainUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('logo.png'))
        
        self.show()
        

if __name__ == "__main__":
    app  = QApplication(sys.argv)
    
    window = MyWindow()
    
    sys.exit(app.exec_())