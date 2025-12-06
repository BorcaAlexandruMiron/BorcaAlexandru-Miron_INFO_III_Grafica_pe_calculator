# This is the CPP version of TP1 
>[!IMPORTANT]
> # the following dependencies are necessary:  
> * glfw  
> * glew
> * CMake > (3.28.0)

# Building the project with CMake:

create build directory in the project and change directory to build:
```bash
mkdir build && cd build 
```
Generate build files from CMakeLists:
```bash
cmake ..
```
Build the project in the current directory (you can use the parallel tag to optimize the build time):
```bash
cmake --build . --parallel
```

>[!TIP]
> # Book recommendation:  
> * Computer Graphics Programming in OpenGL Using C++, 3rd Edition (Gordon PhD, V. Scott, Clevenger PhD, John L.)
