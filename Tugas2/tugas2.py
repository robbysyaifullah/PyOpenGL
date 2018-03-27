from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

window = 0                                             # glut window number
width, height = 1280, 720                               # window size
PI = 3.141592653589793238462643383279502884197169399
rot = 0
interval = 100

def draw_car():
    glBegin(GL_POLYGON) 
                                     # start drawing a rectangle
    glVertex2f(775, 100)
    glVertex2f(825, 120)
    glVertex2f(855, 175)
    glVertex2f(750, 250)
    glVertex2f(680, 235)
    glVertex2f(670, 270)
    glVertex2f(595, 310)
    glVertex2f(520, 315)
    glVertex2f(475, 300)
    glVertex2f(400, 250)
    glVertex2f(100, 175)
    glVertex2f(80, 150)
    glVertex2f(100, 120)
    glVertex2f(100, 120)    
    glVertex2f(100, 100)  
    
    glEnd()                                            # done drawing a rectangle 

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def draw_circle(x, y, radius, smoothness):
    #glRotatef(40.0, 0.0, 0.0, 1.0)
    #glScalef(2.0, 2.0, 2.0)
    glBegin(GL_POLYGON)
    colorUpdate =1
    i = rot
    while (i < 2 * PI):
        glColor3f(0.6, 0.5, 0.2)
        if (colorUpdate == 1):
            glColor3f(1.0, 0.8, 0.3)
        glVertex2f(x + cos(i) * radius, y + sin(i) * radius)
        i = i + (PI / smoothness)
        colorUpdate = colorUpdate * -1
    glEnd()

def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position  
    refresh2d(width, height)                           # set mode to 2d

    # ToDo draw rectangle
    glColor3f(0.0, 0.0, 1.0)  
    draw_car()
    draw_circle(300, 100, 50, 4)
    draw_circle(700, 100, 50, 4)
    
    glutSwapBuffers()                                  # important for double buffering   

def rotate(value):                                     # rotate tire
    global rot
   
    glPushMatrix()
    rot = rot - 1
    glPopMatrix()
    glutTimerFunc(interval, rotate, 0)


# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow("noobtuts.com")              # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
glutTimerFunc(interval, rotate, 0)
glutMainLoop()                                         # start everything