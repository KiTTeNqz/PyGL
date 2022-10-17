import math

import pygame
import random
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def quadWhite():
    glBegin(GL_QUADS)
    glVertex2f(-0.6, -0.5)
    glVertex2f(-0.6, 0.5)
    glVertex2f(0.6, 0.5)
    glVertex2f(0.6, -0.5)
    glEnd()

def quadBlue1():
    glBegin(GL_QUADS)
    glVertex2f(-0.6, 0.4)
    glVertex2f(-0.6, 0.25)
    glVertex2f(0.6, 0.25)
    glVertex2f(0.6, 0.4)
    glEnd()

def quadBlue2():
    glBegin(GL_QUADS);
    glVertex2f(-0.6, -0.4)
    glVertex2f(-0.6, -0.25)
    glVertex2f(0.6, -0.25)
    glVertex2f(0.6, -0.4)
    glEnd()

def triangle1():

    glBegin(GL_TRIANGLES)
    glVertex2f(-0.1, -0.05)
    glVertex2f(0.1, -0.05)
    glVertex2f(0, 0.17)
    glEnd()

def triangle2():
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.1, 0.1)
    glVertex2f(0.1, 0.1)
    glVertex2f(0, -0.12)
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glEnable(GL_LINE_SMOOTH);
        glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
        glEnable(GL_BLEND);
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

        glColor3f(1.0, 1.0, 1.0)
        quadWhite()
        glColor3f(0.0, 0.0, 1.0)
        quadBlue1()
        quadBlue2()

        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        glLineWidth(7);
        glColor3f(0.0, 0.0, 1.0)

        triangle1()
        triangle2()

        pygame.display.flip()
        pygame.time.wait(10)

main()
