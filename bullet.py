import pygame
from circleshape import *
from constants import *
class Bullet(CircleShape):
    def __init__(self,x,y,SHOT_RADIUS):
        super().__init__(x ,y,  SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position, SHOT_RADIUS)


    def update(self, dt):
        self.position += self.velocity *dt 