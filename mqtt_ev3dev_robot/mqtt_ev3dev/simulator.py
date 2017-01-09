# -*- coding: utf-8 -*-
import math


class Simulator:
    """
    Simulator for the robot and positional system. With a given RADIUS (radius of the obot in cm),
    POSITION_FACTOR (factor between robot distance and positional system) and TACHO_COUNT_CM_RATIO
    (factor between robot distance and cm).
    """
    # round x/y position
    ROUND_DIGITS = 2
    # The radius of the robot in cm
    RADIUS_CM = 7
    # factor robot distance (tacho counts) to cm (20 tacho counts ca. 1 cm)
    TACHO_COUNT_CM_FACTOR = 20
    # factor between robot distance (tacho counts) and x/y positional system
    POSITION_FACTOR = 2

    def __init__(self, x=0, y=0, angle=0, r=15):
        """
        Initialize the robot simulator and positional system.
        :param x: the horizontal starting position.
        :param y: the vertical starting position.
        :param angle: the starting angle in degrees.
        """
        self.__x = x
        self.__y = y
        self.__r = r
        self.__angle = angle
        self.__start_x = x * self.POSITION_FACTOR
        self.__start_y = y * self.POSITION_FACTOR
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
        self.__right_distance = 0
        self.__left_distance = 0

    def angle(self):
        """
        The current angle in degrees.
        :return: the angle degrees.
        """
        return self.__angle

    def position(self):
        """
        The current position adn radius (x,y,r) from the robot.
        :return: the x, y coordinates and radius as tuple
        """
        return round(self.__x * 1 / self.POSITION_FACTOR, self.ROUND_DIGITS), round(self.__y * 1/self.POSITION_FACTOR, self.ROUND_DIGITS), self.__r

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
            'left_motor': self.__left_distance,
            'angle': self.angle()
        }

        return out

    def calc_distance_with_angle(self, angle):
        """
        Calculate the distance when the robot turns a given angle in degree.
        :param angle: angle in degree
        :return: distance in tacho counts
        """
        return round(2 * self.RADIUS_CM * math.pi * angle / 360 * self.TACHO_COUNT_CM_FACTOR)

    def __str__(self):
        return "x: %s, y: %s, angle: %s" % (self.__x, self.__y, self.__angle)




