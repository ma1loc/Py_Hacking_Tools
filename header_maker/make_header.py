# !/usr/bin/env python

# >>>>> days 0/30 <<<<<<

# ascii_art = {'A': [" █████╗ "]}     # to_know dictionary

import  datetime
import  argparse
from    ascii_letters import ascii_art

# TO_DO
# to-do-fun that count every letter in the name 

def user_args():
    parser = argparse.ArgumentParser(description="Author name")
    parser.add_argument("-a", "--author_name", required=True, help="Author name of the project.\n")
    parser.add_argument("-p", "--project_name", required=True, help="Name of your project")
    args = parser.parse_args()
    return (args)



def main():
    args = user_args()
    today = datetime.date.today()
    letter = 'M'
    print(f"{ascii_art[letter][0]}")
    print(f"{ascii_art[letter][1]}")
    print(f"{ascii_art[letter][2]}")
    print(f"{ascii_art[letter][3]}")
    print(f"{ascii_art[letter][4]}")
    print(f"{ascii_art[letter][5]}")
    len_ = len(ascii_art[letter][0])
    print(f"{len_}")

if __name__ == "__main__":
    main()
