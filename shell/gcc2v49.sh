#!/bin/sh
sudo apt-get install gcc-4.9 g++-4.9 gfortran-4.9
sudo update-alternatives --install /usr/bin/gfortran gfortran /usr/bin/gfortran-4.9 100 
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.9 100 
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.9 100
gcc -v
