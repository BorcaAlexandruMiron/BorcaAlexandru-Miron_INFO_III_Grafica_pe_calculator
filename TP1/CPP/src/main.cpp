#include <GL/glew.h>
#include <GLFW/glfw3.h>
#include <cstddef>
#include <cstdlib>
#include <iostream>

#define numberOfVAOs 1

GLuint renderingProgram;
GLuint vao[numberOfVAOs];

GLuint createShaderProgram() {
  const char *vertex_shader =
      "#version 330 core\n"
      "void main(){\n"
      "if(gl_VertexID == 0) gl_Position = vec4(0.0,0.5,0.0,1.0);\n"
      "else if(gl_VertexID == 1) gl_Position = vec4(-0.5,-0.5,0.0,1.0);\n"
      "else gl_Position = vec4(0.5,-0.5,0.0,1.0);}";

  const char *fragment_shader = "#version 330 core\n"
                                "out vec4 FragColor;\n"
                                "void main()\n"
                                "{FragColor=vec4(1.0,0.5,0.2,1.0);}";
  GLuint vShader = glCreateShader(GL_VERTEX_SHADER);
  GLuint fShader = glCreateShader(GL_FRAGMENT_SHADER);

  glShaderSource(vShader, 1, &vertex_shader, NULL);
  glShaderSource(fShader, 1, &fragment_shader, NULL);

  glCompileShader(vShader);
  glCompileShader(fShader);

  GLuint Vertex_Fragment = glCreateProgram();
  glAttachShader(Vertex_Fragment, vShader);
  glAttachShader(Vertex_Fragment, fShader);

  glLinkProgram(Vertex_Fragment);

  return Vertex_Fragment;
}

void init(GLFWwindow *window) {
  renderingProgram = createShaderProgram();
  glGenVertexArrays(numberOfVAOs, vao);
  glBindVertexArray(vao[0]);
}
void display(GLFWwindow *window, double time) {
  // glClearColor(1, 0, 0, 1);
  // glClear(GL_COLOR_BUFFER_BIT);
  glPointSize(30.0f);
  glUseProgram(renderingProgram);
  glDrawArrays(GL_TRIANGLES, 0, 3);
}

int main(void) {
  if (!glfwInit()) {
    exit(EXIT_FAILURE);
  }

  glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 4);
  glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);

  GLFWwindow *window = glfwCreateWindow(800, 600, "TP1", NULL, NULL);
  glfwMakeContextCurrent(window);

  if (glewInit() != GLEW_OK) {
    exit(EXIT_FAILURE);
  }
  glfwSwapInterval(1);
  init(window);

  while (!glfwWindowShouldClose(window)) {
    display(window, glfwGetTime());
    glfwSwapBuffers(window);
    glfwPollEvents();
  }
  glfwDestroyWindow(window);
  glfwTerminate();
  exit(EXIT_SUCCESS);
}
