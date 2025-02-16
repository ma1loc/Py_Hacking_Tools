#!/usr/bin/env python

import subprocess
import optparse

def	parse_args():
	parse = optparse.OptionParser()
	parse.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address.")
	parse.add_option("-m", "--mac", dest="new_mac", help="MAC Address to set it to the interface")
	(options, arguments) = parse.parse_args()
	if not options.interface:
    		parse.error("[-] Error There's no provided Interface, use --help for clear usge.")
	elif not options.new_mac:
    		parse.error("[-] Error There's no provided MAC Addr, use --help for clear usge.")
	return options

def change_mac(interface, new_mac):
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.run(["ifconfig", interface, "up"])

options = parse_args()
change_mac(options.interface, options.new_mac)