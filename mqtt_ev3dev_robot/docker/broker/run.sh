#!/bin/bash

docker run --rm -ti -p 1883:1883 -p 9001:9001 --name broker toke/mosquitto