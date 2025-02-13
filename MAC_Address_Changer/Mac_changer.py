#!/usr/bin/env python

# learn about the subprocess, optparse
import subprocess
import optparse

# basic
parser = optparse.OptionParser() # what is it and why

parser.add_option("-i", "--interface", dest="interface", help="Interface to chagne its MAC Address")
parser.add_option("-m", "--mac", dest="new_mac", help="The New MAC Address")

# how that (...) works.
(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

# basic basic
# interface = input("Interface -> ")
# new_mac = input("New MAC -> ")

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig" , interface, "up"])
 
print("Your interface " + interface + " is updated with the new MAC Address " + new_mac)