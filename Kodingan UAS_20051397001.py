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
#Menginisialisasi window untuk ditampilkan
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
#Mengatur nama tampilan window
pygame.display.set_caption("Diamond")
#Mengatur perspektif
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
#Melakukan translasi
glTranslate(0, 0, -5)

while True:
    #Event loop
    for event in pygame.event.get():
        #Event saat tombol exit diklik
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    #Melakukan rotasi
    glRotate(1, 4, 3, 2)
    #Membersihkan window dan buffer kedalaman
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    draw_diamond()

    #Mengupdate tampilan
    pygame.display.flip()
    #Lama looping
    pygame.time.wait(10)