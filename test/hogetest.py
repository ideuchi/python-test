# coding:utf-8

import unittest
from hoge import Hoge

class HogeTest(unittest.TestCase):

    def SetUp(self):
        print('setup')

    def test_first(self):
        print('test_first')

    def test_hoge(self):
        hoge = Hoge()
        self.assertTrue(hoge.index())
        self.assertEqual(hoge.primitiv_test1(), [5.0, 7.0, 9.0])
        self.assertEqual(hoge.primitiv_test2(), [5.0, 5.0])
        self.assertTrue(len(hoge.primitiv_xor_test()) == 4)
        self.assertLess(hoge.primitiv_xor_test(), 1.5)

def suite():
	suite = unittest.TestSuite()
	suite.addTests(unittest.makeSuite(HogeTest))
	return suite

