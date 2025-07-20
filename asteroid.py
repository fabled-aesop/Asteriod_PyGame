from circleshape import *
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius,*groups):
        super().__init__(x, y, radius, *groups)   
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    
    def draw(self, screen):
        pygame.draw.circle(screen,(255,255,255),self.position,self.radius,2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split (self) :
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS :
            return
        else :
            split_direction = random.uniform(20,50)
            asteroid_1_velocity = self.velocity.rotate(split_direction)
            asteroid_2_velocity = self.velocity.rotate(-split_direction)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_1.velocity = asteroid_1_velocity * 1.2
            new_asteroid_2.velocity = asteroid_2_velocity * 1.2

