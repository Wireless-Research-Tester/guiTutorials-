# -*- coding: utf-8 -*-
# Austin Langebeck-Fissinger
# Form implementation generated from reading ui file 'QPixmap.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.i = -1
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Photo = QtWidgets.QLabel(self.centralwidget)
        self.Photo.setGeometry(QtCore.QRect(125, 20, 450, 411))
        self.Photo.setText("")
        self.Photo.setPixmap(QtGui.QPixmap("3819.jpeg"))
        self.Photo.setScaledContents(True)
        self.Photo.setObjectName("Photo")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(250, 300, 100, 200))
        self.title.setText("Rapid Prototyping Process")
        self.title.adjustSize()
        self.title.setObjectName("Title")
        self.title.move(275, 500)
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(550, 480, 121, 51))
        self.pushButton_1.setObjectName("nextButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 480, 131, 51))
        self.pushButton_2.setObjectName("prevButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_1.clicked.connect(self.displayNext)
        self.pushButton_2.clicked.connect(self.displayPrev)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_1.setText(_translate("MainWindow", "NEXT >>"))

        self.pushButton_2.setText(_translate("MainWindow", "<< PREV"))

    def displayNext(self):
        if self.i >= 12 or self.i < 0:
            self.i = 0
            self.Photo.setPixmap(QtGui.QPixmap(temp_list[self.i]))
        else:
            self.i = self.i + 1
            self.Photo.setPixmap(QtGui.QPixmap(temp_list[self.i]))


    def displayPrev(self):
        if self.i <= 0 or self.i > 12:
            self.i = 12
            self.Photo.setPixmap(QtGui.QPixmap(temp_list[self.i]))
        else:
            self.i = self.i - 1
            self.Photo.setPixmap(QtGui.QPixmap(temp_list[self.i]))



if __name__ == "__main__":
    import sys

    # i = 0
    temp_list = ["1.png", "2.png", "3.png", "4.png", "5.png", "6.jpg", "7.png", "8.jpg", "9.png",
                 "10.png", "11.png", "12.png", "13.png"]
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
