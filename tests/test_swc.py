# -*- coding: utf-8 -*-

import unittest
import pyswc


class TestSwc(unittest.TestCase):
    def setUp(self):
        self.swc = pyswc.Swc()

    def test_read_file(self):
        pass


if __name__ == '__main__':
    unittest.main()
