from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

# connecting a function to a button

def clicked():
    print("clicked")


def window():
    app = QApplication(sys.argv)  # config setup for application depending on OS
    win = QMainWindow()
    xpos = 200  # starting position of window
    ypos = 200  # coordinates (0,0) are at top left part of the screen
    width = 300
    height = 300
    win.setGeometry(xpos, ypos, width, height)  # set size of window
    win.setWindowTitle("Beginning GUI")  # set title of window

    # Adding Widget to the created window
    label = QtWidgets.QLabel(win)  # label is a QLabel & is set inside the win (MainWindow)
    label.setText("WRC Rules!")
    label.move(110, 150)  # where top left corner will appear in main window

    # syntax for creating new widget:
    # "widget name" = QtWidgets."WidgetType"(place to be embedded)
    b1 = QtWidgets.QPushButton(win)
    b1.setText("click MEE")
    b1.clicked.connect(clicked)  # connecting a widget to function

    win.show()  # actually show the window on the user screen
    sys.exit(app.exec())  # make sure the window shows up and has a "clean exit"


window()
