#!/usr/bin/env python

# >>> help usage <<<
# python3 Mac_changer.py --help -> help you to the usage of the tool
# -i or --interface -> interface of the NIC to chage its MAC Address
# -m or --new_mac -> New MAC of your choise to assign it to the interface
# example of the usage -> python3 script.py -i eth0 -m 00:11:22:33:44:55

import	subprocess	# a library that execute programs with a new process id.
import	argparse	# a library that take an argument in the command line interface. (new then optparse)

def	parse_args():
    parser = argparse.ArgumentParser(description="cahgne MAC Address")
    parser.add_argument("-i", "--interface", required=True, help="Interface to Change its MAC Address.")
    parser.add_argument("-m", "--new_mac", required=True, help="MAC Address to assign it to the Interface.")
    return parser.parse_args()

def	new_mac(interface, new_mac):
		subprocess.run(["ip", "link", "set", interface, "down"])
		subprocess.run(["ip", "link", "set", interface, "address", new_mac])
		subprocess.run(["ip", "link", "set", interface, "up"])

options = parse_args()
new_mac(options.interface, options.new_mac)