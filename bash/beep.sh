#!/bin/bash
#
# Example: ev3dev ultrasonic sensor
# ---------------------------------
# This scripts beeps for every distance/1000. So when the 
# distance is mm (millimetre) the script will beep for 100 mm in a 
# 100/1000 milliseconds interval.

# ultrasonic sensor
sensor=/sys/class/lego-sensor/sensor0

# sets mode to CM and decimals 1
# value -> 101 = 10.1 cm
echo "US-DIST-CM" > $sensor/mode


mode=$(cat $sensor/mode)
echo "mode $mode"

while true; do

        value=$(cat $sensor/value0)

        timeout=$(echo "$value 1000" | awk '{printf "%.4f \n", $1/$2}')

        echo "timeout $timeout"
        echo "value $value"

        beep -f 1000
        sleep $timeout
done