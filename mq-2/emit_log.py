#!/usr/bin/env python
import pika
import sys

#
# A simple script to publish a message to a RabbitMQ topic
#
# Based on the script found at: https://www.rabbitmq.com/tutorials/tutorial-three-python.html
#

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()

channel.exchange_declare(exchange='labs-mq-2', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='labs-mq-2', routing_key='', body=message)
print(" [x] Sent %r" % message)
connection.close()
