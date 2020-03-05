# Using OOP classes to compose more functionality into GUI
# Added toggle functionality to b1 to switch between label text
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):  # class "MyWindow" inherits from QMainWindow

    # Constructor: created an init method that will run whenever an instance of MyWindow is created
    # super is calling the parent constructor so everything gets set up properly
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)  # set size of window
        self.setWindowTitle("Creating GUI with classes :)")  # set title of window
        self.flag = 1  # flag used to toggle pushButton
        self.initUI()

    def initUI(self):
        # Adding Widgets to the MyWindow class
        self.label = QtWidgets.QLabel(self)  # MyWindow inherits QMainWindow t/f self.label is the correct instance
        self.label.setText("WRC Rules!")
        self.label.move(110, 150)  # where top left corner will appear in main window

        # syntax for creating new widget:
        # "widget name" = QtWidgets."WidgetType"(place to be embedded)
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("click MEE")
        self.b1.clicked.connect(self.clicked)  # connecting a widget to a method

    def clicked(self):
        if self.flag:
            self.label.setText("U Pressed MEE!")
            self.update()
            self.flag = 0
        else:
            self.label.setText("WRC Rules!")
            self.update()
            self.flag = 1

    def update(self):   # method automatically adjusts the size of the label depending on text
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)  # config setup for application depending on OS
    win = MyWindow()  # win is now an instance of the class created above!
    win.show()  # actually show the window on the user screen
    sys.exit(app.exec())  # make sure the window shows up and has a "clean exit"


window()
