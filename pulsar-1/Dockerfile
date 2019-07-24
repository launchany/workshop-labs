FROM ubuntu

# Prep the container with the latest libraries, including Python and pip
RUN apt-get update && apt-get install -y python-pip curl

# install the python dependencies needed for the lab
RUN pip install pulsar-client --upgrade

ENV LAB_HOME /lab/
RUN mkdir $LAB_HOME
COPY *.py $LAB_HOME
COPY *.sh $LAB_HOME

CMD bash
