'''
    分别按下1, 2两个按键
    控制台会输出各自的响应
'''

# 信号与槽
from PyQt5.QtCore import pyqtSignal, QObject, Qt

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
    
class Mysigs(QObject):
    # Communicate类创建了一个pyqtSignal()属性的信号。
    sig1 = pyqtSignal() 
    sig2 = pyqtSignal() 

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):      
        # 创建全局的MySigs类, 内含多个信号
        self.mySigs = Mysigs()
        
        # 绑定自定义事件(自定义类QObject的pyqtSignal sig1) 
        # 到 槽dosth1
        self.mySigs.sig1.connect(self.doSth1)
        
        ## 通俗理解：dosth2监听sig2
        self.mySigs.sig2.connect(self.doSth2)      

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()

    # signal
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_1:
            # 发送事件
            self.mySigs.sig1.emit()
        if e.key() == Qt.Key_2:
            self.mySigs.sig2.emit()

    # slot
    def doSth1(self):
        print("sign1 something happend")
        
    def doSth2(self):
        print("sign2 something happend")


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


"""
1、QObject类是所有Qt对象的基类。

2、QObject是Qt对象模型的核心。该模型的核心特性是一种非常强大的无缝对象通信机制,称为信号和槽。
可以使用connect()将信号连接到槽,并使用disconnect()销毁连接。为了避免永无止境的通知循环,可以使用blockSignals()临时阻止信号。
受保护的函数connectNotify()和disconnectNotify()使跟踪连接成为可能。

......

————————————————
版权声明:本文为CSDN博主「beibeix2015」的原创文章,遵循CC 4.0 BY-SA版权协议,转载请附上原文出处链接及本声明。
原文链接:https://blog.csdn.net/beibeix2015/article/details/114868764
"""