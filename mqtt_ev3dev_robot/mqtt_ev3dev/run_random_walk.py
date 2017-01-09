# -*- coding: utf-8 -*-
import sys
import logging
import json
import getopt
import paho.mqtt.client as mqtt
import time
import random

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)

TIMEOUT_SEC = 0.5
KEEPALIVE_SEC = 60

# default topic
topic = "robot"

# default mqtt broker (hostname or ip) and port
server = "127.0.0.1"
port = 1883


####
# global values:
# These values will be upated by robot/state an robot/position messages
####
angle = 0
x = 0
y = 0
r = 0
left_motor = 0
right_motor = 0
max_x = 0
max_y = 0




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

    logging.info("Try to connect to " + str(server) + ":" + str(port) + " and topic " + str(topic))

    mqtt = mqtt.Client()
    mqtt.connect(server, port, KEEPALIVE_SEC)


    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(client, userdata, flags, rc):
        logging.info("Connected with return code " + str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe(topic + "/position")
        client.subscribe(topic + "/state")


    def on_message(client, userdata, msg):
        global x, y, r, angle, left_motor, right_motor, max_x, max_y

        obj = json.loads(msg.payload.decode('utf-8'))

        # update position
        if "robot/position" in msg.topic:
            obj = json.loads(msg.payload.decode('utf-8'))
            x = obj['robot']['x']
            y = obj['robot']['y']
            r = obj['robot']['r']
            max_x = obj['world']['x_max']
            max_y = obj['world']['y_max']

        # update robot state
        if "robot/state" in msg.topic:
            angle = obj['angle']
            left_motor = obj['left_motor']
            right_motor = obj['right_motor']


    def on_disconnect(client, userdata, rc):
        logging.info("Disconnected with return code " + str(rc))


    mqtt.on_connect = on_connect
    mqtt.on_message = on_message
    mqtt.on_disconnect = on_disconnect


while True:

    mqtt.loop()
    time.sleep(TIMEOUT_SEC)

    o = random.randint(0, 100)

    logging.info("x: %s y: %s, r: %s, angle: %s, left_motor: %s, right_motor: %s, x-max: %s, y-max: %s" % (x, y, r, angle, left_motor, right_motor, max_x, max_y))

    if x >= max_x:

        print(angle % 360)

        if angle % 360 > 90:
            command = {'command': 'left', 'args': [10]}
            mqtt.publish(topic + "/process", json.dumps(command))
            continue

        command = {'command': 'backward', 'args': [10]}
        mqtt.publish(topic + "/process", json.dumps(command))
        continue

    if o <= 85:
        command = {'command': 'forward', 'args': [10 + random.randint(1, 5)]}
        mqtt.publish(topic + "/process", json.dumps(command))
    elif o <= 90:
        command = {'command': 'backward', 'args': [10 + random.randint(1, 5)]}
        mqtt.publish(topic + "/process", json.dumps(command))
    elif o <= 95:
        command = {'command': 'left', 'args': [random.randint(0, 180)]}
        mqtt.publish(topic + "/process", json.dumps(command))
    elif o <= 100:
        command = {'command': 'right', 'args': [random.randint(0, 180)]}
        mqtt.publish(topic + "/process", json.dumps(command))













