#!/usr/bin/env python3

#!/usr/bin/env python3
import argparse

import socket

from datetime import datetime

def server(port):
    x = "Your choice was server and it will run on port " + str(port)
    return x

def client(port):
    x = "Your choice was client and it will run on port " + str(port)
    return x

def parze(options):
    parser = argparse.ArgumentParser(description='Send and receive UDP locally')
    parser.add_argument('role', choices=options, help='which role to play')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060, help='UDP port (default 1060)')
#    parser.add_argument("updater", help="The person who ruined this code")
#    parser.add_argument("why", help="The reason name ruined this code")
#    parser.add_argument("solution", help="What will you do now that you have ruined it")
    return parser.parse_args()

def main():
    choices = {'client': client, 'server': server}
    args = parze(choices)
    function = choices[args.role]
    print(function(args.p))

if __name__ == "__main__":
    main()
