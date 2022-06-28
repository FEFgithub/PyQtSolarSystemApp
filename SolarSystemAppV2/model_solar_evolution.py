import vpython as vp
from vpython import color
from constants_hub import ConstantsHub


const_hub = ConstantsHub()

class ModelSolarEvolution:
    def __init__(self, change_r, change_trace, change_t, change_r_sun):
        self.change_r = change_r
        self.change_trace = change_trace
        self.change_t = change_t
        self.change_r_sun = change_r_sun
    
    def step_method(self, def_acceleration, r_max_0, v_0, dt):
        dt_2 = dt / 2.0
        r_max_1 = r_max_0 + v_0 * dt_2
        v_1 = v_0 + def_acceleration(r_max_1) * dt          
        r_max_1 = r_max_1 + v_1 * dt_2
        return r_max_1, v_1
    
    def acceleration(self, r_vector):
        mod_r_vector = vp.mag(r_vector)
        return -const_hub.GM * r_vector / (mod_r_vector ** 3)        

    def start_model(self):
     
        r_max_mercury = vp.vec(self.change_r * const_hub.dict_apogelium['Mercury'], 0.0, 0.0)
        r_max_venus = vp.vec(self.change_r * const_hub.dict_apogelium['Venus'], 0.0, 0.0)
        r_max_earth = vp.vec(self.change_r * const_hub.dict_apogelium['Earth'], 0.0, 0.0)
        r_max_mars = vp.vec(self.change_r * const_hub.dict_apogelium['Mars'], 0.0, 0.0)
        r_max_jupiter = vp.vec(self.change_r * const_hub.dict_apogelium['Jupiter'], 0.0, 0.0)
        r_max_saturn = vp.vec(self.change_r * const_hub.dict_apogelium['Saturn'], 0.0, 0.0)
        r_max_uranium = vp.vec(self.change_r * const_hub.dict_apogelium['Uranium'], 0.0, 0.0)
        r_max_neptune = vp.vec(self.change_r * const_hub.dict_apogelium['Neptune'], 0.0, 0.0)

        v_mercury = vp.vec(0.0, const_hub.dict_speeds['Mercury'], 0.0)
        v_venus = vp.vec(0.0, const_hub.dict_speeds['Venus'], 0.0)
        v_earth = vp.vec(0.0, const_hub.dict_speeds['Earth'], 0.0)
        v_mars = vp.vec(0.0, const_hub.dict_speeds['Mars'], 0.0)
        v_jupiter = vp.vec(0.0, const_hub.dict_speeds['Jupiter'], 0.0)
        v_saturn = vp.vec(0.0, const_hub.dict_speeds['Saturn'], 0.0)
        v_uranium = vp.vec(0.0, const_hub.dict_speeds['Uranium'], 0.0)
        v_neptune = vp.vec(0.0, const_hub.dict_speeds['Neptune'], 0.0)

        sun = vp.sphere(pos=vp.vec(0,0,0), radius=0.22, texture="Textures\\sun.jpg", emissive=True)
        sunlight = vp.local_light(pos=vp.vec(0,0,0), color=vp.color.yellow) 
        mercury = vp.sphere(pos=r_max_mercury, radius=const_hub.dict_radiuses_planets['Mercury'],
                            make_trail=self.change_trace, texture="Textures\\Planets\\mercury.jpg")
        venus = vp.sphere(pos=r_max_venus, radius=const_hub.dict_radiuses_planets['Venus'], 
                            make_trail=self.change_trace, texture="Textures\\Planets\\venus.jpg")
        earth = vp.sphere(pos=r_max_earth, radius=const_hub.dict_radiuses_planets['Earth'], 
                            make_trail=self.change_trace, texture="Textures\\Planets\\earth.jpg")
        mars = vp.sphere(pos=r_max_mars, radius=const_hub.dict_radiuses_planets['Mars'], 
                            make_trail=self.change_trace, texture="Textures\\Planets\\mars.jpg")
        jupiter = vp.sphere(pos=r_max_jupiter, radius=const_hub.dict_radiuses_planets['Jupiter'], 
                            make_trail=self.change_trace, texture="Textures\\Planets\\jupiter.jpg")
        saturn = vp.sphere(pos=r_max_saturn, radius=const_hub.dict_radiuses_planets['Saturn'], 
                            make_trail=self.change_trace, texture="Textures\\Planets\\saturn.jpg")
        uranium = vp.sphere(pos=r_max_uranium, radius=const_hub.dict_radiuses_planets['Uranium'], 
                            make_trail=self.change_trace, texture="Textures\\Planets\\uranium.jpg")
        neptune = vp.sphere(pos=r_max_neptune, radius=const_hub.dict_radiuses_planets['Neptune'], 
                            make_trail=self.change_trace, texture="Textures\\Planets\\neptune.jpg")

        t, T, dt = 0.0, 1_000_000.0, self.change_t
        while t < T:
            vp.rate(1000)

            r_max_mercury, v_mercury = self.step_method(self.acceleration, r_max_mercury, v_mercury, dt)
            r_max_venus, v_venus = self.step_method(self.acceleration, r_max_venus, v_venus, dt)
            r_max_earth, v_earth = self.step_method(self.acceleration, r_max_earth, v_earth, dt)
            r_max_mars, v_mars = self.step_method(self.acceleration, r_max_mars, v_mars, dt)
            r_max_jupiter, v_jupiter = self.step_method(self.acceleration, r_max_jupiter, v_jupiter, dt)
            r_max_saturn, v_saturn = self.step_method(self.acceleration, r_max_saturn, v_saturn, dt)
            r_max_uranium, v_uranium = self.step_method(self.acceleration, r_max_uranium, v_uranium, dt)
            r_max_neptune, v_neptune = self.step_method(self.acceleration, r_max_neptune, v_neptune, dt)

            mercury.pos = r_max_mercury
            venus.pos = r_max_venus
            earth.pos = r_max_earth
            mars.pos = r_max_mars
            jupiter.pos = r_max_jupiter
            saturn.pos = r_max_saturn
            uranium.pos = r_max_uranium
            neptune.pos = r_max_neptune

            if (sun.texture == 'Textures\\sun.jpg') or (sun.texture == 'Textures\\red_gigant.jpg'):
                 sun.radius += self.change_r_sun

            if sun.radius >= 0.4:
                sun.texture = 'Textures\\red_gigant.jpg'
                mercury.texture = None
                mercury.color = color.black

            if sun.radius >= 0.6:
                venus.texture = 'Textures\\red_earth.jpg'
            
            if sun.radius >= 0.7:
                venus.texture = None
                venus.color = color.black
                earth.texture = 'Textures\\Planets\\venus.jpg'

            if sun.radius > 0.85:
                earth.texture = 'Textures\\red_earth.jpg'
            
            if sun.radius >1.2:
                sun.radius = 0.01
                sun.texture = 'Textures\\white_dwarf.jpg'

                earth.texture = None
                earth.color = color.black

            t += dt
