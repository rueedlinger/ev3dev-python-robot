# ev3dev Python Robot Examples
This project contains simple ev3dev robot examples for the LEGO MINDSTORMS EV3 intelligent brick. The API uses the [ev3dev](http://www.ev3dev.org/) Python module. 

You can use these examples to get started with 
your ev3dev self-driving robot.


## Get started
- Have a look at the *Getting Started with ev3dev* for how to use ev3dev https://www.ev3dev.org/docs/getting-started/
- The examples uses the *python-ev3dev2* Python library which are already bundled with the ev3dev image. https://ev3dev-lang.readthedocs.io/projects/python-ev3dev/en/stable/
- Follow the instruction from robotsquare (Educator Vehicle) http://robotsquare.com/2013/10/01/education-ev3-45544-instruction/

Make sure that the motors are connected to the following ouput pins:

- Right motor (EV3 large motor) => Output pin A
- Left motor (EV3 large motor) => Output pin B

Some of the examples may require the following sensors:

- Ultrasonic sensor
- Gyro sensor
- Color sensor
- Infrared sensor

Examples:

- [run_ir.py](run_ir.py) - is autonomous robot example. 
- [run_plain.py](run_plain.py) - is an example where you can steer the robot with IR remote.


> __Note:__
> The main logic is stored in the [robot](robot) package. To run these examples 
> you need to copy the _'robot'_ package as well.


### Plain ev3dev robot

[run_robot.py](run_robot.py) is a simple example for autonomous self driving robot. 
Copy the example to the EV3 brick an make the _run.py_ script executable. 

The example uses the following sensors:

- Ultrasonic sensor
- Color sensor
- Gyro sensor
    
### IR ev3dev robot (Infrared Remote)

[run_robot_remote_control.py](run_robot_remote_control.py)  is example how to control your robot with a the infrared remote control.

The example uses the following sensors:

- Infrared sensor
- Ultrasonic sensor
- Color sensor
- Gyro sensor

