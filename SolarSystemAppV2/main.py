#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets  
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap

from model_solar_system import *
from model_solar_evolution import *
from model_earth_moon_sun import *

from constants_hub import ConstantsHub
from info_matplotlib import InfoMatplotlib

from main_window import Ui_MainWindow
from solar_system_window import Ui_SolarSystemWindow 
from info_window import Ui_InfoWindow
from info_ast_window import Ui_InfoAstWindow
from earth_moon_sun_window import Ui_EarthMoonSunWindow
from change_g_window import Ui_ChangeGWindow
from solar_evolution_window import Ui_SolarEvolutionWindow


const_hub = ConstantsHub()

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)

        self.add_picture('Pictures\\main_window.jpg', self.ui)

        self.ui.pb_solar_system.clicked.connect(self.click_pb_solar_system)
        self.ui.pb_solar_evolution.clicked.connect(self.click_pb_solar_evolution)
        self.ui.pb_earth_moon_sun.clicked.connect(self.click_pb_earth_moon_sun)
        self.ui.pb_change_g.clicked.connect(self.click_pb_change_g)
        self.ui.pb_info.clicked.connect(self.click_pb_info)
        self.ui.pb_info_ast.clicked.connect(self.click_pb_info_ast)
    
    def add_picture(self, path, ui_window):
        my_scene = QtWidgets.QGraphicsScene(self)
        my_pixmap = QPixmap(path)
        my_item = QtWidgets.QGraphicsPixmapItem(my_pixmap)
        my_scene.addItem(my_item) 
        ui_window.graphicsView.setScene(my_scene)
    
    def show_some_message(self, title, text):
        my_message = QMessageBox()
        my_message.setWindowTitle(title)
        my_message.setText(text)
        my_message.exec_()

    def click_pb_solar_system(self):
        self.second_form_solar_system = QtWidgets.QWidget()
        self.ui_second_form_solar_system = Ui_SolarSystemWindow()
        self.ui_second_form_solar_system.setupUi(self.second_form_solar_system)
        self.second_form_solar_system.show()
        self.ui_second_form_solar_system.pb_start_solar_system.clicked.connect(self.click_pb_start_solar_system)

        self.add_picture('Pictures\\solar_system.jpg', self.ui_second_form_solar_system)

        self.ui_second_form_solar_system.combo_box_radius.addItem('R')
        self.ui_second_form_solar_system.combo_box_radius.addItem('R*2')
        self.ui_second_form_solar_system.combo_box_radius.addItem('R/2')

        self.ui_second_form_solar_system.combo_box_trace.addItem('Показать след')
        self.ui_second_form_solar_system.combo_box_trace.addItem('Скрыть след')

        self.ui_second_form_solar_system.combo_box_time.addItem('T')
        self.ui_second_form_solar_system.combo_box_time.addItem('T*10')
        self.ui_second_form_solar_system.combo_box_time.addItem('T/10')
        
    def click_pb_start_solar_system(self):
        try:
            new_r, new_trace, new_t = None, None, None

            if self.ui_second_form_solar_system.combo_box_radius.currentText() == 'R':
                new_r = 1
            elif self.ui_second_form_solar_system.combo_box_radius.currentText() == 'R*2':
                new_r = 2
            else:
                new_r = 0.5
            
            if self.ui_second_form_solar_system.combo_box_trace.currentText() == 'Показать след':
                new_trace = True
            else:
                new_trace = False
            
            if self.ui_second_form_solar_system.combo_box_time.currentText() == 'T':
                new_t = 0.00005
            elif self.ui_second_form_solar_system.combo_box_time.currentText() == 'T*10':
                new_t = 0.00005 * 10
            else:
                new_t = 0.00005 / 10

            model_solar_system = ModelSolarSystem(change_r=new_r, change_trace=new_trace, change_t=new_t,
                                                change_sign=1, change_m=1, change_func_r=3)
            model_solar_system.start_model()
        except:
            exit()

    def click_pb_solar_evolution(self):
        self.second_form_solar_evolution = QtWidgets.QWidget()
        self.ui_second_form_solar_evolution = Ui_SolarEvolutionWindow()
        self.ui_second_form_solar_evolution.setupUi(self.second_form_solar_evolution)
        self.second_form_solar_evolution.show() 

        self.add_picture('Pictures\\solar_evolution.jpg', self.ui_second_form_solar_evolution)

        self.ui_second_form_solar_evolution.pb_start_solar_evolution.clicked.connect(self.click_pb_start_solar_evolution)

        self.ui_second_form_solar_evolution.combo_box_radius.addItem('R')
        self.ui_second_form_solar_evolution.combo_box_trace.addItem('Скрыть след')
        self.ui_second_form_solar_evolution.combo_box_time.addItem('T')
        self.ui_second_form_solar_evolution.combo_box_time.addItem('T*10')
        self.ui_second_form_solar_evolution.combo_box_time.addItem('T/10')

    def click_pb_start_solar_evolution(self):
        try:
            new_r, new_trace, new_t = 1, False, None
            
            if self.ui_second_form_solar_evolution.combo_box_time.currentText() == 'T':
                new_t = 0.00005
                new_r_sun = 0.00001
            elif self.ui_second_form_solar_evolution.combo_box_time.currentText() == 'T*10':
                new_t = 0.00005 * 10
                new_r_sun = 0.00001 * 10
            else:
                new_t = 0.00005 / 10
                new_r_sun = 0.00001 / 10
                
            model_solar_evolution = ModelSolarEvolution(change_r=new_r, change_trace=new_trace, 
                                                        change_t=new_t, change_r_sun=new_r_sun)
            model_solar_evolution.start_model()
        except:
            exit()

    def click_pb_earth_moon_sun(self):
        self.second_form_earth_moon_sun = QtWidgets.QWidget()
        self.ui_second_form_earth_moon_sun = Ui_EarthMoonSunWindow()
        self.ui_second_form_earth_moon_sun.setupUi(self.second_form_earth_moon_sun)
        self.second_form_earth_moon_sun.show()

        self.add_picture('Pictures\\earth_moon_sun.jpg', self.ui_second_form_earth_moon_sun) 

        self.ui_second_form_earth_moon_sun.combo_box_radius.addItem('R')
        self.ui_second_form_earth_moon_sun.combo_box_trace.addItem('Скрыть след')
        self.ui_second_form_earth_moon_sun.combo_box_trace.addItem('Показать след')
        self.ui_second_form_earth_moon_sun.combo_box_time.addItem('T')
        self.ui_second_form_earth_moon_sun.combo_box_time.addItem('T*10')
        self.ui_second_form_earth_moon_sun.combo_box_time.addItem('T/10')

        self.ui_second_form_earth_moon_sun.pb_start_earth_moon_sun.clicked.connect(self.click_pb_start_earth_moon_sun)
    
    def click_pb_start_earth_moon_sun(self):
        try:
            new_trace, new_t = None, None

            if self.ui_second_form_earth_moon_sun.combo_box_trace.currentText() == 'Показать след':
                new_trace = True
            else:
                new_trace = False
            
            if self.ui_second_form_earth_moon_sun.combo_box_time.currentText() == 'T':
                new_t = 10
            elif self.ui_second_form_earth_moon_sun.combo_box_time.currentText() == 'T*10':
                new_t = 100
            else:
                new_t = 1

            earth_moon_sun = EarthMoonSun(change_trace=new_trace, change_t=new_t)
            earth_moon_sun.start_model()
        except:
            exit()

    def click_pb_change_g(self):
        self.second_form_change_g = QtWidgets.QWidget()
        self.ui_second_form_change_g = Ui_ChangeGWindow()
        self.ui_second_form_change_g.setupUi(self.second_form_change_g)
        self.second_form_change_g.show()

        self.add_picture('Pictures\\change_g.jpg', self.ui_second_form_change_g)

        self.ui_second_form_change_g.combo_box_change_sign.addItem('Притяжение')
        self.ui_second_form_change_g.combo_box_change_sign.addItem('Отталкивание')
        self.ui_second_form_change_g.combo_box_change_m.addItem('M')
        self.ui_second_form_change_g.combo_box_change_m.addItem('M*10')
        self.ui_second_form_change_g.combo_box_change_m.addItem('M/10')
        self.ui_second_form_change_g.combo_box_change_r.addItem('~ 1/R^2')
        self.ui_second_form_change_g.combo_box_change_r.addItem('~ 1/R')
        self.ui_second_form_change_g.combo_box_change_r.addItem('~ R^2')

        self.ui_second_form_change_g.pb_start_change_g.clicked.connect(self.click_pb_start_change_g)

    def click_pb_start_change_g(self):
        try:
            new_r, new_trace, new_t = 1, True, 0.00005

            new_sign, new_m, new_func_r = None, None, None

            if self.ui_second_form_change_g.combo_box_change_sign.currentText() == 'Притяжение':
                new_sign = 1
            else:
                new_sign = -1
            
            if self.ui_second_form_change_g.combo_box_change_m.currentText() == 'M':
                new_m = 1
            elif self.ui_second_form_change_g.combo_box_change_m.currentText() == 'M*10':
                new_m = 10
            else:
                new_m = 0.1
            
            if self.ui_second_form_change_g.combo_box_change_r.currentText() == '~ 1/R^2':
                new_func_r = 3
            elif self.ui_second_form_change_g.combo_box_change_r.currentText() == '~ 1/R':
                new_func_r = 2
            else:
                new_func_r = -1
            
            model_change_g = ModelSolarSystem(change_r=new_r, change_trace=new_trace, change_t=new_t,
                                        change_sign=new_sign, change_m=new_m, change_func_r=new_func_r)
            model_change_g.start_model()
        except:
            exit()

    def click_pb_info(self):
        self.second_form_info = QtWidgets.QWidget()
        self.ui_second_form_info = Ui_InfoWindow()
        self.ui_second_form_info.setupUi(self.second_form_info)
        self.second_form_info.show()

        self.add_picture('Pictures\\info.jpg', self.ui_second_form_info)

        self.ui_second_form_info.pb_start_info_change_g.clicked.connect(self.click_pb_start_info_change_g)
        self.ui_second_form_info.pb_start_info_info.clicked.connect(self.click_pb_start_info_info)
        self.ui_second_form_info.pb_start_info_info_ast.clicked.connect(self.click_pb_start_info_info_ast)
        self.ui_second_form_info.pb_start_info_earth_moon_sun.clicked.connect(self.click_pb_start_info_earth_moon_sun)
        self.ui_second_form_info.pb_start_info_solar_evolution.clicked.connect(self.click_pb_start_info_solar_evolution)
        self.ui_second_form_info.pb_start_info_solar_system.clicked.connect(self.click_pb_start_info_solar_system)

    def click_pb_start_info_change_g(self):
        self.show_some_message('О модели изменения g', const_hub.dict_text_messages['info_change_g'])
    
    def click_pb_start_info_info(self):
        self.show_some_message('О программе', const_hub.dict_text_messages['info_info'])
    
    def click_pb_start_info_info_ast(self):
        self.show_some_message('Об астрономии', const_hub.dict_text_messages['info_info_ast'])

    def click_pb_start_info_earth_moon_sun(self):
        self.show_some_message('О модели Земля Луна Солнце', const_hub.dict_text_messages['info_earth_moon_sun'])
    
    def click_pb_start_info_solar_evolution(self):
        self.show_some_message('О модели эволюция Солнца', const_hub.dict_text_messages['info_solar_evolution'])

    def click_pb_start_info_solar_system(self):
        self.show_some_message('О модели Солнечная система', const_hub.dict_text_messages['info_solar_system'])

    def click_pb_info_ast(self):
        self.second_form_info_ast = QtWidgets.QWidget()
        self.ui_second_form_info_ast = Ui_InfoAstWindow()
        self.ui_second_form_info_ast.setupUi(self.second_form_info_ast)
        self.second_form_info_ast.show()

        self.add_picture('Pictures\\info_ast.jpg', self.ui_second_form_info_ast)

        for one_variant in const_hub.list_graph_variants:
            self.ui_second_form_info_ast.combo_box_info_ast.addItem(one_variant)    

        self.ui_second_form_info_ast.pb_start_info_ast.clicked.connect(self.click_pb_start_info_ast)

    def click_pb_start_info_ast(self):
        my_flag = None
        if self.ui_second_form_info_ast.combo_box_info_ast.currentText() == 'График распределения планет по массам':
            my_flag = 1
        elif self.ui_second_form_info_ast.combo_box_info_ast.currentText() =='График распределения планет по радиусам':
            my_flag = 2
        elif self.ui_second_form_info_ast.combo_box_info_ast.currentText() == 'График распределения планет по плотностям':
            my_flag = 3
        elif self.ui_second_form_info_ast.combo_box_info_ast.currentText() == 'График распределения планет по ускорениям свободного падения':
            my_flag = 4
        elif self.ui_second_form_info_ast.combo_box_info_ast.currentText() == 'График распределения планет по периодам обращения вокруг своей оси':
            my_flag = 5
        elif self.ui_second_form_info_ast.combo_box_info_ast.currentText() == 'График распределения планет по периодам обращения вокруг Солнца':
            my_flag = 6
        elif self.ui_second_form_info_ast.combo_box_info_ast.currentText() == 'График распределения планет по расстояниям от Солнца':
            my_flag = 7
        elif self.ui_second_form_info_ast.combo_box_info_ast.currentText() == 'График распределения планет по орбитальным скоростям':
            my_flag = 8
        else:
            my_flag = 9

        info_math = InfoMatplotlib(my_flag)
        info_math.show_graph()


if __name__ == '__main__':

    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()

    sys.exit(app.exec())
