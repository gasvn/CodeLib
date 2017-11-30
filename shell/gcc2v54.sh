#!/bin/sh
sudo apt-get install gcc-5 g++-5
sudo ln -s /usr/bin/gcc-5 /usr/bin/gcc -f
sudo ln -s /usr/bin/g++-5 /usr/bin/g++ -f
gcc -v
