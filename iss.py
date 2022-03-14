# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'iss.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
import positionISS

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import qApp


class Ui_Form(object):
    def setupUi(self, Form):
        self.objISS = positionISS.Donnee_ISS()
        Form.setObjectName("Form")
        Form.resize(402, 135)
        Form.setMinimumSize(QtCore.QSize(402, 135))
        Form.setMaximumSize(QtCore.QSize(402, 135))
        Form.setWindowOpacity(1)
        self.btnFermer = QtWidgets.QPushButton(Form)
        self.btnFermer.setGeometry(QtCore.QRect(310, 100, 88, 34))
        self.btnFermer.setObjectName("btnFermer")
        self.btnFermer.clicked.connect(qApp.quit)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 401, 101))
        self.groupBox.setObjectName("groupBox")
        self.lLatitude = QtWidgets.QLabel(self.groupBox)
        self.lLatitude.setGeometry(QtCore.QRect(20, 30, 371, 31))
        self.lLatitude.setObjectName("lLatitude")
        self.lLongitude = QtWidgets.QLabel(self.groupBox)
        self.lLongitude.setGeometry(QtCore.QRect(20, 60, 371, 31))
        self.lLongitude.setObjectName("lLongitude")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Raffraichir la page
        # make QTimer
        self.qTimer = QtCore.QTimer()
        # set interval to 1 s
        self.qTimer.setInterval(1000)  # 1000 ms = 1 s
        # connect timeout signal to signal handler
        self.qTimer.timeout.connect(self.__affichePosition)
        # start timer
        self.qTimer.start()

    def __affichePosition(self):
        self.objISS.lectureDonnees()
        self.lLatitude.setText("Latitude: {}".format(self.objISS.latitude))
        self.lLongitude.setText("Longitude: {}".format(self.objISS.longitude))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ISS"))
        self.btnFermer.setText(_translate("Form", "Quitter"))
        self.groupBox.setTitle(_translate("Form", "Position"))
        self.lLatitude.setText(_translate("Form", "Latitude: "))
        self.lLongitude.setText(_translate("Form", "Longitude:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
