import pgzrun
from utils import zero_import_animations as import_animations
from os import getcwd

WIDTH, HEIGHT = (800, 600)

Player = Actor(f"{getcwd()}/images/character/up-idle/idle01")
Player.pos = (400, 300)
Player.scale = 8
Player.animations = import_animations("images/character/")
Player.speed = 1
Player.animation_speed = 0.3
Player.counter = 0
Player.direction = "up"
Player.animation_type = "idle"
Player.old_animation = "up-idle"



def update():
    if keyboard.up or keyboard.w:
        Player.direction = "up"
        Player.animation_type = "run"
        Player.y -= Player.speed
    elif keyboard.down or keyboard.s:
        Player.direction = "down"
        Player.animation_type = "run"
        Player.y += Player.speed
    else:
        Player.animation_type = "idle"
    '''
    elif keyboard.left or keyboard.a:
        Player.direction = "left"
        Player.animation_type = "run"
        Player.x -= Player.speed
    elif keyboard.right or keyboard.d:
        Player.direction = "right"
        Player.animation_type = "run"
        Player.x += Player.speed
    else:
        Player.animation_type = "idle"
    '''
    Player.animation_type = "idle"

    if Player.counter >= len(Player.animations[f"{Player.direction}-{Player.animation_type}"]):
        Player.counter = 0

    Player.new_animation = f"{Player.direction}-{Player.animation_type}"  
    if Player.new_animation != Player.old_animation:
        Player.counter = 0.7

    Player.old_animation = Player.new_animation
    Player.image = Player.animations[Player.new_animation][int(Player.counter)] 

        
def draw():
    screen.clear()
    update()
    Player.draw()

pgzrun.go()