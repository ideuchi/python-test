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
		self.assertEqual(hoge.primitiv_init(), [5.0, 7.0, 9.0])

def suite():
	suite = unittest.TestSuite()
	suite.addTests(unittest.makeSuite(HogeTest))
	return suite

