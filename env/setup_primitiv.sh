#!/bin/sh

CURDIR=`dirname $0`
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

# symlink header file
ln -s ${CURDIR}/primitiv-develop/primitiv/core/shape.h ${CURDIR}/primitiv-develop/primitiv/shape.h

# build Python3 primitiv
pip3 install numpy cython cmake scikit-build
unzip -qo primitiv-python-develop.zip
cd primitiv-python-develop
python3 ./setup.py build
sudo python3 ./setup.py install

return 0

