import unittest
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

        n = 10
        g = api.Game(n_points=n, max_x=300, max_y=300)
        self.assertEqual(len(g.points()), n)

        t = turtle.Turtle()
        #t.screen.screensize(400,400)

        t.forward(300)
        t.left(90)
        t.forward(300)
        t.left(90)
        t.forward(300)
        t.left(90)
        t.forward(300)
        t.setx(300/2)
        t.sety(300/2)
        t.circle(1)


        t.penup()
        for p in g.points():

            t.setx(p.x)
            t.sety(p.y)
            t.pendown()
            t.circle(p.r)
            t.penup()
            print(p)







