# -*- coding: utf-8 -*-
import math


class Simulator:
    """
    Simulator for the robot and positional system. With a given RADIUS and TACHO COUNT CM RATIO.
    """

    ROUND_DIGITS = 2
    RADIUS_CM = 7
    TACHO_COUNT_CM_FACTOR = 20
    POSITION_FACTOR = 1/2

    def __init__(self, x=0, y=0, angle=0):
        """
        Initialize the robot simulator and positional system.
        :param x: the horizontal starting position.
        :param y: the vertical starting position.
        :param angle: the starting angle in degrees.
        """
        self.__x = x
        self.__y = y
        self.__angle = angle
        self.__start_x = x
        self.__start_y = y
        self.__start_angle = angle
        self.__left_distance = 0
        self.__right_distance = 0

    def forward(self, distance):
        """
        Move the robot forward by a given distance.
        :param distance: the distance the robot should move forward.
        :return: None
        """
        x = math.cos(math.radians(self.__angle)) * distance
        y = math.sin(math.radians(self.__angle)) * distance
        self.__x += x
        self.__y += y
        self.__left_distance += distance
        self.__right_distance += distance

    def backward(self, distance):
        """
        Move the robot backward by a given distance.
        :param distance: the distance the robot should move backward.
        :return: None
        """
        x = math.cos(math.radians(self.__angle)) * distance
        y = math.sin(math.radians(self.__angle)) * distance
        self.__x -= x
        self.__y -= y
        self.__left_distance -= distance
        self.__right_distance -= distance

    def right(self, angle):
        """
        Turn the robot right by a given angle (degrees).
        :param angle: the angle in degrees.
        :return: None
        """
        self.__angle -= angle
        distance = self.calc_distance_with_angle(angle)
        self.__right_distance -= distance
        self.__left_distance += distance

    def left(self, angle):
        """
        Turn the robot left by a given angle (degrees).
        :param angle: the angle in degrees.
        :return: None
        """
        self.__angle += angle
        distance = self.calc_distance_with_angle(angle)
        self.__right_distance += distance
        self.__left_distance -= distance

    def reset(self):
        """
        Sets the robot back to the staring position.
        :return: None
        """
        self.__x = self.__start_x
        self.__y = self.__start_y
        self.__angle = self.__start_angle

    def angle(self):
        """
        The current angle in degrees.
        :return: the angle degrees.
        """
        return self.__angle

    def position(self):
        """
        The current position (x,y) from the robot.
        :return: the x, y coordinates as tuple
        """
        return round(self.__x * self.POSITION_FACTOR, self.ROUND_DIGITS), round(self.__y *  self.POSITION_FACTOR, self.ROUND_DIGITS)

    def stop(self):
        """
        Stops the robot
        :return: None
        """
        pass

    def state(self):
        """
        Returns the state of the robot (distance right / left motor and angle)
        :return: map {'right_motor', 'lef_motor', 'angle'} with the current values distance
        left motor, distance right motor and current angle in degrees of the robot
        """
        out = {
            'right_motor': self.__right_distance,
            'lef_motor': self.__left_distance,
            'angle': self.angle()
        }

        return out

    def calc_distance_with_angle(self, angle):
        return round(2 * self.RADIUS_CM * math.pi * angle / 360 * self.TACHO_COUNT_CM_FACTOR)

