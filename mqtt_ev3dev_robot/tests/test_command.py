# -*- coding: utf-8 -*-


import unittest
from .context import mqtt_ev3dev as api


class Caller:
    def foo(self):
        print('foo')

    def one(self, arg1):
        print('one')

    def two(self, arg1, arg2):
        print('two')


class BasicTestSuite(unittest.TestCase):

    def test_init(self):
        caller = Caller()
        ce = api.CommandDispatcher(caller)
        self.assertTrue(len(ce.strategies) == 3)

    def test_exec(self):
        caller = Caller()
        ce = api.CommandDispatcher(caller)
        ce.exec({'command': 'foo'})

    def test_exec_one_args(self):
        caller = Caller()
        ce = api.CommandDispatcher(caller)
        ce.exec({'command': 'one', 'args': ['test']})

    def test_command_not_found(self):
        caller = Caller()
        ce = api.CommandDispatcher(caller)
        with self.assertRaises(NameError):
            ce.exec({'command': 'missing'})

    def test_exec_missing_args(self):
        caller = Caller()
        ce = api.CommandDispatcher(caller)
        with self.assertRaises(TypeError):
            ce.exec({'command': 'one'})

    def test_wrong_format(self):
        caller = Caller()
        ce = api.CommandDispatcher(caller)
        with self.assertRaises(RuntimeError):
            ce.exec({'cmd': 'd'})

    def test_command_null(self):
        caller = Caller()
        ce = api.CommandDispatcher(caller)
        with self.assertRaises(RuntimeError):
            ce.exec({'command'})

    def test_none(self):
        caller = Caller()
        ce = api.CommandDispatcher(caller)
        with self.assertRaises(RuntimeError):
            ce.exec(None)