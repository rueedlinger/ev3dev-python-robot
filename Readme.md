# ev3dev Python Robot Examples
This project contains simple ev3dev robot examples for the LEGO MINDSTORMS EV3 intelligent brick. The API uses 
the [ev3dev](http://www.ev3dev.org/) Python module. You can use these examples to get started with 
your ev3dev self-driving robot.


## Get started
Build the Robot as described in my Blog Post _'Programming LEGO MINDSTORMS EV3 with Python and ev3dev'_ http://to.predict.ch/hacking/2016/12/02/lego-mindstorms-with-python.html or follow the 
instruction from robotsquare http://robotsquare.com/2013/10/01/education-ev3-45544-instruction/

Make sure that the motors are connected to the following ouput pins:

- Right motor (EV3 large motor) -> Output pin A
- Left motor (EV3 large motor) -> Output pin B

Some of the examples may require the follwoing sensors:

- Ultrasonic sensor
- Gyro sensor
- Color sensor
- Infrared sensor

> __Note:__
> The main logic is stored in the [common](common) package. To run these examples 
> you need to copy the _'common'_ package as well.

### Plain ev3dev robot

[plain_ev3dev_robot](plain_ev3dev_robot) is a simple example for autonomous self driving robot. 
Copy the example to the EV3 brick an make the _run.py_ script executable. 

The example uses the following sensors:

- Ultrasonic sensor
- Color sensor
- Gyro sensor
    
### IR ev3dev robot (Infrared Remote)

[ir_ev3dev_robot](ir_ev3dev_robot)  is example how to controll your robot with a the infrared remote control.

The example uses the following sensors:

- Infrared sensor
- Ultrasonic sensor
- Color sensor
- Gyro sensor