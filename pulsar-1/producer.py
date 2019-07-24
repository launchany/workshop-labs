import pulsar

#
# A simple Pulsar producer that publishes a message to a topic 10 times
#
# Derived from: https://pulsar.apache.org/docs/en/standalone-docker/
#

client = pulsar.Client('pulsar://pulsar:6650')
producer = client.create_producer('labs-pulsar-1-topic')

for i in range(10):
    producer.send(('hello-pulsar-%d' % i).encode('utf-8'))

client.close()
