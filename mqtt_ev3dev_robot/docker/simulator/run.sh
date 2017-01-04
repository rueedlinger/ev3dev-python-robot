#!/bin/bash

echo "args: $@"
docker run --rm --link broker robot/simulator $@