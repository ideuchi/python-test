# coding utf-8

sys.path
sys.path.append('/usr/local/lib')

import numpy as np
from primitiv import *
from primitiv import devices as D
from primitiv import functions as F
from primitiv import initializers as I
from primitiv import optimizers as O

class Hoge:
	dev = d.Naive()
	Device.set_default(dev)
	g = Graph()
	Graph.set_default(g)

	def index(self):
		return True

	def primitiv_init(self):
		x = F.input(np.array([[1], [2], [3]]))
		y = 2 * x + 3
		return y.to_list()

