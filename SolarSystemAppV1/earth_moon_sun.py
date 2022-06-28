from vpython import sphere, vector, color, rotate 
import math


class EarthMoonSun:

    def __init__(self):

        self.G = 6.667e-11 # гравитационная постоянная, м^3 кг^-1 с^-2
        self.M_SUN = 1.9885e30  # масса Солнца, кг
        self.M_EARTH = 5.97e24  # масса Земли, кг
        self.M_MOON = 7.348e22  # масса Луны, кг
        self.R_SUN_EARTH = 1.496e11  # среднее расстояние от Солнца до Земли, метры
        self.R_EARTH_MOON = 384.4e6  # расстояние от Земли до Луны

        self.calculate()
        self.move()

    def calculate(self):

        # Гравитационная сила между Солнцем и Землей. Н
        self.F_SUN_EARTH = self.G*self.M_SUN*self.M_EARTH/(self.R_SUN_EARTH ** 2)
        # Гравитационная сила между Землей и Луной, Н
        self.F_EARTH_MOON = self.G*self.M_EARTH*self.M_MOON/(self.R_EARTH_MOON **2)
        # Угловая скорость Луны
        self.W_MOON = math.sqrt(self.F_EARTH_MOON/(self.M_MOON*self.R_EARTH_MOON))
        # Угловая скорость Земли
        self.W_EARTH = math.sqrt(self.F_SUN_EARTH/(self.M_EARTH*self.R_SUN_EARTH))

    def move(self):

        # Инициализируем начальный вектор
        v = vector(0.55, 0, 0)
        # Земля 
        Earth = sphere(pos=vector(3, 0, 0), texture="Pictures\\earth.jpg", radius=.25, make_trail=True)
        # Луна
        Moon = sphere(pos=Earth.pos+v, texture="Pictures\\moon.jpg", radius=0.08, make_trail=True)
        # Солнце
        Sun = sphere(pos=vector(0, 0, 0), texture="Pictures\\sun.jpg", radius=1)

        # Будем использовать полярные координаты
        # Шаг
        dt = 100
        # углы поворота за один шаг:
        theta_earth = self.W_EARTH * dt
        theta_moon = self.W_MOON * dt
        while dt <= 2.8 * 10 ** 6:
            # Земля и Луна поворачиваются вокруг оси z (0,0,1)
            Earth.pos = rotate(Earth.pos, angle=theta_earth, axis=vector(0, 0, 1))
            v = rotate(v, angle=theta_moon, axis=vector(0, 0, 1))
            Moon.pos = Earth.pos + v
            dt += 10

