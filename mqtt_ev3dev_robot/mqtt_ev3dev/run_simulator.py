# -*- coding: utf-8 -*-
import sys
import logging
import json
import getopt
import paho.mqtt.client as mqtt
import time

from simulator import Simulator
from game import PointEncoder
from command import CommandDispatcher
from game import Game

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)

TIMEOUT_SEC = 1
KEEPALIVE_SEC = 60

# default topic
topic = "robot"

# default mqtt broker (hostname or ip) and port
server = "127.0.0.1"
port = 1883


if __name__ == "__main__":

    logging.info("Starting simulator...")

    # parse args
    optlist, args = getopt.getopt(sys.argv[1:], shortopts="", longopts=["broker=", "port=", "topic="])

    for opt, arg in optlist:
        if opt == '--broker':
            server = arg
        elif opt == '--port':
            port = arg
        elif opt == '--topic':
            topic = arg

    # default robot / game
    game = Game(n_points=50, radius=5, max_x=800, max_y=800, radius_factor=40)
    logging.info("Game: " + str(game))

    robot = Simulator(x=game.center_x(), y=game.center_y())
    logging.info("Robot: " + str(robot))

    dispatcher = CommandDispatcher(robot)

    logging.info("Try to connect to " + str(server) + ":" + str(port) + " and topic " + str(topic))

    mqtt = mqtt.Client()
    mqtt.connect(server, port, KEEPALIVE_SEC)


    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(client, userdata, flags, rc):
        logging.info("Connected with return code " + str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe(topic + "/process")
        client.subscribe("game")


    # The callback for when a PUBLISH message is received from the server.
    def on_message(client, userdata, msg):
        logging.info("Received message '" + str(msg.payload) + " on topic " + msg.topic + " with QoS " + str(msg.qos))

        if "robot" in msg.topic:
            try:
                obj = json.loads(msg.payload.decode('utf-8'))
                dispatcher.exec(obj)
                client.publish(topic + "/done", json.dumps(obj))
            except Exception as ex:
                logging.exception("Invalid message format! %s" % msg.payload)
                client.publish(topic + "/error",  json.dumps({'type': type(ex).__name__, 'error': str(ex)}))

        if "game" in msg.topic:
            global game, robot
            logging.info("Reset game")
            robot.reset()
            game.reset()


    def on_disconnect(client, userdata, rc):
        logging.info("Disconnected with return code " + str(rc))


    mqtt.on_connect = on_connect
    mqtt.on_message = on_message
    mqtt.on_disconnect = on_disconnect

    mqtt.loop_start()

    while True:

        time.sleep(TIMEOUT_SEC)

        mqtt.publish(topic + "/state", json.dumps(robot.state()))

        x, y, r = robot.position()
        x_max = game.max_x()
        y_max = game.max_y()

        game.check(x, y, r)
        points = game.points()

        mqtt.publish(topic + "/position", json.dumps({'robot': {'x': x, 'y': y, 'r': r},
                                                      'world': {'x_max': x_max, 'y_max': y_max},
                                                      'points': points}, cls=PointEncoder))



