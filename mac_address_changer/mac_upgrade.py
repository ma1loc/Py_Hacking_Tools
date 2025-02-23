# ╔══════════════════════════════════════════════════════════════════════════╗
# ║                                                                          ║
# ║             ███╗   ███╗ █████╗  ██╗██╗      ██████╗  ██████╗             ║
# ║             ████╗ ████║██╔══██╗███║██║     ██╔═══██╗██╔════╝             ║
# ║             ██╔████╔██║███████║╚██║██║     ██║   ██║██║                  ║
# ║             ██║╚██╔╝██║██╔══██║ ██║██║     ██║   ██║██║                  ║
# ║             ██║ ╚═╝ ██║██║  ██║ ██║███████╗╚██████╔╝╚██████╗             ║
# ║             ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═╝╚══════╝ ╚═════╝  ╚═════╝             ║
# ║                                                                          ║
# ║    Project: Mac_Changer                                                  ║
# ║    Created: 2025-02-23                                                   ║
# ║    Author: ma1loc (youness anflous)                                      ║
# ║                                                                          ║
# ╚══════════════════════════════════════════════════════════════════════════╝

#!/usr/bin/env python

# >>>>> days 8/30 <<<<<<

# TO_DO
# to-do-fun -> fun to gernerate a new random mac address every time !!!
# to-do-fun -> fun to check if the mac addr is really changed with new one !!!

import subprocess
import argparse
import re
import sys

def	parse_args():
    parser = argparse.ArgumentParser(description="Change the MAC Address of a network interface.")
    parser.add_argument("-i", "--interface", required=True, help="Interface to Change its MAC Address (e.g eth0).")
    parser.add_argument("-m", "--new_mac", required=True, help="MAC Address to assign it to the Interface. (e.g 1a:2b:3c:4d:5e:6f)")
    return parser.parse_args()

def is_valid_addr(mac):
    if re.match(r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$", mac):
        return True
    print("[-] Invalid MAC Address format. Use format like 1a:2b:3c:4d:5e:6f.")
    return False

def upgrade_mac(interface, new_mac):
    try:
        print(f"[+] Updating the MAC address of {interface} to {new_mac}.")
        subprocess.run(["ip", "link", "set", interface, "down"], check=True)
        subprocess.run(["ip", "link", "set", interface, "address", new_mac], check=True)
        subprocess.run(["ip", "link", "set", interface, "up"], check=True)
        print("[+] MAC address successfully updated.")
    except subprocess.CalledProcessError as error:
        print(f"[-] Error: {error}")
        print("[-] MAC address NOT updated.")
    except Exception as error:
        print(f"[-] Unexpected error: {error}")

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
