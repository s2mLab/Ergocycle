import time
import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets

DURATION_INT = 5


class TimerWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.time_left_int = DURATION_INT
        self.widget_counter_int = 0

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        vbox = QtWidgets.QVBoxLayout()
        central_widget.setLayout(vbox)

        #self.pages_qsw = QtWidgets.QStackedWidget()
        #vbox.addWidget(self.pages_qsw)
        self.time_passed_qll = QtWidgets.QLabel()
        vbox.addWidget(self.time_passed_qll)

        #self.widget_one = QtWidgets.QLabel("This is widget one")
        #self.pages_qsw.addWidget(self.widget_one)
        #self.widget_two = QtWidgets.QLabel("This is widget two")
        #self.pages_qsw.addWidget(self.widget_two)
        #self.widget_three = QtWidgets.QLabel("This is widget three")
        #self.pages_qsw.addWidget(self.widget_three)
        #self.widget_four = QtWidgets.QLabel("This is widget four")
        #self.pages_qsw.addWidget(self.widget_four)

        self.timer_start()
        self.update_gui()

    def timer_start(self):
        self.time_left_int = 60*(DURATION_INT)

        self.my_qtimer = QtCore.QTimer(self)
        self.my_qtimer.timeout.connect(self.timer_timeout)
        self.my_qtimer.start(1000)
        self.update_gui()

    def timer_timeout(self):
        self.time_left_int -= 1

        if self.time_left_int == 0:
            self.close()
            #self.widget_counter_int = (self.widget_counter_int + 1) % 4
            #self.pages_qsw.setCurrentIndex(self.widget_counter_int)
            #self.time_left_int = DURATION_INT

        self.update_gui()

    def update_gui(self):
        self.time_passed_qll.setText(str(self.time_left_int))


app = QtWidgets.QApplication(sys.argv)
main_window = TimerWindow()
main_window.show()
sys.exit(app.exec_())
#t=2
#t_sec = 60*(t)
#while t_sec :
    #min = t_sec//60
    #sec = t_sec % 60
    #t_layout = '{:02d}:{:02d}'.format(min, sec)
    #print(t_layout)
    #time.sleep(1)
    #t_sec -= 1
#print("done")
