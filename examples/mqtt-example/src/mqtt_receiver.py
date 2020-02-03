#!/usr/bin/env python

import paho.mqtt.client as mqtt
import optparse

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

parser = optparse.OptionParser()

parser.add_option('-p', '--port', type=int, default=1883)
parser.add_option('-u', '--url', default='localhost')
parser.add_option('-t', '--transport', default='tcp')
parser.add_option('-a', '--addr', default='sensors')

options, remainder = parser.parse_args()

client = mqtt.Client(client_id='mqtt_receiver', transport=options.transport)
#client.username_pw_set('cloudpi1', password='Y2xvdWRwaTEK')

client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.on_subscribe = on_subscribe

client.connect(options.url, options.port, 60)
client.subscribe(options.addr)

client.loop_forever()
