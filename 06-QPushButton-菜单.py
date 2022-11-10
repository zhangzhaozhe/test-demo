# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.1 控件设置
window.setWindowTitle("菜单API")
window.resize(500, 500)

btn = QPushButton(window)
btn.setText('xxx')
btn.setIcon(QIcon('xxx.png'))


# ####################菜单的设置#####################

menu = QMenu()
# 子菜单 最近打开
open_recent_menu = QMenu(menu)
open_recent_menu.setTitle('最近打开')

file_action = QAction('Python-GUI', open_recent_menu)
open_recent_menu.addAction(file_action)

# 行为动作 新建 打开 分割线 退出
# new_action = QAction()
# new_action.setText('新建')
# new_action.setIcon(QIcon('xxx.png'))
new_action = QAction(QIcon('xxx.png'), '新建', menu)
new_action.triggered.connect(lambda : print("新建文件"))

open_action = QAction(QIcon('xxx.png'), '打开', menu)
open_action.triggered.connect(lambda : print('打开文件'))

close_action = QAction('退出', menu)
close_action.triggered.connect(lambda : print('退出程序'))

menu.addAction(new_action)
menu.addAction(open_action)
menu.addMenu(open_recent_menu)
menu.addSeparator()
menu.addAction(close_action)

btn.setMenu(menu) 

# ####################菜单的设置#####################



# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec())



