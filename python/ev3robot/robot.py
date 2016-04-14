#!/usr/bin/python
# -*- coding: utf-8 -*-
import threading
import time


class Robot(threading.Thread):
    """
    Thread helper class to start a new robot. The robot class is responsible for starting the
    main logic of the robot in an new thread and the proper shutdown of the new started thread.
    """

    def __init__(self, strategy, timeout=0.1):
        """
        Creates a simple robot.

        :param strategy: the strategy which should be executed in an new thread

        :param timeout: in ms until the next iteration of the strategy starts (Default 0.1 ms).

        """
        super(Robot, self).__init__()
        self.timeout = timeout
        self.running = True
        self.strategy = strategy

    def run(self):
        """
        The provided strategy is executed in a new thread and runs in a endless loop until
        the method Robot.kill() is called.
        """

        self._invoke()

    def _invoke(self):

        try:
            # setup robot
            self.strategy.setup()

        except AttributeError:
            # method not implemented by strategy
            pass

        # main loop
        print('running')
        while self.running:
            self.strategy.loop()
            time.sleep(self.timeout)


        # stop motors
        self.strategy.brake()
        print('brake')

    def kill(self):
        """
        Sets the Robot.running to False, so that the thread which executes the strategy is terminated.
        """
        self.running = False
        print('kill')
        try:
            # teardown robot
            self.strategy.teardown()
        except AttributeError:
            # method not implemented by strategy
            pass

