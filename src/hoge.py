# coding utf-8

import numpy as np
from primitiv import *
from primitiv import devices as D
from primitiv import functions as F
from primitiv import initializers as I
from primitiv import optimizers as O

class Hoge:
    def index(self):
        return True

    def primitiv_test1(self):
        dev = D.Naive()
        Device.set_default(dev)
        g = Graph()
        Graph.set_default(g)

        x = F.input(np.array([[1], [2], [3]]))
        y = 2 * x + 3
        return y.to_list()

    def primitiv_test2(self):
        dev = D.Naive()
        Device.set_default(dev)
        g = Graph()
        Graph.set_default(g)

        x = F.input(np.array([[1], [2]]))
        a = F.input(np.array([[1, 2], [1, 2]]))
        y = F.matmul(a, x)
        return y.to_list()

    def primitiv_xor_test(self):
        dev = D.Naive()
        Device.set_default(dev)
        g = Graph()
        Graph.set_default(g)

        input_data = [
        np.array([[ 1], [ 1]]),
        np.array([[-1], [ 1]]),
        np.array([[-1], [-1]]),
            np.array([[ 1], [-1]]),
        ]

        label_data = [
            np.array([ 1]),
            np.array([-1]),
            np.array([ 1]),
            np.array([-1]),
        ]

        N = 8
        pw = Parameter([1, N], I.XavierUniform())
        pb = Parameter([],     I.Constant(0))
        pu = Parameter([N, 2], I.XavierUniform())
        pc = Parameter([N],    I.Constant(0))

        optimizer = O.SGD(0.5)
        optimizer.add(pw, pb, pu, pc)

        for epoch in range(20):
            print(epoch, end=' ')

        g.clear()

        y = build_graph()
        for val in y.to_list():
            print('{:+.6f},'.format(val), end=' ')

            loss = calc_loss(y)
            print('loss={:.6f}'.format(loss.to_float()))

            optimizer.reset_gradients()
            loss.backward()
            optimizer.update()

        pw.save('pw.data')
        pb.save('pb.data')
        pu.save('pu.data')
        pc.save('pc.data')

        return y.to_list()

    def build_graph():
        x = F.input(input_data)
        w = F.parameter(pw)
        b = F.parameter(pb)
        u = F.parameter(pu)
        c = F.parameter(pc)
        h = F.tanh(u @ x + c)
        return F.tanh(w @ h + b)

    def calc_loss(y):
        t = F.input(label_data)
        diff = y - t
        return F.batch.mean(diff * diff)


