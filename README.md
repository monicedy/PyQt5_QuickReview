## 重启pyqt5目的与意义
- 构建一个标准流程
- 方便下次直接上手

## 目录
- 1.模块功能
- 2.常用控件
- 3.布局
- 4.信号与槽

#### 1.模块功能 QtWidgets, QtCore, QtGui
- QtWidgets 包含了一系列创建桌面应用的UI元素。
- QtGui 包含了窗口系统、事件处理、2D图像、基本绘画、字体和文字类。
- QtCore 包含了核心的非GUI的功能。主要和时间、文件与文件夹、各种数据、流、URLs、mime类文件、进程与线程一起使用。

#### 2.常用控件
- [x] 2.0标签 (QLabel)
- [x] 2.1按钮 (QPushButton)
- [x] 2.2输入框 (QLineEdit, QInputDialog)
- [x] 2.3单选多选项 (QCheckBox, QComboBox)
- [x] 2.4消息弹窗 (`QMessageBox().question(self,tit,text,OK|NO,DF)`)

<!-- 
###### 2.1按钮

###### 2.2输入框(单行多行)

###### 2.3单选多选项

###### 2.4消息弹窗 -->

#### 3.布局
#### 3.1 盒布局
使用盒布局能让程序具有更强的适应性。这个才是布局一个应用的更合适的方式。QHBoxLayout和QVBoxLayout是基本的布局类，分别是水平布局和垂直布局。
如果我们需要把两个按钮放在程序的右下角，创建这样的布局，我们只需要一个水平布局加一个垂直布局的盒子就可以了。再用弹性布局增加一点间隙。
```
    # [] | OK | NO
    hbox = QHBoxLayout()
    hbox.addStretch(1)
    hbox.addWidget(okButton)
    hbox.addWidget(cancelButton)
    
    #   []
    #   ———
    #   hbox
    vbox = QVBoxLayout()
    vbox.addStretch(1)
    vbox.addLayout(hbox)

    self.setLayout(vbox) 
```

#### 3.2 栅布局

```
    grid = QGridLayout()
    grid.setSpacing(10)

    grid.addWidget(obj, 3, 1, 5, 1)
    第n列(h)，第n行(w)，跨度行(h)，跨度列(w)

    self.setLayout(grid)

    可以弹性拉伸
        # 亲测：横向可以调整（即多占即列，拉伸宽度
        # 位置都是相对的, 多退少不补
        # (少分配了位置会重叠)
        # 多分配了会自动调整
```

#### 4.信号与槽 signal slot （事件监听）
- 绑定模板 `obj.signal.connect(slot)`
    - connect: 使用connect()将信号连接到槽
    - disconnect: 使用disconnect()销毁连接

