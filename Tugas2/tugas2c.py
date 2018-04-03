from OpenGLContext import testingcontext
BaseContext = testingcontext.getInteractive()

import logging
logging.basicConfig()

from OpenGL.GL import *
from OpenGL.arrays import vbo
from OpenGLContext.arrays import *
from OpenGL.GL import shaders
import math
import time

PI = 3.1415926535897932384626433832795

class TestContext(BaseContext):
    """Creates a simple vertex shader..."""
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
        
        self.vbo = vbo.VBO(
            array([
                 [ 4,0,0, 1,1,1],
                 [ 4,2, 0, 1,1,1 ], 
                 [ 3,2,0, 1,1,1],
                 [ 3,3,0, 1,1,1],
                 [ -2,3,0, 1,1,1],
                 [ -3,2,0, 1,1,1],
                 [ -4,2, 0, 1,1,1 ], 
                 [ -4.5,0, 0, 0,0,1 ]
            ],'f')
        )
        
    def OnIdle(self,):
        """Request refresgh of the context whenecer idle"""
        self.triggerRedraw(1)
        return 1
        
    def drawCircle(self, x, y, smoothness, radius):
        #x = -1.0
        #y = 0.0
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
            glColor3f(1.0, 0.0, 0.0)
            if (c == 1):
                glColor3f(0.0, 0.0, 1.0)    
            glBegin(GL_TRIANGLES)
            glVertex2f(x,y)
            glVertex2f(x + cos(temp) * radius, y + sin(temp) * radius)
            glVertex2f(x + cos(i) * radius, y + sin(i) * radius)
            glEnd()
            
            c = c - 1
            if (c < 0):
                c = smoothness / 4
                
        glPopMatrix()
        
    def Render( self, mode):
        BaseContext.Render(self, mode)
        glUseProgram(self.shader)
        try:
            self.vbo.bind()
            try:
                glEnableClientState(GL_VERTEX_ARRAY);
                glEnableClientState(GL_COLOR_ARRAY);
                glVertexPointer(3, GL_FLOAT, 24, self.vbo)
                glColorPointer(3, GL_FLOAT, 24, self.vbo+12)
                #glDrawArrays(GL_TRIANGLES, 3, 3)
                #glRotated( time.time()%(3.0) * 360, 0,0,1)
                #glDrawArrays(GL_TRIANGLES, 0, 3)
                #glLoadIdentity()
                #glTranslatef(-2.0,1.0,0.0)
                #glRotatef( time.time()%(3.0)/3 * 360, 0,0,1)
                #glTranslatef(2.0,-1.0,0.0)
                self.drawCircle(-2.0,0.0,6,1.0)
                #glLoadIdentity()
                #glTranslatef(2.0,1.0,0.0)
                #glRotatef( time.time()%(3.0)/3 * 360, 0,0,1)
                #glTranslatef(-2.0,-1.0,0.0)
                self.drawCircle(2.0,0.0,6,1.0)
                #self.drawCircle(2.0,0.0,6,1.0)
                #self.drawCircle(1,0,6,1.0)
                glDrawArrays(GL_POLYGON, 0, 8)
            finally:
                self.vbo.unbind()
                glDisableClientState(GL_VERTEX_ARRAY);
                glDisableClientState(GL_COLOR_ARRAY);
        finally:
            glUseProgram( 0 )

if __name__ == "__main__":
    TestContext.ContextMainLoop()
