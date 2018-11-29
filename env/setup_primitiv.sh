#!/bin/sh

CURDIR=`dirname $0`
echo "current dir = " ${CURDIR}
cd ${CURDIR}

# build C++ primitiv
unzip -qo primitiv-develop.zip
cd primitiv-develop
mkdir build
cd build
cmake ..
make
sudo make install
cd ../..

# create symlink shape header file
sudo ln -s /usr/local/include/primitiv/core/shape.h /usr/local/include/primitiv/shape.h
sudo ln -s /usr/local/include/primitiv/core/device.h /usr/local/include/primitiv/device.h

# build Python3 primitiv
pip3 install numpy cython cmake scikit-build
unzip -qo primitiv-python-develop.zip
cd primitiv-python-develop
python3 ./setup.py build
sudo python3 ./setup.py install

return 0

