'''
    事件传递系统在PyQt5内建的single和slot机制里面。
    点击按钮之后, 信号会被捕捉并给出既定的反应。
    
    QCoreApplication包含了事件的主循环, 它能添加和删除所有的事件
        instance()创建了一个它的实例。
        QCoreApplication是在QApplication里创建的。 
    点击事件和能终止进程并退出应用的quit函数绑定在了一起。
    在发送者和接受者之间建立了通讯, 发送者就是按钮, 接受者就是应用对象。
'''
from PyQt5.QtCore import QCoreApplication

from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton
from PyQt5.QtGui import QIcon, QFont

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
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        
        # 绑定事件
        btn.clicked.connect(QCoreApplication.instance().quit)
        
        # 调整尺寸和位置
        btn.resize(btn.sizeHint())
        btn.move(50, 50)  
        

if __name__ == "__main__":
    # 创建主程序
    app  = QApplication(sys.argv)
    
    # 创建GUI
    window = MyWindow()
    
    # 运行app.exec_()
    sys.exit(app.exec_())