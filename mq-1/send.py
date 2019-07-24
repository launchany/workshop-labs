#!/usr/bin/env python
import pika

#
# A simple script to send a plain text message to a RabbitMQ queue
#
# Based on the script found at: https://www.rabbitmq.com/tutorials/tutorial-one-python.html
#

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()

channel.queue_declare(queue='labs-mq-1')

channel.basic_publish(exchange='', routing_key='labs-mq-1', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()

