from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, velocity,*groups):
        super().__init__(x, y, SHOT_RADIUS, *groups)   
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(velocity)
    
    def draw(self, screen):
        pygame.draw.circle(screen,(255,255,255),self.position,self.radius,2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)