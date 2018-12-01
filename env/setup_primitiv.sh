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
sudo ln -s /usr/local/include/primitiv/core/tensor.h /usr/local/include/primitiv/tensor.h
sudo ln -s /usr/local/include/primitiv/core/graph.h /usr/local/include/primitiv/graph.h
sudo ln -s /usr/local/include/primitiv/core/initializer.h /usr/local/include/primitiv/initializer.h
sudo ln -s /usr/local/include/primitiv/core/parameter.h /usr/local/include/primitiv/parameter.h
sudo ln -s /usr/local/include/primitiv/core/functions.h /usr/local/include/primitiv/functions.h
sudo ln -s /usr/local/include/primitiv/devices/naive/device.h /usr/local/include/primitiv/naive_device.h
sudo ln -s /usr/local/include/primitiv/core/initializer_impl.h /usr/local/include/primitiv/initializer_impl.h
sudo ln -s /usr/local/include/primitiv/core/model.h /usr/local/include/primitiv/model.h
sudo ln -s /usr/local/include/primitiv/core/optimizer.h /usr/local/include/primitiv/optimizer.h
sudo ln -s /usr/local/include/primitiv/core/optimizer_impl.h /usr/local/include/primitiv/optimizer_impl.h

# build Python3 primitiv
pip3 install numpy cython cmake scikit-build
pip3 install --upgrade setuptools
unzip -qo primitiv-python-develop.zip
cd primitiv-python-develop
sed -i -e "s/\*args, \*\*kwargs,/\*args,/g" setup.py
sed -i -e 's/extra_compile_args=\["-std=c++11"\],/extra_compile_args=\["-std=c++11"\], \*\*kwargs/g' setup.py
sed -i -e 's/setup_kwargs,/setup_kwargs/g' setup.py
python3 ./setup.py build
echo "=====build end.====="
sudo python3 ./setup.py install
echo "=====install end.====="

return 0

