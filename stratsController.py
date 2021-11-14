import pygame

pygame.init()
joysticks = []
clock = pygame.time.Clock()
keepPlaying = True

# for al the connected joysticks
for i in range(0, pygame.joystick.get_count()):
    # create an Joystick object in our list
    joysticks.append(pygame.joystick.Joystick(i))
    # initialize them all (-1 means loop forever)
    joysticks[-1].init()
    # print a statement telling what the name of the controller is
    print (joysticks[-1].get_name())


while True:
    for event in pygame.event.get():
            if event.type == 1539:
                print("Joystick R2 button pressed.")