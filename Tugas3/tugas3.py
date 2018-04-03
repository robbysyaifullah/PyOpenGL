import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *

PI = 3.1415926535897932384626433832795
rot = 0
			
def Cyl(x, y, z, length, radius, smoothness):
	global rot
	c = 6 / 4
	i = rot
	
	while ( i < (2 * PI) + rot):
		temp = i
		i = i + (PI / 12)
		glColor4f(0.0, 0.0, 0.0, 1.0)
		if (c == 1):
			glColor4f(0.8, 0.8, 1.0, 1.0)
			
		glBegin(GL_TRIANGLES)
		glVertex3f(x, y, z)
		glVertex3f(x + cos(temp) * radius, y + sin(temp) * radius, z)
		glVertex3f(x + cos(i) * radius,y + sin(i) * radius, z)
		glEnd()
		
		glBegin(GL_TRIANGLES)
		glVertex3f(x, y, z + length)
		glVertex3f(x + cos(temp) * radius, y + sin(temp) * radius, z + length)
		glVertex3f(x + cos(i) * radius, y + sin(i) * radius, z + length)
		glEnd()
		
		glColor4f(1.0, 1.0, 1.0, 1.0)
		glBegin(GL_QUADS)
		glVertex3f(x + cos(temp) * radius, y + sin(temp) * radius, z)
		glVertex3f(x + cos(i) * radius, y + sin(i) * radius, z)
		glVertex3f(x + cos(i) * radius, y + sin(i) * radius, z + length)
		glVertex3f(x + cos(temp) * radius, y + sin(temp) * radius, z + length)
		glEnd()
		
		c = c - 1
		if ( c < 0):
			c = 12/4
		
	#glPopMatrix()
			
def drawParts(x0, y0, z0, x1, y1, z1, x2, y2, z2, x3, y3, z3):
	glBegin(GL_QUADS)
	glVertex3f(x0, y0, z0)
	glVertex3f(x1, y1, z1)
	glVertex3f(x2, y2, z2)
	glVertex3f(x3, y3, z3)
	glEnd()
	
def main():
	
    global rot
    pygame.init()
    display = (1000,800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    glEnable(GL_BLEND)
    glEnable(GL_DEPTH_TEST)
    
    glDepthFunc(GL_LESS)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0,0, -20)

    glRotatef(25, 2, 1, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    #glTranslatef(-0.5,0,0)
                    glRotatef(10, 1, 1, 1)
                if event.key == pygame.K_RIGHT:
                    #glTranslatef(0.5,0,0)
                    glRotatef(-10, 1, 1, 1)

                if event.key == pygame.K_UP:
                    glTranslatef(0,1,0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0,-1,0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 5:
                    glRotatef(10,1,0,0)

                if event.button == 4:
                    glRotatef(-10,1,0,0)
                    
                if event.button == 1:
                    glRotatef(10, 0,0,1)
                
                if event.button == 3:
                    glRotatef(-10, 0,0,1)

        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        glColor3f(0.9,0.1,0.1)
        drawParts(-0.9, 0.2, 0.4, 
			 2.0, 0.2, 0.4, 
			 2.0, 2.0, 0.4, 
			 -0.9, 1.7, 0.4)
        
        drawParts(-0.9, 0.2, 3.9, 
			 2.0, 0.2, 3.9, 
			 2.0, 2.0, 3.9, 
			 -0.9, 1.7, 3.9)

        drawParts(3.3, 3.3, 0.4, 
			 2.0, 2.0, 0.4, 
			 2.0, 0.2, 0.4, 
			 3.3, 0.2, 0.4)
        
        drawParts(3.3, 3.3, 3.9, 
			 2.0, 2.0, 3.9, 
			 2.0, 0.2, 3.9, 
			 3.3, 0.2, 3.9)

        glColor3f(0.9,0.2,0.1)
        drawParts(3.3, 3.3, 0.4, 
			 3.3, 0.2, 0.4, 
			 6.6, 0.2, 0.4, 
			 6.6, 3.3, 0.4)

        drawParts(3.3, 3.3, 3.9, 
			 3.3, 0.2, 3.9, 
			 6.6, 0.2, 3.9, 
			 6.6, 3.3, 3.9)

        glColor3f(0.9,0.9,0.1)
        drawParts(7, 2.0, 0.4, 
			 7, 1.0, 0.4, 
			 6.6, 0.2, 0.4, 
			 6.6, 3.3, 0.4)

        drawParts(7, 2.0, 3.9, 
			 7, 1.0, 3.9, 
			 6.6, 0.2, 3.9, 
			 6.6, 3.3, 3.9)

# atap
        glColor3f(0.3,0.3,0.3)
        drawParts(-0.9, 0.2, 0.4, 
			 -0.9, 1.7, 0.4, 
			 -0.9, 1.7, 3.9, 
			 -0.9, 0.2, 3.9)

        glColor3f(0.3,0.9,0.3)
        drawParts(2, 2, 0.4, 
			 -0.9, 1.7, 0.4, 
			 -0.9, 1.7, 3.9, 
			 2, 2, 3.9)

        glColor3f(0.3,0.9,0.3)
        drawParts(2, 2, 0.4, 
			 3.3, 3.3, 0.4, 
			 3.3, 3.3, 3.9, 
			 2, 2, 3.9)

        glColor3f(0.3,0.9,0.3)
        drawParts(6.6, 3.3, 0.4, 
			 3.3, 3.3, 0.4, 
			 3.3, 3.3, 3.9, 
			 6.6, 3.3, 3.9)

        glColor3f(0.8,0.9,0.3)
        drawParts(7, 3, 0.4, 
			 6.6, 3.3, 0.4, 
			 6.6, 3.3, 3.9, 
			 7, 3, 3.9)

        glColor3f(0.8,0.9,0.3)
        drawParts(7, 2, 0.4, 
			 6.6, 3.3, 0.4, 
			 6.6, 3.3, 3.9, 
			 7, 2, 3.9)

        glColor3f(0,0.9,0.3)
        drawParts(7, 2, 0.4, 
			 7, 1, 0.4, 
			 7, 1, 3.9, 
			 7, 2, 3.9)

        glColor3f(0,0.9,0.3)
        drawParts(6.6, 0.2, 0.4, 
			 7, 1, 0.4, 
			 7, 1, 3.9, 
			 6.6, 0.2, 3.9)

        #glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        
        glRotatef(1, 0, 0, 1)
        Cyl(1.0, 0.6, 0.0, 0.3, 0.8, 12)
        Cyl(1.0, 0.6, 4.0, 0.3, 0.8, 12)
        Cyl(1.0, 0.6, 0.3, 3.7, 0.1, 12)
        glPopMatrix()
        
        glPushMatrix()
        glRotatef(1, 0, 0, 1)
        Cyl(6.0, 0.6, 0.0, 0.3, 0.8, 12)
        Cyl(6.0, 0.6, 4.0, 0.3, 0.8, 12)
        Cyl(6.0, 0.6, 0.3, 3.7, 0.1, 12)	
        glPopMatrix()
		
        #draw_circle(0.0, 0.0, 0.5, 12)
        #draw_tube()
        rot = rot - 1
        
        pygame.display.flip()
        pygame.time.wait(0)
		
main()
