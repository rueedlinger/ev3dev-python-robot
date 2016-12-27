# ev3dev Python Robot Examples
This project contains simple ev3dev robot examples for the LEGO MINDSTORMS EV3 intelligent brick. The API uses 
the [ev3dev](http://www.ev3dev.org/) Python module. You can use these examples to get started with 
your ev3dev self-driving robot.


## Get started
Build the Robot as described in my Blog Post _'Programming LEGO MINDSTORMS EV3 with Python and ev3dev'_ http://to.predict.ch/hacking/2016/12/02/lego-mindstorms-with-python.html or follow the "Educator Vehicle" 
instruction from robotsquare http://robotsquare.com/2013/10/01/education-ev3-45544-instruction/

- Right motor (EV3 large motor) -> Output pin A
- Left motor (EV3 large motor) -> Output pin B
- Ultrasonic sensor -> Input pin 1
- Gyro sensor -> Input pin 3
- Color sensor -> Input pin 4


All examples uses the [common](common) package. To run the following examples 
you need to copy the _'common'_ package as well.

- [plain_ev3dev_robot](plain_ev3dev_robot) - is as simple example for autonomous self driving robot. 
Copy the example to the EV3 brick an make the _run.py_ script executable.