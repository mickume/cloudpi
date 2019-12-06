import paho.mqtt.client as mqtt
import optparse

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe(mqttAddress)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

parser = optparse.OptionParser()

parser.add_option('-p', '--port', type=int, default=1883)
parser.add_option('-u', '--url', default='mqtt://example.com')
parser.add_option('-t', '--transport', default='tcp')

options, remainder = parser.parse_args()

client = mqtt.Client(client_id='mqtt_client', transport=options.transport)
client.username_pw_set('cloudpi1', password='Y2xvdWRwaTEK')

client.on_connect = on_connect
client.on_message = on_message

print('Connecting to', options.url, options.port, options.transport)
client.connect(options.url, options.port, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.

client.loop_forever()
