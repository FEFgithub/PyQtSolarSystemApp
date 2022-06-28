import matplotlib.pyplot as plt
import numpy as np
from constants_hub import ConstantsHub


const_hub = ConstantsHub()

class InfoMatplotlib: 
    def __init__(self, my_flag):
        self.my_flag = my_flag 
    
    def add_values(self, x, y):
            for i in range(len(x)):
                plt.text(i, y[i], y[i])

    def show_graph(self):
        x_planets = const_hub.tuple_names_planets 
        x_position = np.arange(len(x_planets)) 
        y_variant, y_text = None, None
        if self.my_flag == 1:
            y_variant = const_hub.dict_for_graps['Masses']
            y_text = 'Массы, в массах Земли'
        elif self.my_flag == 2:
            y_variant = const_hub.dict_for_graps['Radiuses']
            y_text = 'Радиусы, в радиусах Земли'
        elif self.my_flag == 3:
            y_variant = const_hub.dict_for_graps['Densities']
            y_text = 'Плотность, в г/см^3'
        elif self.my_flag == 4:
            y_variant = const_hub.dict_for_graps['g on equator']
            y_text = 'g, в м/с^2'
        elif self.my_flag == 5:
            y_variant = const_hub.dict_for_graps['Periods around self']
            y_text = 'Периоды вокруг своей оси, в часах'
        elif self.my_flag == 6:
            y_variant = const_hub.dict_for_graps['Periods around Sun']
            y_text = 'Периоды вокруг Солнца, в годах'
        elif self.my_flag == 7:
            y_variant = const_hub.dict_for_graps['Distances from Sun']
            y_text = 'Расстояние от Солнца, в а.е.'
        elif self.my_flag == 8:
            y_variant = const_hub.dict_for_graps['Orbital speeds']
            y_text = 'Средняя орбитальная скорость, в км/c'
        else:
            y_variant = const_hub.dict_for_graps['Orbital e']
            y_text = 'Эксцентриситет орбит'
        plt.bar(x_position, y_variant, align='center', alpha=0.5, color=['r', 'y', 'g', 'b', 'c', 'k', 'olive', 'gray']) 
        self.add_values(x_position, y_variant)
        plt.xticks(x_position, x_planets)  
        plt.ylabel(y_text)
        plt.title('Планеты') 
        plt.show()
