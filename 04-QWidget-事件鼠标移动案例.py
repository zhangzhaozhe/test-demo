# 0. 导入需要的包和模块
from PyQt5 import QtGui
from PyQt5.Qt import *


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("窗口移动的学习")
        self.resize(500, 500)
        self.setup_ui()
        self.move_flag = False

    def setup_ui(self):
        pass

    def mousePressEvent(self, evt) -> None:
        if evt.button() == Qt.LeftButton:
            self.move_flag = True
            # a0: QtGui.QMouseEvent
            # print('鼠标按下')
            # 确定两个点(鼠标第一次按下的点，窗口当前所在的原始点)
            self.mouse_x = evt.globalX()
            self.mouse_y = evt.globalY()
            print(self.mouse_x, self.mouse_y)

            self.origin_x = self.x()
            self.origin_y = self.y()

    def mouseMoveEvent(self, evt) -> None:
        if self.move_flag:
            print(evt.globalX(), evt.globalY())
            # 计算的是移动量
            move_x = evt.globalX() - self.mouse_x
            move_y = evt.globalY() - self.mouse_y

            dest_x = self.origin_x + move_x
            dest_y = self.origin_y + move_y
            self.move(dest_x, dest_y)


    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        print('鼠标释放')
        self.move_flag = False



if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    window.setMouseTracking(True)

    sys.exit(app.exec())



