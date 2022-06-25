import sys
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QApplication, QComboBox, QCheckBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):     

        self.lbl = QLabel(self)
        self.lbl.move(0, 60)
        
        # 单行编辑框
        qle = QLineEdit(self)
        qle.textChanged[str].connect(self.onChanged)
        qle.move(0, 40) 
        
        # 其他复杂控件
        self.initCombox()
        self.checkBox()
        
        self.setGeometry(300, 300, 320, 240)
        self.setWindowTitle('QLineEdit')
        self.show()
        
    def checkBox(self):
        ckBox = QCheckBox('显示图片',self)
        ckBox.stateChanged.connect(self.changeCheckBox)
        ckBox.toggle() # 默认选中
        ckBox.move(0,20)
    
    def initCombox(self):
        combo = QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Gentoo")        
        combo.activated[str].connect(self.onActivated)          

    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()   
    
    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()  
        
    def changeCheckBox(self, state):
        if state == Qt.Checked:
            self.setPic()
        else:
            self.lbl.setText("取消选中")
            
    def setPic(self):
        """
        pixmap = QPixmap("redrock.png")
        创建一个QPixmap对象, 接收一个文件作为参数。
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        """
        pixmap = QPixmap("./ori/logo.png")
        self.lbl.setPixmap(pixmap) 
        self.lbl.adjustSize()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())