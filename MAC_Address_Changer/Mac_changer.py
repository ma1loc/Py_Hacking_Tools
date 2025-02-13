#!/usr/bin/env python

import subprocess

print("[+] Change the MAC Address.")

# here i will execute the command
# to chagne the mac address will use the command in linux
# ifconfig (name of the interface) down
# ifconfig hw (here the mac) ether (name of the interface)
# ifconfig (name of the interface) up
# you can add more futers to it (like auto randome mac address)

interface = input("Interface > ")
new_mac = input("New MAC > ")

subprocess.call(["ifconfig"])

