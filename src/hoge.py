# coding utf-8

import os
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

    def calc_loss(self, y, label_data):
        t = F.input(label_data)
        diff = y - t
        return F.batch.mean(diff * diff)

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
        if os.path.isfile('output/xor/pw.data') and os.path.isfile('output/xor/pb.data') and os.path.isfile('output/xor/pu.data') and os.path.isfile('output/xor/pc.data'):
            pw.load('output/xor/pw.data')
            pb.load('output/xor/pb.data')
            pu.load('output/xor/pu.data')
            pc.load('output/xor/pc.data')

        optimizer = O.SGD(0.5)
        optimizer.add(pw, pb, pu, pc)

        for epoch in range(50):
            print(epoch, end=' ')

            g.clear()

            x = F.input(input_data)
            w = F.parameter(pw)
            b = F.parameter(pb)
            u = F.parameter(pu)
            c = F.parameter(pc)
            h = F.tanh(u @ x + c)
            y = F.tanh(w @ h + b)

            for val in y.to_list():
                print('{:+.6f},'.format(val), end=' ')

            loss = self.calc_loss(y, label_data)
            print('loss={:.6f}'.format(loss.to_float()))

            optimizer.reset_gradients()
            loss.backward()
            optimizer.update()

        pw.save('output/xor/pw.data')
        pb.save('output/xor/pb.data')
        pu.save('output/xor/pu.data')
        pc.save('output/xor/pc.data')

        return y.to_list()

