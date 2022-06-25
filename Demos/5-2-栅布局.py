"""
    可以弹性拉伸
        # 亲测：横向可以调整（即多占即列，拉伸宽度
        # 位置都是相对的, 多退少不补
        # (少分配了位置会重叠)
        # 多分配了会自动调整
"""

# 栅格布局
from PyQt5.QtWidgets import QGridLayout

import sys
from PyQt5.QtWidgets import (QWidget, QTextEdit,
    QPushButton, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                '4', '5', '6', '*',
                 '1', '2', '3', '-',
                '0', '.', '=', '+']

        positions = [(i,j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        #### 手动添加控件
        # 位置都是相对的, 多退少不补
        # (少分配了位置会重叠)
        # 多分配了会自动调整
        btnEnter1 = QTextEdit("enter",self)
        btnEnter2 = QPushButton("btn",self)
        grid.addWidget(btnEnter1,5,0,2,2)
        grid.addWidget(btnEnter2,7,0,1,2)

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()
        

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())