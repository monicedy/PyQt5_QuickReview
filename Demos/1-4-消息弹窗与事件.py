'''
    事件传递系统在PyQt5内建的single和slot机制里面。
    点击按钮之后, 信号会被捕捉并给出既定的反应。
'''
from PyQt5.QtWidgets import QMessageBox

from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initMainUI()
        
    def initMainUI(self):
        # 初始化窗口参数
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('logo.png'))
        
        # 初始化其他控件
        self.initTooltip()        
        self.initBtn()
        
        # 显示Qwidget
        self.show()
        
    def initTooltip(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        
    def initBtn(self):
        # 继承自父组件
        btn = QPushButton('exit', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        
        # 绑定事件
        btn.clicked.connect(QCoreApplication.instance().quit)
        
        # 调整尺寸和位置
        btn.resize(btn.sizeHint())
        btn.move(50, 50)  
        
        
    def closeEvent(self, event):
        # 父类，标题，内容
        # 选项，默认选项
        msgBox = QMessageBox().question(self,"msgbox","this is content",
                                        QMessageBox.Yes|QMessageBox.No, 
                                        QMessageBox.Yes)
        if msgBox == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore() 
        

if __name__ == "__main__":
    # 创建主程序
    app  = QApplication(sys.argv)
    
    # 创建GUI
    window = MyWindow()
    
    # 运行app.exec_()
    sys.exit(app.exec_())