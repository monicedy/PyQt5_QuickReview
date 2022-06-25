from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
class MyMainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # 状态栏是由QMainWindow创建的。
        self.statusBar().showMessage('Ready')
        
        ## 
        # QAction.setStatusTip('Exit application')

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')  
        self.show()
       

if __name__ == "__main__":
    # 创建主程序
    app  = QApplication(sys.argv)
    
    # 创建GUI
    window = MyMainWin()
    
    # 运行app.exec_()
    sys.exit(app.exec_())