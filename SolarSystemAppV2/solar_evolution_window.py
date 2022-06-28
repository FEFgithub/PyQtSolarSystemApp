# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'solar_evolution_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SolarEvolutionWindow(object):
    def setupUi(self, SolarEvolutionWindow):
        SolarEvolutionWindow.setObjectName("SolarEvolutionWindow")
        SolarEvolutionWindow.resize(600, 400)
        SolarEvolutionWindow.setMinimumSize(QtCore.QSize(600, 400))
        SolarEvolutionWindow.setMaximumSize(QtCore.QSize(600, 400))
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(SolarEvolutionWindow)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(40, 10, 524, 360))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.graphicsView = QtWidgets.QGraphicsView(self.verticalLayoutWidget_3)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_3.addWidget(self.graphicsView)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.combo_box_radius = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.combo_box_radius.setObjectName("combo_box_radius")
        self.verticalLayout.addWidget(self.combo_box_radius)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.combo_box_trace = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.combo_box_trace.setObjectName("combo_box_trace")
        self.verticalLayout_4.addWidget(self.combo_box_trace)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.combo_box_time = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.combo_box_time.setObjectName("combo_box_time")
        self.verticalLayout_2.addWidget(self.combo_box_time)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.pb_start_solar_evolution = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pb_start_solar_evolution.setMinimumSize(QtCore.QSize(150, 50))
        self.pb_start_solar_evolution.setObjectName("pb_start_solar_evolution")
        self.horizontalLayout_2.addWidget(self.pb_start_solar_evolution)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(SolarEvolutionWindow)
        QtCore.QMetaObject.connectSlotsByName(SolarEvolutionWindow)

    def retranslateUi(self, SolarEvolutionWindow):
        _translate = QtCore.QCoreApplication.translate
        SolarEvolutionWindow.setWindowTitle(_translate("SolarEvolutionWindow", "Окно модели эволюции Солнца"))
        self.label.setText(_translate("SolarEvolutionWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Изменить начальное </span></p><p><span style=\" font-size:10pt;\">расположение планет</span></p></body></html>"))
        self.label_3.setText(_translate("SolarEvolutionWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Скрывать/показывать</span></p><p><span style=\" font-size:10pt;\">траекторию планеты </span></p></body></html>"))
        self.label_2.setText(_translate("SolarEvolutionWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Изменить период </span></p><p><span style=\" font-size:10pt;\">обращения планет</span></p></body></html>"))
        self.pb_start_solar_evolution.setText(_translate("SolarEvolutionWindow", "Запустить "))