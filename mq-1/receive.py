#!/usr/bin/env python
import pika

#
# A simple script to check a RabbitMQ queue and print any messages found
#
# Based on the script found at: https://www.rabbitmq.com/tutorials/tutorial-one-python.html
#

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()

channel.queue_declare(queue='labs-mq-1')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(
    queue='labs-mq-1', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

