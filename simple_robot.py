from ev3dev.auto import *
import time

m_right = Motor(OUTPUT_A)
m_left = Motor(OUTPUT_B)

us = UltrasonicSensor()
cs = ColorSensor()
gs = GyroSensor()
ts = TouchSensor()


Sound.speak('5, 4, 3, 2, 1, lets go!')
time.sleep(2)


angle = gs.value()
motors = [m_right, m_left]
normal_speed = 35
fast_speed = 60


def turn():
    angle = gs.value()
    adjusted = angle + 90
    stop()
    forward()
    m_left.run_direct()
    while(gs.value() <= adjusted):
        time.sleep(0.5)


    stop()
    forward()
    start()



def start():
    for m in motors:
        m.run_direct()

def set_speed(speed):
    for m in motors:
        m.duty_cycle_sp = speed

def stop():
    for m in motors:
        m.stop()


def forward():
    set_speed(normal_speed)

def backward():
    set_speed(-normal_speed)
    start()
    time.sleep(1)

def adjust(angle, speed):
    if angle > gs.value():
        m_right.duty_cycle_sp = speed - 5
        time.sleep(1)
        m_right.duty_cycle_sp = speed
    else:
        m_left.duty_cycle_sp = speed - 5
        time.sleep(1)
        m_left.duty_cycle_sp = speed

set_speed(normal_speed)
start()

while True:

    distance = us.value()
    color_reflect = cs.value()

    if distance > 250:
        set_speed(fast_speed)
    else:
        set_speed(normal_speed)


    #adjust(angle, normal_speed)

    if ts.value() == 1:
        stop()
        backward()
        turn()


    if color_reflect <= 7:
        stop()
        backward()
        turn()

    if distance <= 100:
        # break
        stop()
        backward()
        turn()


