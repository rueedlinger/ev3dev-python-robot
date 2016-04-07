#!/bin/bash
#
# Example: ev3dev leds
# ---------------------------------
# This script plays with the ev3 leds.
#

leds='/sys/class/leds/ev3\'


function green {
        echo 0 > /sys/class/leds/ev3\:left\:red\:ev3dev/brightness
        echo 0 > /sys/class/leds/ev3\:right\:red\:ev3dev/brightness

        echo 255 > /sys/class/leds/ev3\:right\:green\:ev3dev/brightness
        echo 255 > /sys/class/leds/ev3\:left\:green\:ev3dev/brightness           
}

function red {
        echo 255 > /sys/class/leds/ev3\:left\:red\:ev3dev/brightness
        echo 255 > /sys/class/leds/ev3\:right\:red\:ev3dev/brightness

        echo 0 > /sys/class/leds/ev3\:right\:green\:ev3dev/brightness
        echo 0 > /sys/class/leds/ev3\:left\:green\:ev3dev/brightness
}

function yellow {
        echo 50 > /sys/class/leds/ev3\:left\:red\:ev3dev/brightness
        echo 50 > /sys/class/leds/ev3\:right\:red\:ev3dev/brightness

        echo 255 > /sys/class/leds/ev3\:right\:green\:ev3dev/brightness
        echo 255 > /sys/class/leds/ev3\:left\:green\:ev3dev/brightness
}


function orange {
        echo 255 > /sys/class/leds/ev3\:left\:red\:ev3dev/brightness
        echo 255 > /sys/class/leds/ev3\:right\:red\:ev3dev/brightness

        echo 255 > /sys/class/leds/ev3\:right\:green\:ev3dev/brightness
        echo 255 > /sys/class/leds/ev3\:left\:green\:ev3dev/brightness
}


function off {
        echo 0 > /sys/class/leds/ev3\:left\:red\:ev3dev/brightness
        echo 0 > /sys/class/leds/ev3\:right\:red\:ev3dev/brightness

        echo 0 > /sys/class/leds/ev3\:right\:green\:ev3dev/brightness
        echo 0 > /sys/class/leds/ev3\:left\:green\:ev3dev/brightness
}



timeout=0.5


for i in `seq 1 5`;do

        green
        sleep $timeout
        yellow
        sleep $timeout
        orange
        sleep $timeout
        red
        sleep $timeout
        off
        sleep $timeout
done

off
