FROM ubuntu:14.04

RUN apt-get update

RUN apt-get -y install python3 python3-pip libjpeg8-dev zlib1g-dev git

RUN pip3 install paho-mqtt python-ev3dev

COPY _build_docker /app

ENTRYPOINT ["python3", "/app/mqtt_ev3dev/run_simulator.py"]