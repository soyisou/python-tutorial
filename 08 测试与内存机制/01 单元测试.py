# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
单元测试
'''
import unittest
from  unittest import TestCase


class TestStringMethonds(unittest, TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaise(TypeError):
            s.split('')