#!/bin/bash

DOCKER_BUILD_DIR='_build_docker'

rm -rf $DOCKER_BUILD_DIR
mkdir $DOCKER_BUILD_DIR

cp -R ././../../mqtt_ev3dev $DOCKER_BUILD_DIR

docker build -t robot/simulator .