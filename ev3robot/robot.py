#!/usr/bin/python
# -*- coding: <encoding name> -*-

import threading
import time

class Robot:

    def __init__(self, strategy):
        self.timeout = 0.5
        self.strategy = strategy

    def _invoke(self):

        while True:

            if hasattr(self.strategy, '__call__'):
                self.strategy()
            else:
                self.strategy.loop()

            time.sleep(self.timeout)



    def run(self):
        threading.Thread(target=self._invoke).start()