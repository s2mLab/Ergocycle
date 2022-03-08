import sys
import math

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

res_x = 1366.0 # in pixels
res_y = 768.0 # in pixels
monitor_size = 14.0 #in inches

res_diag = math.sqrt(math.pow(res_x, 2) + math.pow(res_y, 2))
monitor_size_x =  monitor_size * res_x / res_diag
monitor_size_y =  monitor_size * res_y / res_diag


screen_res_x = 1920.0 # in pixels
screen_res_y = 1080.0 # in pixels
screen_size = 7.0 #in inches

screen_res_diag = math.sqrt(math.pow(screen_res_x, 2) + math.pow(screen_res_y, 2))
screen_size_x =  screen_size * screen_res_x / screen_res_diag
screen_size_y =  screen_size * screen_res_y / screen_res_diag

width = round(res_x * screen_size_x / monitor_size_x) #in pixels
height = round(res_y * screen_size_y / monitor_size_y) #in pixels

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle('QHBoxLayout')

window.setFixedWidth(width)

window.setFixedHeight(height)

layout = QHBoxLayout()

layout.addWidget(QPushButton('Left'))

layout.addWidget(QPushButton('Center'))

layout.addWidget(QPushButton('Right'))

window.setLayout(layout)

window.show()

sys.exit(app.exec_())
