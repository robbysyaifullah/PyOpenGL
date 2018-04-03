from OpenGLContext import testingcontext
BaseContext = testingcontext.getInteractive()

import logging
logging.basicConfig()

from random import *
from OpenGL.GL import *
from OpenGL.arrays import vbo
from OpenGLContext.arrays import *
from OpenGL.GL import shaders
import math
import time

PI = 3.141592653589793238


class TestContext( BaseContext ):
    
    def OnInit( self ):
        try:
            shaders.compileShader("""
            void main() {""", GL_VERTEX_SHADER)
        except (GLError, RuntimeError) as err:
            print 'Example of shader compile error', err
        else:
            raise RuntimeError("""Didn't catch compilation error!""")
        
        vertex = shaders.compileShader(
        """
        varying vec4 vertex_color;
        void main(){
            gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
            vertex_color = gl_Color;
        }""", GL_VERTEX_SHADER)
        
        fragment = shaders.compileShader("""
        varying vec4 vertex_color;
        void main(){
            gl_FragColor = vertex_color;
        }""", GL_FRAGMENT_SHADER)
        self.shader = shaders.compileProgram(vertex, fragment)
        
        in_file = open("in.txt", "r");
        temp_car = [[float(x) for x in y.split(" ")] for y in ((in_file.read()).split("\n"))]
        in_file.close()

        for i in temp_car:
            i.append(0)
            i.append(randint(0,1))
            i.append(randint(0,1))
            i.append(randint(0,1))
            i[0] = (i[0]/1000 * 20) - 10
            i[1] = (i[1]/500 * 20) - 10
        
        print temp_car
        self.vbo = vbo.VBO(
            array(temp_car, 'f' )
        )

    def OnIdle(self,):
        self.triggerRedraw(1)
        return 1
    
    def draw_circle(self, x, y, radius, smoothness):
        #glRotatef(40.0, 0.0, 0.0, 1.0)
        #glScalef(2.0, 2.0, 2.0)
        radius = 1
        smoothness = 24
        c = smoothness / 4
        i = 0
        glPushMatrix()
        glTranslatef(x,y,0.0)
        glRotatef( time.time()%(3.0) * 360, 0,0,1)
        glTranslatef(-x,-y,0.0)
        while (i < (2 * PI)):
            temp = i
            i = i + (PI / smoothness)
            glColor3f(0.6, 0.5, 0.2)
            if (c == 1):
                glColor3f(1.0, 0.8, 0.3)    
            glBegin(GL_TRIANGLES)
            glVertex2f(x,y)
            glVertex2f(x + cos(temp) * radius, y + sin(temp) * radius)
            glVertex2f(x + cos(i) * radius, y + sin(i) * radius)
            glEnd()
            
            c = c - 1
            if (c < 0):
                c = smoothness / 4
                
        glPopMatrix()

    def Render( self, mode ):
        '''
        render the scene geometry
        '''
        BaseContext.Render(self, mode)
        glUseProgram( self.shader )
        try:
            self.vbo.bind()
            try:
                glEnableClientState( GL_VERTEX_ARRAY )
                glEnableClientState( GL_COLOR_ARRAY)

                glVertexPointer( 3, GL_FLOAT, 24, self.vbo )
                glColorPointer( 3, GL_FLOAT, 24, self.vbo + 12 )
                self.draw_circle(3.8,-3.4,6,1.0)
                self.draw_circle(1.5,0.0,6,1.0)
                glDrawArrays( GL_POLYGON, 0, 9 )
            finally:
                self.vbo.unbind()
                glDisableClientState( GL_VERTEX_ARRAY )
                glDisableClientState( GL_COLOR_ARRAY )

        finally:
            glUseProgram( 0 )


if __name__ == "__main__":
    TestContext.ContextMainLoop()

