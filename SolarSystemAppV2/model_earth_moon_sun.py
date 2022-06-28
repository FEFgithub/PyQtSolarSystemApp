from vpython import sphere, vector, rotate 
import vpython as vp
import math
from constants_hub import ConstantsHub


const_hub = ConstantsHub()

class EarthMoonSun:

    def __init__(self, change_trace, change_t):
        self.change_trace = change_trace
        self.change_t = change_t
        self.calculate()

    def calculate(self):
        self.f_sun_earth = (const_hub.dict_EMS['G'] * const_hub.dict_EMS['Solar mass'] * 
        const_hub.dict_EMS['Earth mass'] / (const_hub.dict_EMS['Distance Earth Sun'] ** 2))
                                                                                            
        self.f_earth_moon = (const_hub.dict_EMS['G'] * const_hub.dict_EMS['Earth mass'] * 
        const_hub.dict_EMS['Moon mass'] / (const_hub.dict_EMS['Distance Earth Moon'] **2))
        
        self.w_moon = math.sqrt(self.f_earth_moon / (const_hub.dict_EMS['Moon mass'] *  
                                const_hub.dict_EMS['Distance Earth Moon']))

        self.w_earth = math.sqrt(self.f_sun_earth / (const_hub.dict_EMS['Earth mass'] *  
                                const_hub.dict_EMS['Distance Earth Sun']))

    def start_model(self):
        vec_moon = vector(0.55, 0, 0)

        sun = sphere(pos=vector(0, 0, 0), texture="Textures\\sun.jpg", radius=1, emissive=True)
        sunlight = vp.local_light(pos=vp.vec(0,0,0), color=vp.color.yellow)

        earth = sphere(pos=vector(3, 0, 0), texture="Textures\\Planets\\earth.jpg", 
                       radius=0.25, make_trail=self.change_trace)
        
        moon = sphere(pos=earth.pos + vec_moon, texture="Textures\\moon.jpg", radius=0.08, 
                      make_trail=self.change_trace)
        
        dt = self.change_t
        theta_earth = self.w_earth * dt
        theta_moon = self.w_moon * dt
        while dt <= 1 * 10 ** 10:
            earth.pos = rotate(earth.pos, angle=theta_earth, axis=vector(0, 0, 1))
            vec_moon = rotate(vec_moon, angle=theta_moon, axis=vector(0, 0, 1))
            moon.pos = earth.pos + vec_moon
            dt += 0.1
