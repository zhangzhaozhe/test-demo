# 0. 导入需要的包和模块
from PyQt5 import QtGui
from PyQt5.Qt import *
import sys
"""
事件对象没处理，就会往父对象的事件中去传
"""

class Window(QWidget):
    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        print('顶层窗口的鼠标按下')


class MidWindow(QWidget):
    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        print('中间控件被按下')


class Label(QLabel):
    # pass
    def mousePressEvent(self, evt) -> None:
        print('标签控件鼠标按下')
        evt.accept()
        print(evt.isAccepted())
        # evt.ignore()

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = Window()
# 2.1 控件设置
window.setWindowTitle("事件转发")
window.resize(500, 500)

mid_window = MidWindow(window)
mid_window.resize(300, 300)
mid_window.setAttribute(Qt.WA_StyledBackground, True)
mid_window.setStyleSheet("background-color: yellow;")

label = Label(mid_window)
label.setText('这是一个标签')
label.setStyleSheet('background-color: red;')
label.move(100, 100)

# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec())



