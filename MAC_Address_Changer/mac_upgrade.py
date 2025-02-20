# ╔════════════════════════════════════════════════════════════════════════════╗
# ║                                                                            ║
# ║             ███╗   ███╗ █████╗  ██╗██╗      ██████╗  ██████╗               ║
# ║             ████╗ ████║██╔══██╗███║██║     ██╔═══██╗██╔════╝               ║
# ║             ██╔████╔██║███████║╚██║██║     ██║   ██║██║                    ║
# ║             ██║╚██╔╝██║██╔══██║ ██║██║     ██║   ██║██║                    ║
# ║             ██║ ╚═╝ ██║██║  ██║ ██║███████╗╚██████╔╝╚██████╗               ║
# ║             ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═╝╚══════╝ ╚═════╝  ╚═════╝               ║
# ║                                                                            ║
# ║    Project: Mac_Changer                                                    ║
# ║    Created:                                                                ║
# ║    Author: ma1loc (youness anflous)                                        ║
# ║                                                                            ║
# ╚════════════════════════════════════════════════════════════════════════════╝

#!/usr/bin/env python

# TO_DO
# to-do-fun -> fun to gernerate a new random mac address every time !!!
# to-do-fun -> fun to check if the mac addr is really changed with new one !!!

# >>> help usage <<<
# python3 Mac_changer.py --help -> help you to the usage of the tool
# -i or --interface -> interface of the NIC to chage its MAC Address
# -m or --new_mac -> New MAC of your choise to assign it to the interface
# example of the usage -> python3 script.py -i eth0 -m 00:11:22:33:44:55 

import subprocess
import argparse
import re
import sys

def	parse_args():
    parser = argparse.ArgumentParser(description="Change the MAC Address of a network interface.")
    parser.add_argument("-i", "--interface", required=True, help="Interface to Change its MAC Address (e.g eth0).")
    parser.add_argument("-m", "--new_mac", required=True, help="MAC Address to assign it to the Interface. (e.g 1a:2b:3c:4d:5e:6f)")
    # if not (parser.interface):
    #     print("[-] No interface provided, use --help")
    # if not (parser.new_mac):
    #     print("[-] No MAC Address provided")
    return parser.parse_args()

def is_valid_addr(mac):
    if re.match(r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$", mac):
        return True
    print("[-] Invalid MAC Address format. Use format like 1a:2b:3c:4d:5e:6f.")
    return False

def upgrade_mac(interface, new_mac):
    try:
        print(f"[+] Updating the MAC address of {interface} to {new_mac}.")
        subprocess.run(["ip", "link", "set", interface, "down"])                # why at the end check=Ture
        subprocess.run(["ip", "link", "set", interface, "address", new_mac])    # why at the end check=Ture
        subprocess.run(["ip", "link", "set", interface, "up"])                  # why at the end check=Ture
        print("[+] MAC address successfully updated.")
    except subprocess.CalledProcessError as e:
        print(f"[-] Error: {e}")
        print("[-] MAC address NOT updated.")
    except Exception as e:
        print(f"[-] Unexpected error: {e}")

def is_root():
    if subprocess.run(["id", "-u"], capture_output=True, text=True).stdout.strip() != "0":
        print("[-] This script must be run as root. Use 'sudo'.")
        sys.exit(1)

def main():
    options = parse_args()
    is_root()
    if is_valid_addr(options.new_mac):
        upgrade_mac(options.interface, options.new_mac)

if __name__ == "__main__":
    main()