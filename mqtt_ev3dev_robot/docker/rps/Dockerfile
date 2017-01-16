FROM jjanzic/docker-python3-opencv 

RUN pip3 install jupyter
RUN pip3 install matplotlib
RUN pip3 install paho-mqtt


# Add Tini. Tini operates as a process subreaper for jupyter. This prevents
# kernel crashes.
ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]

EXPOSE 8888
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0"]


#EXPOSE 8888

#CMD /usr/local/bin/jupyter-notebook --ip=0.0.0.0
