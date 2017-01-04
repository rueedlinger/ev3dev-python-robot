FROM ubuntu:14.04
ENV app /app
ENV build _build_docker

ENV repo https://github.com/rueedlinger/ev3dev-python-robot

RUN apt-get update

RUN apt-get -y install python3 python3-pip libjpeg8-dev zlib1g-dev git

RUN pip3 install paho-mqtt python-ev3dev

ENV updated-adds-on 015

ADD ${build} ${app}

ENTRYPOINT ["python3", "/app/mqtt_ev3dev/run_simulator.py"]