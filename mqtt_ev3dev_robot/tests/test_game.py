import unittest
import random
from .context import mqtt_ev3dev as api

import turtle

class BasicTestSuite(unittest.TestCase):

    def test_point(self):
        x = 10
        y = 9
        r = 5
        p = api.Point(x=x, y=y, r=r)
        self.assertEqual(p.collected, False)
        self.assertEqual(p.score, 100)
        self.assertEqual(p.x, x)
        self.assertEqual(p.y, y)
        self.assertEqual(p.r, r)

    def test_create_game(self):
        n = 10
        g = api.Game(n_points=n)
        self.assertEqual(len(g.points()), n)

    def test_check(self):
        n = 1
        g = api.Game(n_points=n)
        self.assertEqual(len(g.points()), n)
        p = g.points()[0]
        self.assertEqual(p.collected, False)

        g.check(p.x, p.y)

        p = g.points()[0]
        print(p)
        self.assertEqual(p.collected, True)

    def test_create_points(self):
        x = 300
        y = 300

        n = 80
        g = api.Game(n_points=n, max_x=x, max_y=y)

        self.assertEqual(len(g.points()), n)

        t = turtle.Turtle()
        t.speed(0)
        t.screen.screensize(x, y)

        t.forward(x)
        t.left(90)
        t.forward(y)
        t.left(90)
        t.forward(x)
        t.left(90)
        t.forward(y)
        t.setx(x/2)
        t.sety(y/2)
        t.circle(1)

        t.penup()
        for p in g.points():

            t.setx(p.x)
            t.sety(p.y)
            t.pendown()
            t.circle(p.r)
            t.penup()
            self.assertEqual(p.collected, False)

        t.setx(x / 2)
        t.sety(y / 2)

        t.color("red")
        for p in g.points():
            t.pendown()

            x = p.x + random.randint(-2, 2)
            y = p.y + random.randint(-2, 2)
            t.setx(x)
            t.sety(y)
            random.randint(-4, 40)
            g.check(x, y)
            t.begin_fill()
            t.circle(p.r)
            t.end_fill()

        for p in g.points():
            self.assertEqual(p.collected, True)





