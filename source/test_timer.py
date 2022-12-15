import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from datetime import datetime

DURATION_INT = 5


class TimerWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.my_qtimer = None

        self.time_left_int = DURATION_INT
        self.widget_counter_int = 0

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        vbox = QtWidgets.QVBoxLayout()
        central_widget.setLayout(vbox)

        # self.pages_qsw = QtWidgets.QStackedWidget()
        # vbox.addWidget(self.pages_qsw)
        self.time_passed_qll = QtWidgets.QLabel()
        vbox.addWidget(self.time_passed_qll)

        self.timer_start()
        self.update_gui()

    def timer_start(self):
        self.time_left_int = 60 * DURATION_INT - 1

        self.my_qtimer = QtCore.QTimer(self)
        self.my_qtimer.timeout.connect(self.timer_timeout)
        self.my_qtimer.start(1000)
        self.timer_timeout()
        self.update_gui()

    def timer_timeout(self):
        # get time
        time = datetime.now()
        formatted_time = time.strftime("%I:%M:%S")
        self.time_passed_qll.setDigitCount(12)
        self.time_passed_qll.display(formatted_time)

        self.update_gui()

    def update_gui(self):
        self.time_passed_qll.setText(str(self.time_left_int))


app = QtWidgets.QApplication(sys.argv)
main_window = TimerWindow()
main_window.show()
sys.exit(app.exec_())
