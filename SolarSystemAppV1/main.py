#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtGui
from gui_app import Ui_MainWindow  
import sys
from earth_moon_sun import EarthMoonSun 
from solar_system import SolarSystem
from solar_evolution import SolarEvolution
from PyQt5.QtWidgets import QMessageBox
 

class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):

        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)

        # Обработчики событий нажатия на кнопки
        self.ui.pb_EMS.clicked.connect(self.click_pb_EMS)
        self.ui.pb_Info.clicked.connect(self.click_pb_Info)
        self.ui.pb_SolarSystem.clicked.connect(self.click_pb_SolarSystem)
        self.ui.pb_Sun.clicked.connect(self.click_pb_Sun)

        # Добавление разных вариантов в комбо-бокс 
        self.ui.comboBox.addItem("О программе")
        self.ui.comboBox.addItem("Система Земля-Луна-Солнце")
        self.ui.comboBox.addItem("Солнечная система")
        self.ui.comboBox.addItem("Эволюция Солнца")

        # Выбор масштаба расстояний
        self.ui.comboBox_2.addItem("Реальный масштаб")
        self.ui.comboBox_2.addItem("Наглядный масштаб")
        

    # Функции, описывающие отклик на нажатие на ту или иную кнопку 
    def click_pb_Info(self):

        info = self.ui.comboBox.currentText()
        msg = QMessageBox()

        if info == 'О программе':
            msg.setWindowTitle("О программе")
            msg.setText('   Данное приложение позволяет визуализировать некоторые физические процессы в Солнечной системе. ' + 
                        'При моделировании Солнечной системы и эволюции Солнца предусмотрено 2 вараната масштаба: реальный, где ' + 
                        'соблюдены действительные пропорции расстояний планет от Солнца и наглядный - где Солнечная система показана ' + 
                        'более компактно. Во всех видах масштабов периоды обращений планет соотесены с реальными периодами, однако ' +
                        'не визуализированы астероиды, метеорные кольца и кольца планет, так же не показано вращение и наклон оси планет. ' +
                        'В браузере с помощью колеса прокрутки мыши пользователь может приближать и отдалять камеру, с помощью правой кнопки ' +
                        'мыши можно вращать систему на 360 градусов, левой кнопокй мыши можно зафиксировать систему без вращения.')

        if info == 'Система Земля-Луна-Солнце':
            msg.setWindowTitle("Система Земля-Луна-Солнце")
            msg.setText('   В данной физической модели показана система трёх тел Земля-Луна-Солнце. Луна совершает сложное движение, ' + 
                        'испытывая гравитационное влияние Солнца и Земли, её траектория выделена.')

        if info == 'Солнечная система':
            msg.setWindowTitle("Солнечная система")
            msg.setText('   Модель Солнечной системы показывает реальный масштаб периодов обращений планет, расстояний, текстуры ' + 
                        'планет соотвествуют реальным астрономическим снимкам.')

        if info == 'Эволюция Солнца':
            msg.setWindowTitle("Эволюция Солнца")
            msg.setText('   В данной модели показана упрощённая эволюция Солнца из желтого карлика в красный гигант и затем в ' + 
                        'белый карлик. Принята гипотеза, по которой Меркурий, Венера и Земля будут уничтожены, а орбиты других планет ' + 
                        'увеличены вследствии потери звездой половины своей массы.')

        msg.exec_()

    def click_pb_SolarSystem(self):
        
        start = SolarSystem()
        if self.ui.comboBox_2.currentText() == 'Реальный масштаб':
            start.move(1.16, 2.17, 3, 4.57, 15.6, 28.62, 57.57, 90.18, 0.9, 0.1, 0.2, 0.22, 0.18, 0.6, 0.4, 0.35, 0.35)
        else:
            start.move(1, 2, 3, 4, 5, 6, 7, 8, 0.55, 0.1, 0.2, 0.22, 0.18, 0.4, 0.29, 0.25, 0.25)
        
    
    def click_pb_Sun(self):

        start = SolarEvolution()
        if self.ui.comboBox_2.currentText() == 'Реальный масштаб':
            start.move(1.16, 2.17, 3, 4.57, 15.6, 28.62, 57.57, 90.18, 0.9, 0.1, 0.2, 0.22, 0.18, 0.6, 0.4, 0.35, 0.35)
        else:
            start.move(1, 2, 3, 4, 5, 6, 7, 8, 0.55, 0.1, 0.2, 0.22, 0.18, 0.4, 0.29, 0.25, 0.25)
    
    # Функция с реализацией логики программы 
    def click_pb_EMS(self):

        start = EarthMoonSun()

# Если файл является исполняемым, а не импортируемым модулем 
if __name__ == '__main__':

    # Создаем и показываем экземпляр приложения
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()

    sys.exit(app.exec())
