from pygame import *

clock = time.Clock()
FPS = 60

window = display.set_mode((700, 500))
display.set_caption("Доганялки")
background = transform.scale(image.load("background.png"), (700, 500))

sprite1 = transform.scale(
    image.load("sprite1.png"),(100, 100))

sprite2 = transform.scale(
    image.load("sprite2.png"),(100, 100))

game = True
while game:
    window.blit(background, (0, 0))
    window.blit(sprite1, (100, 100))
    window.blit(sprite2, (200, 200))

    keys_preesed = key.get_pressed()

    for e in event.get():
        if e.type == QUIT:
            game = False



    
    display.update()
    clock.tick(FPS)



