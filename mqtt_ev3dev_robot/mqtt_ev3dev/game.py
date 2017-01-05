# -*- coding: utf-8 -*-
import random
import math

class Point:
    """
    A point in the game world. A pint has a score which is
    earned when the point was collected by the robot.
    """
    def __init__(self, x, y, r):
        """
        A point with x, y coordinates and a radius r.
        :param x: the x coordinate
        :param y: the y coordinate
        :param r: the radius
        """
        self.x = x
        self.y = y
        self.r = r
        self.collected = False
        self.score = 100

    def __str__(self):
        return "x: " + str(self.x) + ", y: " + str(self.y) + ", r:" + str(self.r)


class Game:
    """
    The game engine -  master of the points and score
    """

    def __init__(self, n_points=10, radius=5, max_x=800, max_y=800):

        self.__max_y = max_y
        self.__max_x = max_x
        self.__radius = radius
        self._n_points = n_points

        self.__points = self.create_points(n_points, round(max_x / 2), round(max_y / 2))

    def points(self):
        return self.__points

    def max_x(self):
        return self.__max_x

    def max_y(self):
        return self.__max_y

    def create_coordinate(self):
        x = random.randint(self.__radius * 2, self.__max_x - self.__radius * 2)
        y = random.randint(self.__radius * 2, self.__max_y - self.__radius * 2)
        return x, y

    def create_points(self, n_points, x_center, y_center):

        points = []

        for i in range(n_points):

            x, y = self.create_coordinate()
            r = self.__radius * 10

            while math.pow(x - round(x_center), 2) + math.pow(y - round(y_center), 2) < math.pow(r, 2):
                x, y = self.create_coordinate()

            points.append(Point(x=x, y=y, r=self.__radius))

        return points

    def check(self, x, y):
        for p in self.__points:
            if math.pow(x - p.x, 2) + math.pow(y - p.y, 2) < math.pow(p.r, 2):
                # robot has found the point
                p.collected = True




