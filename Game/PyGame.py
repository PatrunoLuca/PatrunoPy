import pygame
from utils import import_animations


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.animations = import_animations("images/character/",128,128)
        self.image = self.animations["up-idle"][0]
        self.vector = pygame.math.Vector2(0, 0)
        self.rect = self.image.get_rect(center= pos)
        self.speed = 5
        self.animation_speed = 0.3
        self.counter = 0
        self.direction = "up"
        self.animation_type = "idle"
        self.old_animation = "up-idle"
    
    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction = "up"
            self.animation_type = "run"
            self.vector.x = 0
            self.vector.y = -1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction = "down"
            self.animation_type = "run"
            self.vector.x = 0
            self.vector.y = 1
        else:
            self.animation_type = "idle"
            self.vector.x = 0
            self.vector.y = 0
        '''
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction = "left"
            self.animation_type = "run"
            self.vector.x = -1
            self.vector.y = 0
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction = "right"
            self.animation_type = "run"
            self.vector.x = 1
            self.vector.y = 0
        '''


    
    def update(self):
        self.get_input()
        self.rect.x += self.vector.x * self.speed
        self.rect.y += self.vector.y * self.speed
        self.counter += self.animation_speed
        
        if self.counter >= len(self.animations[f"{self.direction}-{self.animation_type}"]):
            self.counter = 0

        self.new_animation = f"{self.direction}-{self.animation_type}"  
        if self.new_animation != self.old_animation:
            self.counter = 0.7

        self.old_animation = self.new_animation
        self.image = self.animations[self.new_animation][int(self.counter)] 
        #self.image = pygame.transform.flip(self.frame, True, False)
            

def main():
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    group = pygame.sprite.Group()
    player = Player((400,300))
    group.add(player)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
        screen.fill("white")
        player.update()
        group.draw(screen)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

if __name__ == "__main__":
    main()