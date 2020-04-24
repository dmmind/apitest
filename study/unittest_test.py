import unittest
import requests


class ArithmeticTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test01(self):
        """test01"""
        self.assertEqual(3, (2 + 1))

    def test02(self):
        """test02"""
        a = 'A'
        b = '哎'
        self.assertEqual(a, b, msg='失败原因：%s!=%s' % (a, b))
        self.assertEqual((7/2), 3)


if __name__ == '__main__':
    unittest.main()

