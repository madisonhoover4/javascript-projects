import pygame
 
# colors
black = (0, 0, 0)
white = (255, 255, 255)
bue = (50, 50, 255)
 
# screen dimensions
width = 800
height = 600

# initialize the game and set the screen
pygame.init();
screen = pygame.display.set_mode([width, height])

# give the window a title
pygame.display.set_caption('Madison"s Game')

surface = pygame.image.load('background.jpg').convert()
pygame.display.update()


clock = pygame.time.Clock()

clock.tick(60)
