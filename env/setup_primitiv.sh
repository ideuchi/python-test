# build C++ primitiv
unzip primitiv-develop.zip
cd primitiv-develop
mkdir build
cd build
cmake ..
make
make install

# build Python3 primitiv
pip3 install numpy cython cmake scikit-build
unzip primitiv-python-develop.zip
cd primitiv-python-develop
python3 ./setup.py build
python3 ./setup.py install

return 0

