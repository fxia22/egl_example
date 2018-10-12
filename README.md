# egl_example
Creating an EGL + OpenGL context using glad, dynamically loading the libraries, for headless rendering in the cloud (for example using Ubuntu 16.04 without X11)

# python example
a python EGL + OpenGL context example, from [lucid](https://github.com/tensorflow/lucid). 

## build and run ##
```
sudo apt install libx11-dev
mkdir build
cd build
cmake ..
make 
./main
```

Example output:
~~~~~~~~~~
number of devices found 1
Loaded EGL 1.4 after reload.
GL_VENDOR=NVIDIA Corporation
GL_RENDERER=TITAN Xp/PCIe/SSE2
GL_VERSION=4.6.0 NVIDIA 396.51
GL_SHADING_LANGUAGE_VERSION=4.60 NVIDIA
~~~~~~~~~~
