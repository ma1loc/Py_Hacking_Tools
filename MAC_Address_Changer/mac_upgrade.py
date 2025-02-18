#!/usr/bin/env python

# >>> help usage <<<
# python3 Mac_changer.py --help -> help you to the usage of the tool
# -i or --interface -> interface of the NIC to chage its MAC Address
# -m or --new_mac -> New MAC of your choise to assign it to the interface
# example of the usage -> python3 script.py -i eth0 -m 00:11:22:33:44:55

import	subprocess	# a library that execute programs with a new process id.
import	argparse	# a library that take an argument in the command line interface. (new then optparse).
import  re          # a library for regular expression operations (matching some thing).
import  sys         # ???

def	parse_args():
    parser = argparse.ArgumentParser(description="Change the MAC Address of a network interface.")
    parser.add_argument("-i", "--interface", required=True, help="Interface to Change its MAC Address (e.g eth0).")
    parser.add_argument("-m", "--new_mac", required=True, help="MAC Address to assign it to the Interface. (e.g 1a:2b:3c:4d:5e:6f)")
    return parser.parse_args()

def is_valid_addr(mac):
    # in this functoin will check if the MAC Address is valid or not.
    # here i use the regular expression(regex) to see the match of the providing "mac"
    if re.match(r"^(0-9A-Fa-f{2}[:-]){5}(0-9A-Fa-f){2})$"):
        return True
    return False

def upgrade_mac(interface, new_mac):
    # in the upgrade_mac function, we will execute the command lines.
    try:    # try statement -> help if there's an error will execute the 
        print(f"[+] Update the {interface} to the {new_mac}.") # msg start, why the (f"") ???
        subprocess.run(["ip", "link", "set", interface, "down"])
        subprocess.run(["ip", "link", "set", interface, "address", new_mac])
        subprocess.run(["ip", "link", "set", interface, "up"])
        print("[+] Updating the MAC Address was successfully done.") # msg end
    #  except subprocess.CalledProcessError as e: why and what is it ???
    except:
        print("[-] Error happening, MAC Address NOT upgraded")

def is_root():
    # Check if the script is run as root.
    if subprocess.run(["id", "-u"], capture_output=True, text=True).stdout.strip() != "0": # what and why ???
        print("[-] This script must be run as root. Use 'sudo'.")
        sys.exit(1)

def main():
    is_root()
    options = parse_args()
    is_valid_addr(options.new_mac)
    upgrade_mac(options.interface, options.new_mac)

    # if not (parser.interface):
    #     print("[-] No interface provided, use --help")
    # if not (parser.new_mac):
    #     print("[-] No MAC Address provided")

if __name__ == "__main__": # what and why ???
    main()