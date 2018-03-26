import pygame
import colorsys
import math

def function(_x,_y,og=False):
	x = map(_x,[0,backgroundSize[0]/2],[-scale,scale])
	y = map(_y,[0,backgroundSize[1]],[-scale,scale])
	if not og:
		#Edit here for different equations
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		z = complex(x,y)
		z = z**5 - x + 1
		x,y = z.real,z.imag
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		return x,y
	else:
		return x,y

def map(value,changed,og):
	return (value-changed[0])*(float(og[1]-og[0])/float(changed[1]-changed[0]))+og[0]

def get_hsv(_x,_y):
	h=map((math.atan2((_y),(_x)))%(2*math.pi)-math.pi+rota,[-r,r],[0,360])
	return 255,h

scale = 10
backgroundSize = [1800,900]

pygame.init()
WHITE= [255, 255, 255]
MID = [backgroundSize[0]/2,backgroundSize[1]/2]
screen = pygame.display.set_mode(backgroundSize)
pygame.display.set_caption("Solveing 2D equations using color")
clock = pygame.time.Clock()
done = False
r = 1130
rota = 1-math.pi/2

for x in xrange(backgroundSize[0]/2):
	for y in xrange(backgroundSize[1]):
		
		temp = function(x,y,True)
		v,h = get_hsv(temp[0],temp[1])
		screen.set_at((x,y),colorsys.hsv_to_rgb(h,1,v))
	
		temp = function(x,y)
		v,h = get_hsv(temp[0],temp[1])
		screen.set_at((x+MID[0],y),colorsys.hsv_to_rgb(h,1,v))

print "Done!"
finished = screen.copy()

done = True
while done:	
	pygame.Surface.blit(screen,finished,[0,0])
	temp = pygame.mouse.get_pos()
	z = function(min(temp[0]-MID[0],MID[0]),temp[1])

	try:
		pygame.draw.circle(screen,WHITE,[int(z[0]+MID[0]/2),int(z[1]+MID[1])],5,1)
		pygame.display.flip()
	except:
		pass

	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
			done =False

	