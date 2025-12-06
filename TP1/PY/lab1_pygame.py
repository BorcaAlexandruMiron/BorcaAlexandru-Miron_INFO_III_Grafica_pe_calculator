#!/usr/bin/env python3

import glfw
import numpy as np
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader

def main():
    if not glfw.init():
        return
    window = glfw.create_window(800,600,"Lab1 primul triunghi",None,None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)

    verts = np.array([
        0.0,0.5,0.0,
        -0.5,-0.5,0.0,
        0.5,-0.5,0.0
    ],dtype=np.float32)
    
    VAO = glGenVertexArrays(1)
    VBO = glGenBuffers(1)

    glBindVertexArray(VAO)
    glBindBuffer(GL_ARRAY_BUFFER,VBO)
    glBufferData(GL_ARRAY_BUFFER,verts.nbytes,verts,GL_STATIC_DRAW)

    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0,3,GL_FLOAT,GL_FALSE,0,ctypes.c_void_p(0))

    vertex_shader = """
    #version 330 core
    layout(location = 0) in vec3 position;

    void main()
    {
        gl_Position = vec4(position,1.0);
    }
    """
    
    fragment_shader = """
    #version 330 core
    out vec4 FragColor;

    void main()
    {
        FragColor = vec4(1.0,0.5,0.2,1.0);
    }
    """
    vShader = compileShader(vertex_shader,GL_VERTEX_SHADER)
    fShader = compileShader(fragment_shader,GL_FRAGMENT_SHADER)

    program = glCreateProgram()
    glAttachShader(program,vShader)
    glAttachShader(program,fShader)
    glLinkProgram(program)

    

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(program)
        glBindVertexArray(VAO)
        glDrawArrays(GL_TRIANGLES,0,3)
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
