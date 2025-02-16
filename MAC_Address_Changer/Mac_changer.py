#!/usr/bin/env python

import subprocess
import optparse

def		parse_args():
    parse = optparse.OptionParser()
    parse.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address.")
    parse.add_option("-m", "--mac", dest="new_mac", help="MAC Address to set it to the interface")
    return parse.parse_args()

def		change_mac(interface, new_mac):
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.run(["ifconfig", interface, "up"])


# problem with the no args
# problem with jsut -m of -i and both -m and -i without a value of it !!
(options, arguments) = parse_args()
change_mac(options.interface, options.new_mac)