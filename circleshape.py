import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius,*groups):
        super().__init__(*groups)
        
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self,othershape) :
        collision_distance = self.radius + othershape.radius
        self_pos = pygame.math.Vector2(self.position)
        other_pos = pygame.math.Vector2(othershape.position)
        if self_pos.distance_to(other_pos) <= collision_distance :
            return True
        else:
            return False