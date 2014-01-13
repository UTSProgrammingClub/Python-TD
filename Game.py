import pygame

#----------- define all of the variables here -----------------------

xres = 480
yres = 320

window = pygame.display.set_mode((xres, yres))

# the game is to be done in states:

MENU = 0
LEVELS = 1
MAP = 2
SHOP = 3

screen = MENU # the game starts on the menu

# ---------- these will be the methods that run everything ----------

def draw():
	window.fill((0, 0, 0))
		
	pygame.display.flip()

def update():

	
def keyInput():


def mouseInput():


def event(e):


def run():
	while True:
		for e in pygame.event.get():
			event(e)
			
		keyInput()
		
		mouseInput()
		
		draw()
		
		move()
