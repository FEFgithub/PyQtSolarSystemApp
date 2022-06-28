from vpython import sphere, vector, color, rotate 
import math


class SolarEvolution:

    def __init__(self):

        self.G = 6.667e-11 # гравитационная постоянная, м^3 кг^-1 с^-2

        self.M_SUN = 1.9885e30  # масса Солнца, кг
        self.M_MERCURY = 3.33e23 # масса Меркурия, кг 
        self.M_VENUS = 4.87e24 # масса Венеры, кг
        self.M_EARTH = 5.97e24  # масса Земли, кг 
        self.M_MARS = 6.42e23 # масса Марса, кг 
        self.M_JUPITER = 1.89e27 # масса Юпитера, кг
        self.M_SATURN = 5.68e26 # масса Сатурна, кг
        self.M_URANUS = 8.68e25 # масса Урана, кг
        self.M_NEPTUNE = 1.02e26 # масса Нептуна, кг

        self.R_SUN_MERCURY = 5.79e10 # среднее расстояние от Солнца до Меркурия, метры
        self.R_SUN_VENUS = 1.082e11  # среднее расстояние от Солнца до Венеры, метры
        self.R_SUN_EARTH = 1.496e11  # среднее расстояние от Солнца до Земли, метры
        self.R_SUN_MARS = 2.28e11  # среднее расстояние от Солнца до Марса, метры
        self.R_SUN_JUPITER = 7.781e11 # среднее расстояние от Солнца до Юпитера, метры
        self.R_SUN_SATURN = 1.427e12 # среднее расстояние от Солнца до Сатурна, метры
        self.R_SUN_URANUS = 2.871e12 # среднее расстояние от Солнца до Урана, метры
        self.R_SUN_NEPTUNE = 4.497e12 # среднее расстояние от Солнца до Нептуна, метры

        self.calculate()

    def calculate(self):

        # Гравитационная сила между Солнцем и Меркурием, Н
        self.F_SUN_MERCURY = self.G*self.M_SUN*self.M_MERCURY/(self.R_SUN_MERCURY ** 2)
        # Угловая скорость Меркурия
        self.W_MERCURY = math.sqrt(self.F_SUN_MERCURY/(self.M_MERCURY*self.R_SUN_MERCURY))

        # Гравитационная сила между Солнцем и Венерой, Н
        self.F_SUN_VENUS = self.G*self.M_SUN*self.M_VENUS/(self.R_SUN_VENUS ** 2)
        # Угловая скорость Венеры
        self.W_VENUS = math.sqrt(self.F_SUN_VENUS/(self.M_VENUS*self.R_SUN_VENUS))

        # Гравитационная сила между Солнцем и Землёй, Н
        self.F_SUN_EARTH = self.G*self.M_SUN*self.M_EARTH/(self.R_SUN_EARTH ** 2)
        # Угловая скорость Земли
        self.W_EARTH = math.sqrt(self.F_SUN_EARTH/(self.M_EARTH*self.R_SUN_EARTH))

        # Гравитационная сила между Солнцем и Марсом, Н
        self.F_SUN_MARS = self.G*self.M_SUN*self.M_MARS/(self.R_SUN_MARS ** 2)
        # Угловая скорость Марса
        self.W_MARS = math.sqrt(self.F_SUN_MARS/(self.M_MARS*self.R_SUN_MARS))

        # Гравитационная сила между Солнцем и Юпитером, Н
        self.F_SUN_JUPITER = self.G*self.M_SUN*self.M_JUPITER/(self.R_SUN_JUPITER ** 2)
        # Угловая скорость Юпитера
        self.W_JUPITER = math.sqrt(self.F_SUN_JUPITER/(self.M_JUPITER*self.R_SUN_JUPITER))

        # Гравитационная сила между Солнцем и Сатурном, Н
        self.F_SUN_SATURN = self.G*self.M_SUN*self.M_SATURN/(self.R_SUN_SATURN ** 2)
        # Угловая скорость Сатурна
        self.W_SATURN = math.sqrt(self.F_SUN_SATURN/(self.M_SATURN*self.R_SUN_SATURN))

        # Гравитационная сила между Солнцем и Ураном, Н
        self.F_SUN_URANUS = self.G*self.M_SUN*self.M_URANUS/(self.R_SUN_URANUS ** 2)
        # Угловая скорость Урана
        self.W_URANUS = math.sqrt(self.F_SUN_URANUS/(self.M_URANUS*self.R_SUN_URANUS))

        # Гравитационная сила между Солнцем и Нептуном, Н
        self.F_SUN_NEPTUNE = self.G*self.M_SUN*self.M_NEPTUNE/(self.R_SUN_NEPTUNE ** 2)
        # Угловая скорость Нептуна
        self.W_NEPTUNE = math.sqrt(self.F_SUN_NEPTUNE/(self.M_NEPTUNE*self.R_SUN_NEPTUNE))
    
    def move(self, x1, x2, x3, x4, x5, x6, x7, x8, r0, r1, r2, r3, r4, r5, r6, r7, r8):

        # Солнце
        Sun = sphere(pos=vector(0, 0, 0), texture="Pictures\\sun.jpg", radius=r0)
        # Меркурий
        Mercury = sphere(pos=vector(x1, 0, 0), texture="Pictures\\mercury.jpg", radius=r1, make_trail=False)
        # Венера
        Venus = sphere(pos=vector(x2, 0, 0), texture="Pictures\\venus.jpg", radius=r2, make_trail=False)
        # Земля 
        Earth = sphere(pos=vector(x3, 0, 0), texture="Pictures\\earth.jpg", radius=r3, make_trail=False)
        # Марс 
        Mars = sphere(pos=vector(x4, 0, 0), texture="Pictures\\mars.jpg",  radius=r4, make_trail=False)
        # Юпитер
        Jupiter = sphere(pos=vector(x5, 0, 0), texture="Pictures\\jupiter.jpg", radius=r5, make_trail=False)
        # Сатурн
        Saturn = sphere(pos=vector(x6, 0, 0), texture="Pictures\\saturn.jpg", radius=r6, make_trail=False)
        # Уран
        Uranus = sphere(pos=vector(x7, 0, 0), texture="Pictures\\uranus.jpg", radius=r7, make_trail=False)
        # Нептун 
        Neptune = sphere(pos=vector(x8, 0, 0), texture="Pictures\\neptune.jpg", radius=r8, make_trail=False)

        # Будем использовать полярные координаты
        # Шаг
        dt = 100
        # углы поворота за один шаг:
        theta_mercury = self.W_MERCURY * dt
        theta_venus = self.W_VENUS * dt
        theta_earth = self.W_EARTH * dt
        theta_mars = self.W_MARS * dt
        theta_jupiter = self.W_JUPITER * dt
        theta_saturn = self.W_SATURN * dt
        theta_uranus = self.W_URANUS * dt
        theta_neptune = self.W_NEPTUNE * dt

        while dt <= 10 ** 10:
            # Планеты вращаются вокруг оси z (0,0,1)
            Mercury.pos = rotate(Mercury.pos, angle=theta_mercury, axis=vector(0, 0, 1))
            Venus.pos = rotate(Venus.pos, angle=theta_venus, axis=vector(0, 0, 1))
            Earth.pos = rotate(Earth.pos, angle=theta_earth, axis=vector(0, 0, 1))
            Mars.pos = rotate(Mars.pos, angle=theta_mars, axis=vector(0, 0, 1))
            Jupiter.pos = rotate(Jupiter.pos, angle=theta_jupiter, axis=vector(0, 0, 1))
            Saturn.pos = rotate(Saturn.pos, angle=theta_saturn, axis=vector(0, 0, 1))
            Uranus.pos = rotate(Uranus.pos, angle=theta_uranus, axis=vector(0, 0, 1))
            Neptune.pos = rotate(Neptune.pos, angle=theta_neptune, axis=vector(0, 0, 1))

            if (Sun.texture == 'Pictures\\sun.jpg') or (Sun.texture == 'Pictures\\red_gigant.jpg'):
                 Sun.radius += 0.00001

            if Sun.radius >= 1.1:
                Sun.texture = 'Pictures\\red_gigant.jpg'
                Mercury.texture = None
                Mercury.color = color.black

            if Sun.radius >= 1.5:
                Venus.texture = 'Pictures\\red_earth.jpg'
            
            if Sun.radius >= 2.1:
                Venus.texture = None
                Venus.color = color.black
                Earth.texture = 'Pictures\\venus.jpg'

            if Sun.radius > 2.5:
                Earth.texture = 'Pictures\\red_earth.jpg'
            
            if Sun.radius >3.2:
                Sun.radius = 0.2
                Sun.texture = 'Pictures\\white_dwarf.jpg'

                Earth.texture = None
                Earth.color = color.black

                Mars.pos *= 1.5
                Jupiter.pos *= 1.5
                Saturn.pos *= 1.5
                Uranus.pos *= 1.5
                Neptune.pos *= 1.5

            dt += 10
