"""
    所有的应用都是事件驱动的。事件大部分都是由用户的行为产生的,
    当然也有其他的事件产生方式,比如网络的连接,窗口管理器或者定时器等。
    调用应用的exec_()方法时,应用会进入主循环,主循环会监听和分发事件。
    
    在事件模型中,有三个角色：
        事件源
        事件
        事件目标
    事件源就是发生了状态改变的对象。事件是这个对象状态改变的内容。
    事件目标是事件想作用的目标。事件源绑定事件处理函数,然后作用于事件目标身上。
    PyQt5处理事件方面有个signal and slot机制。Signals and slots用于对象间的通讯。
    
    事件触发的时候,发生一个signal,
    slot是用来被Python调用的(相当于一个句柄?就是相当于事件的绑定函数)slot只有在事件触发的时候才能调用。
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        grid = QGridLayout()
        grid.setSpacing(10)

        x = 0
        y = 0

        self.text = "x: {0},  y: {1}".format(x, y)

        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        # 事件追踪默认没有开启，当开启后才会追踪鼠标的点击事件。
        self.setMouseTracking(True)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()


    def mouseMoveEvent(self, e):
        '''
            【重写内置函数】鼠标移动事件
            e代表了事件对象。里面有我们触发事件(鼠标移动)的事件对象。
            x()和y()方法得到鼠标的x和y坐标点, 然后拼成字符串输出到QLabel组件里。
        '''

        x = e.x()
        y = e.y()

        text = "x: {0},  y: {1}".format(x, y)
        self.label.setText(text)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())