# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_g_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChangeGWindow(object):
    def setupUi(self, ChangeGWindow):
        ChangeGWindow.setObjectName("ChangeGWindow")
        ChangeGWindow.resize(450, 600)
        ChangeGWindow.setMinimumSize(QtCore.QSize(450, 600))
        ChangeGWindow.setMaximumSize(QtCore.QSize(450, 600))
        self.verticalLayoutWidget = QtWidgets.QWidget(ChangeGWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 30, 366, 550))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.verticalLayoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(210, 20))
        self.label.setMaximumSize(QtCore.QSize(210, 20))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.combo_box_change_sign = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.combo_box_change_sign.setMinimumSize(QtCore.QSize(100, 30))
        self.combo_box_change_sign.setMaximumSize(QtCore.QSize(100, 30))
        self.combo_box_change_sign.setObjectName("combo_box_change_sign")
        self.horizontalLayout.addWidget(self.combo_box_change_sign)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(210, 20))
        self.label_2.setMaximumSize(QtCore.QSize(210, 20))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.combo_box_change_m = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.combo_box_change_m.setMinimumSize(QtCore.QSize(100, 30))
        self.combo_box_change_m.setMaximumSize(QtCore.QSize(100, 30))
        self.combo_box_change_m.setObjectName("combo_box_change_m")
        self.horizontalLayout_2.addWidget(self.combo_box_change_m)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(210, 20))
        self.label_3.setMaximumSize(QtCore.QSize(210, 20))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.combo_box_change_r = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.combo_box_change_r.setMinimumSize(QtCore.QSize(100, 30))
        self.combo_box_change_r.setMaximumSize(QtCore.QSize(100, 30))
        self.combo_box_change_r.setObjectName("combo_box_change_r")
        self.horizontalLayout_3.addWidget(self.combo_box_change_r)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.pb_start_change_g = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pb_start_change_g.setMinimumSize(QtCore.QSize(150, 50))
        self.pb_start_change_g.setMaximumSize(QtCore.QSize(150, 50))
        self.pb_start_change_g.setObjectName("pb_start_change_g")
        self.horizontalLayout_4.addWidget(self.pb_start_change_g)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)

        self.retranslateUi(ChangeGWindow)
        QtCore.QMetaObject.connectSlotsByName(ChangeGWindow)

    def retranslateUi(self, ChangeGWindow):
        _translate = QtCore.QCoreApplication.translate
        ChangeGWindow.setWindowTitle(_translate("ChangeGWindow", "???????? ?????????????????? ???????????? ??????????????????"))
        self.label.setText(_translate("ChangeGWindow", "<html><head/><body><p>???????????????? ???????? +/-</p></body></html>"))
        self.label_2.setText(_translate("ChangeGWindow", "???????????????? ?????????? ????????????"))
        self.label_3.setText(_translate("ChangeGWindow", "???????????????? ?????????????????????? ???? ????????????????????"))
        self.pb_start_change_g.setText(_translate("ChangeGWindow", "??????????????????"))
