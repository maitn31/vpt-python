# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'daily.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(722, 311)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(310, 230, 75, 23))
        self.startBtn.setObjectName("startBtn")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 170, 211, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.trangvienbox = QtWidgets.QCheckBox(self.layoutWidget)
        self.trangvienbox.setObjectName("trangvienbox")
        self.horizontalLayout_3.addWidget(self.trangvienbox)
        self.nguyenlieubox = QtWidgets.QComboBox(self.layoutWidget)
        self.nguyenlieubox.setObjectName("nguyenlieubox")
        self.horizontalLayout_3.addWidget(self.nguyenlieubox)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 140, 376, 19))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nhanvipbox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.nhanvipbox.setObjectName("nhanvipbox")
        self.horizontalLayout.addWidget(self.nhanvipbox)
        self.hanhlangbox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.hanhlangbox.setObjectName("hanhlangbox")
        self.horizontalLayout.addWidget(self.hanhlangbox)
        self.pbbox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.pbbox.setObjectName("pbbox")
        self.horizontalLayout.addWidget(self.pbbox)
        self.thantubox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.thantubox.setObjectName("thantubox")
        self.horizontalLayout.addWidget(self.thantubox)
        self.tuhanhbox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.tuhanhbox.setObjectName("tuhanhbox")
        self.horizontalLayout.addWidget(self.tuhanhbox)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 200, 291, 22))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tinhcungbox = QtWidgets.QCheckBox(self.layoutWidget2)
        self.tinhcungbox.setObjectName("tinhcungbox")
        self.horizontalLayout_2.addWidget(self.tinhcungbox)
        self.loaitinhcungbox = QtWidgets.QComboBox(self.layoutWidget2)
        self.loaitinhcungbox.setObjectName("loaitinhcungbox")
        self.horizontalLayout_2.addWidget(self.loaitinhcungbox)
        self.leveltinhcungbox = QtWidgets.QComboBox(self.layoutWidget2)
        self.leveltinhcungbox.setObjectName("leveltinhcungbox")
        self.horizontalLayout_2.addWidget(self.leveltinhcungbox)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(480, 30, 231, 271))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.statusTextBox = QtWidgets.QTextEdit(self.layoutWidget3)
        self.statusTextBox.setReadOnly(True)
        self.statusTextBox.setObjectName("statusTextBox")
        self.verticalLayout.addWidget(self.statusTextBox)
        self.charlocBox = QtWidgets.QComboBox(self.centralwidget)
        self.charlocBox.setGeometry(QtCore.QRect(250, 110, 69, 20))
        self.charlocBox.setObjectName("charlocBox")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 110, 241, 16))
        self.label_5.setObjectName("label_5")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 60, 481, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget4.setGeometry(QtCore.QRect(30, 80, 113, 22))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.svCombo = QtWidgets.QComboBox(self.layoutWidget4)
        self.svCombo.setObjectName("svCombo")
        self.horizontalLayout_4.addWidget(self.svCombo)
        self.layoutWidget5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget5.setGeometry(QtCore.QRect(150, 80, 192, 22))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget5)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.kenhBox = QtWidgets.QComboBox(self.layoutWidget5)
        self.kenhBox.setObjectName("kenhBox")
        self.horizontalLayout_5.addWidget(self.kenhBox)
        self.logacc_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.logacc_checkBox.setGeometry(QtCore.QRect(370, 80, 70, 17))
        self.logacc_checkBox.setObjectName("logacc_checkBox")
        self.stopBtn = QtWidgets.QPushButton(self.centralwidget)
        self.stopBtn.setGeometry(QtCore.QRect(390, 230, 75, 23))
        self.stopBtn.setObjectName("stopBtn")
        self.accCombo = QtWidgets.QComboBox(self.centralwidget)
        self.accCombo.setGeometry(QtCore.QRect(20, 40, 209, 20))
        self.accCombo.setObjectName("accCombo")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "auto daily"))
        self.startBtn.setText(_translate("MainWindow", "start"))
        self.trangvienbox.setText(_translate("MainWindow", "trang viên"))
        self.nhanvipbox.setText(_translate("MainWindow", "nhận vip"))
        self.hanhlangbox.setText(_translate("MainWindow", "hành lang"))
        self.pbbox.setText(_translate("MainWindow", "phụ bản"))
        self.thantubox.setText(_translate("MainWindow", "thần tu"))
        self.tuhanhbox.setText(_translate("MainWindow", "tu hành"))
        self.tinhcungbox.setText(_translate("MainWindow", "tinh cung"))
        self.label_4.setText(_translate("MainWindow", "Status:"))
        self.label_5.setText(_translate("MainWindow", "vị trí nhân vật (lúc chọn nhân vật, mặc định 1):"))
        self.label_6.setText(_translate("MainWindow", "Server:"))
        self.label_3.setText(_translate("MainWindow", "Kênh(mặc địch kênh 5): "))
        self.logacc_checkBox.setText(_translate("MainWindow", "log acc"))
        self.stopBtn.setText(_translate("MainWindow", "Stop"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
