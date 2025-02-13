#!/usr/bin/env python

import subprocess	# create a new process for the program command like [ls] to be executed without losing the process of the current program
import optparse		# library help to pars the argument that the user put it in the input as a command

def get_args():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address.")
	parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address to assign it to the interface.")
	return parser.parse_args()

def	mac_changer(interface, new_mac):
	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
	subprocess.call(["ifconfig", interface, "up"])

(options, arguments) = get_args()
# ^^^^^^^^^^^^^^^^^^
# expline to me this part i don't have any idea about it

print(arguments.interface) # why i can not use the the arguments, it yes why i use it in line 17 ?
print(arguments.new_mac) # same here and what is the . between the arguments and new_mac ?