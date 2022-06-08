#Import library
import pygame
from pygame.locals import*
from OpenGL.GL import*
from OpenGL.GLU import*

#Menggambar diamond
def draw_diamond():
    glBegin(GL_TRIANGLES)

    glColor(0.5, 0.5, 0.5)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.0, 0.5, 0.0)

    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.0, 0.5, 0.0)

    glColor(0.5, 0, 1)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.0, 0.5, 0.0)

    glColor(1, 0, 1)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(0.0, 0.5, 0.0)

    #
    glColor(0, 0, 1)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.0, -1.5, 0.0)

    glColor(0, 1, 0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.0, -1.5, 0.0)

    glColor(0, 1, 5)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.0, -1.5, 0.0)

    glColor(0.1, 0.4, 0.5)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(0.0, -1.5, 0.0)

    glEnd()

#Mendeklarasikan objek
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
pygame.display.set_caption("3D Diamond")
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glTranslate(0, 0, 0-5)

while True:
    #event loop
    for event in pygame.event.get():
        #event saat tombol exit diklik
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    glRotate(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    draw_diamond()

    #Update the sceen
    pygame.display.flip()
    #Lama looping
    pygame.time.wait(10)