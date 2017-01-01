#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import logging
import json
import paho.mqtt.client as mqtt

from command import CommandExecutor
from robot import Robot
from simulator import Simulator

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)

TOPIC = "robot"
SERVER = "192.168.254.101"
PORT = 1883
TIMEOUT_SEC = 1
KEEPALIVE_SEC = 60

if __name__ == "__main__":
    kwargs = dict(x.split('=', 1) for x in sys.argv[1:])
    print(kwargs)

    robot = Simulator()
    dispatcher = CommandExecutor(robot)

    logging.info("Try to connect to " + str(SERVER) + ":" + str(PORT) + " and topic " + str(TOPIC))

    mqtt = mqtt.Client()
    mqtt.connect(SERVER, PORT, KEEPALIVE_SEC)


    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(client, userdata, flags, rc):
        logging.info("Connected with return code " + str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe(TOPIC + "/process")


    # The callback for when a PUBLISH message is received from the server.
    def on_message(client, userdata, msg):
        logging.info("Received message '" + str(msg.payload) + " on topic " + msg.topic + " with QoS " + str(msg.qos))

        try:
            obj = json.loads(msg.payload.decode('utf-8'))
            dispatcher.exec(obj)
        except Exception:
            logging.exception("Invalid message format! %s" % msg.payload)


    def on_disconnect(client, userdata, rc):
        logging.info("Disconnected with return code " + str(rc))


    mqtt.on_connect = on_connect
    mqtt.on_message = on_message
    mqtt.on_disconnect = on_disconnect


    while True:
        resp = mqtt.loop(timeout=TIMEOUT_SEC)

        # try reconnect when return code is not 0
        if resp != 0:
            try:
                mqtt.reconnect()
            except ConnectionRefusedError:
                logging.exception("connection lost rc=%s" % rc)
        else:
            mqtt.publish(TOPIC + "/state", json.dumps(robot.state()))


