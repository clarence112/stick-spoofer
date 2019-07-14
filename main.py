true = True

import sys
try:
    import pygame
except:
    print("Please install pygame!")
    quit()

def setup():

    global screen
    size = width, height = 867, 100
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Stick Spoofer")

    global tosay
    try:
        tosay = sys.argv[1]
    except:
        tosay = "Run the spoofer with 'pyhton main.py " + '"Your message here"' + "'"

def main():
    pygame.init()

    screen.blit(pygame.image.load("stick.png"), (0, 0))
    font = pygame.font.Font("OpenSans-Regular.ttf", 13)
    screen.blit(font.render(tosay, true, [255, 255, 255]), (85, 45))

    pygame.display.flip()

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                quit()

setup()
main()