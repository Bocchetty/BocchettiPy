import pgzrun
from pgzero.builtins import Actor, animate, keyboard

alien = Actor('alien')

RED = 150, 0, 0
GREEN = 0, 128, 0
bg = RED

WIDTH = 800
HEIGHT = 600

score= 0

def draw():
    screen.clear()
    screen.fill(bg)
    alien.draw()

def on_mouse_down(pos):
    global score
    if alien.collidepoint(pos):
        set_alien_hit()
        score += 1
        print("Eek")
    else:
        print("Nothing here")
    print(score)

def set_alien_hit():
    alien.image = 'alien_hurt'
    #sounds.eep.play()
    clock.schedule_unique(set_alien_normal, 0.5)
 
def set_alien_normal():
    alien.image = "alien"

animate(alien,tween='linear',on_finished=None,duration=3, pos=(300,100))

pgzrun.go()