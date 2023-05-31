import random
class BoringParticle:
    def __init__(self, x,y, v_x, v_y):
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.kleur = (55,40,255)

    def bewegen(self,interval):
        self.x += self.v_x * interval
        self.y += self.v_y * interval

    def reset(self, breedte, hoogte):
        if (self.y < 0) or (self.y > hoogte):
            self.x, self.y = breedte//2, hoogte//2
            self.v_x = (random.random()* 1.7)-0.85
            self.v_y = (random.random()* 1.7)-0.85
        if (self.y < 0) or (self.x > breedte):
            self.x, self.y = breedte//2, hoogte//2
            self.v_x = (random.random()* 1.7)-0.85
            self.v_y = (random.random()* 1.7)-0.85    
        if (random.random() > 0.9999):
            self.x, self.y = breedte//2, hoogte//2
            self.v_x = (random.random()* 1.7)-0.85
            self.v_y = (random.random()* 1.7)-0.85  