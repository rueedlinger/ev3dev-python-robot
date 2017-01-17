# -*- coding: utf-8 -*-
import unittest
from .context import mqtt_ev3dev as api


class BasicTestSuite(unittest.TestCase):

    def test_init(self):
        d = api.TimeDecorator(api.Simulator())
        self.assertIsNotNone(d.simulator)

    def test_method_delegate(self):
        d = api.TimeDecorator(api.Simulator())
        self.assertIsNotNone(d.position())
        self.assertIsNotNone(d.state())
        self.assertIsNotNone(d.angle())
        self.assertIsNone(d.stop())

    def test_method_not_implemented(self):
        d = api.TimeDecorator(api.Simulator())
        try:
            d.foo()
            self.fail("Exception not thrown")
        except AttributeError:
            pass

    def test_forward_whole_distance(self):
        d = api.TimeDecorator(api.Simulator())
        start_pos = (0.0, 0.0, 15)

        self.assertEqual(d.position(), start_pos)
        d.forward(100)
        self.assertEqual(d.position(), (50.0, 0.0, 15))

        d.tick()
        self.assertEqual(d.position(), (50.0, 0.0, 15))

    def test_backward_whole_distance(self):
        d = api.TimeDecorator(api.Simulator())
        start_pos = (0.0, 0.0, 15)

        self.assertEqual(d.position(), start_pos)
        d.backward(100)
        self.assertEqual(d.position(), (-50.0, 0.0, 15))

        d.tick()
        self.assertEqual(d.position(), (-50.0, 0.0, 15))

    def test_forward(self):
        d = api.TimeDecorator(api.Simulator())
        start_pos = (0.0, 0.0, 15)

        self.assertEqual(d.position(), start_pos)
        d.forward(350)
        self.assertEqual(d.position(), (50.0, 0.0, 15))

        d.tick()
        self.assertEqual(d.position(), (100.0, 0.0, 15))

        d.tick()
        self.assertEqual(d.position(), (150.0, 0.0, 15))

        d.tick()
        self.assertEqual(d.position(), (175.0, 0.0, 15))

        d.tick()
        self.assertEqual(d.position(), (175.0, 0.0, 15))

    def test_backward(self):
        d = api.TimeDecorator(api.Simulator())
        start_pos = (0.0, 0.0, 15)

        self.assertEqual(d.position(), start_pos)
        d.backward(350)
        self.assertEqual(d.position(), (-1.0, 0.0, 15))

        d.tick()
        self.assertEqual(d.position(), (-2.0, 0.0, 15))

        d.tick()
        self.assertEqual(d.position(), (-3.0, 0.0, 15))

        d.tick()
        self.assertEqual(d.position(), (-4.0, 0.0, 15))

        d.tick()
        self.assertEqual(d.position(), (-5, 0.0, 15))

    def test_next_command(self):
        d = api.TimeDecorator(api.Simulator(), speed=1000)
        start_pos = (0.0, 0.0, 15)

        self.assertEqual(d.position(), start_pos)
        d.forward(978)

        self.assertEqual(d.next, {'command': 'forward', 'value': 968})
        d.tick()
        self.assertEqual(d.next, {'command': 'forward', 'value': 958})

        d.forward(350)
        self.assertEqual(d.next, {'command': 'forward', 'value': 250})

        d.reset()
        self.assertEqual(d.next, {'command': None, 'value': 0})

        d.forward(600)
        self.assertEqual(d.next, {'command': 'forward', 'value': 500})

        d.backward(300)
        self.assertEqual(d.next, {'command': 'backward', 'value': 200})

        d.tick()
        self.assertEqual(d.next, {'command': 'backward', 'value': 100})


