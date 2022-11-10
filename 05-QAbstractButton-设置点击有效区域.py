# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.1 控件设置
window.setWindowTitle("抽象按钮-设置有效点击区域")
window.resize(500, 500)

#####################按钮模拟点击#####################

class Btn(QPushButton):

    def hitButton(self, point) -> bool:
        # print(point)
        # if point.x() > self.width() / 2:
        #     return True
        # return False
        # 确定圆心
        center_x = self.width() / 2
        center_y = self.height() / 2

        hit_x = point.x()
        hit_y = point.y()
        import math
        distance = math.sqrt(math.pow(hit_x-center_x, 2) + math.pow(hit_y-center_y, 2))
        if distance < self.width() / 2:
            return True
        return False

    def paintEvent(self, evt) -> None:
        super().paintEvent(evt)
        painter = QPainter(self)
        painter.setPen(QPen(QColor(100, 150, 200), 5))
        painter.drawEllipse(self.rect())


btn = Btn(window)
btn.move(100, 100)
btn.setText('点击')
btn.resize(200, 200)
btn.pressed.connect(lambda : print('按钮被按下了'))

btn.released.connect(lambda : print('按钮被释放了'))

btn.clicked.connect(lambda value : print('按钮被点击了', value))

btn.toggled.connect(lambda value: print('按钮选中状态发生了改变'))


#####################按钮模拟点击#####################


# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec())



