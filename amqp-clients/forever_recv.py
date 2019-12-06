#!/usr/bin/env python

from __future__ import print_function
import optparse

from proton.handlers import MessagingHandler
from proton.reactor import Container
from proton import Url

class Recv(MessagingHandler):
    def __init__(self, url):
        super(Recv, self).__init__()
        self.url = Url(url)
        self.received = 0

    def on_start(self, event):
        conn = event.container.connect(self.url)
        event.container.create_receiver(conn, self.url.path)

    def on_message(self, event):
        self.received += 1
        print("Received message!")

parser = optparse.OptionParser(usage="usage: %prog [options]")
parser.add_option("-a", "--address", default="localhost:5672/examples",
                  help="address from which messages are received (default %default)")
opts, args = parser.parse_args()

try:
    Container(Recv(opts.address)).run()
except KeyboardInterrupt: pass



