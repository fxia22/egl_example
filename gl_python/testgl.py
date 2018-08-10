from __future__ import absolute_import, division, print_function

import os

import numpy as np

WIDTH, HEIGHT = 100, 100


import glcontext

import OpenGL.GL as gl
import glrenderer
import matplotlib.pyplot as plt

import time



glcontext.create_opengl_context((WIDTH, HEIGHT))
print(gl.glGetString(gl.GL_VERSION))
start = time.time()

for i in range(10000):
	gl.glClear(gl.GL_COLOR_BUFFER_BIT)
	gl.glBegin(gl.GL_TRIANGLES)
	gl.glColor3f(1, 0, 0)
	gl.glVertex2f(0,  1)

	gl.glColor3f(0, 1, 0)
	gl.glVertex2f(-1, -1)

	gl.glColor3f(0, 0, 1)
	gl.glVertex2f(1, -1)
	gl.glEnd()

dt = time.time()-start
print("{} trangles per sec".format(10000/dt))
# Read result
img_buf = gl.glReadPixels(0, 0, WIDTH, HEIGHT, gl.GL_RGB, gl.GL_UNSIGNED_BYTE)
img = np.frombuffer(img_buf, np.uint8).reshape(HEIGHT, WIDTH, 3)[::-1]

assert all(img[0, 0] == 0)  # black corner
assert all(img[0,-1] == 0)  # black corner
assert img[10, WIDTH//2].argmax() == 0  # red corner
assert img[-1,  10].argmax() == 1  # green corner
assert img[-1, -10].argmax() == 2  # blue corner
