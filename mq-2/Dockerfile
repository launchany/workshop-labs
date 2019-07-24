FROM ubuntu

# Prep the container with the latest libraries, including Python and pip
RUN apt-get update && apt-get install -y python-pip

# install the python dependencies needed for the lab
RUN pip install pika --upgrade

ENV LAB_HOME /lab/
RUN mkdir $LAB_HOME
COPY *.py $LAB_HOME

CMD bash
