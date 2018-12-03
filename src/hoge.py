# coding utf-8

import numpy as np
from primitiv import *
from primitiv import devices as D
from primitiv import functions as F
from primitiv import initializers as I
from primitiv import optimizers as O

class Hoge:
	dev = D.Naive()
	Device.set_default(dev)
	g = Graph()
	Graph.set_default(g)

	def index(self):
		return True

	def primitiv_test1(self):
		x = F.input(np.array([[1], [2], [3]]))
		y = 2 * x + 3
		return y.to_list()

	def primitiv_test2(self):
		x = F.input(np.array([[1], [2]]))
		a = F.input(np.array([[1, 2], [1, 2]]))
		y = F.matmul(a, x)
		return y.to_list()


