#!/bin/sh

cd `dirname $0`

# build C++ primitiv
unzip -qo primitiv-develop.zip
cd primitiv-develop
mkdir build
cd build
cmake ..
make
sudo make install

# build Python3 primitiv
pip3 install numpy cython cmake scikit-build
unzip -qo primitiv-python-develop.zip
cd primitiv-python-develop
python3 ./setup.py build
sudo python3 ./setup.py install

return 0

