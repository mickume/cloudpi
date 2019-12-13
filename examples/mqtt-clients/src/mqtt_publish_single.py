#!/usr/bin/env python

import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

import optparse

parser = optparse.OptionParser()

parser.add_option('-p', '--port', type=int, default=1883)
parser.add_option('-u', '--url', default='localhost')
parser.add_option('-t', '--transport', default='tcp')
parser.add_option('-a', '--addr', default='sensors')

options, remainder = parser.parse_args()

publish.single(options.addr, "fu!", hostname=options.url)
