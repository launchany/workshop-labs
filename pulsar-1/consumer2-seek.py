import pulsar

#
# A simple Pulsar consumer that listens to a topic and outputs received messages to the console
#
# Derived from: https://pulsar.apache.org/docs/en/standalone-docker/
#

client = pulsar.Client('pulsar://pulsar:6650')
consumer = client.subscribe('labs-pulsar-1-topic',
                            subscription_name='my-sub-2')

# seek to start and try to re-retrieve all published messages
consumer.seek(pulsar.MessageId.earliest)

while True:
    msg = consumer.receive()
    print("Received message: '%s'" % msg.data())
    consumer.acknowledge(msg)

client.close()
