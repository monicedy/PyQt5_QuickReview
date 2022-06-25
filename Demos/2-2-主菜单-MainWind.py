from PyQt5.QtWidgets import QAction, qApp

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
import sys
class MyMainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # 状态栏是由QMainWindow创建的。
        self.statusBar().showMessage('Ready')
        
        self.initMenu()

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')  
        self.show()
        
    def initMenu(self):
        
        exitAct = QAction(QIcon('logo.png'), '&Exit', self)        
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        
        # 当执行这个指定的动作时，就触发了一个事件。这个事件跟QApplication的quit()行为相关联，所以这个动作就能终止这个应用。
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        

if __name__ == "__main__":
    # 创建主程序
    app  = QApplication(sys.argv)
    
    # 创建GUI
    window = MyMainWin()
    
    # 运行app.exec_()
    sys.exit(app.exec_())