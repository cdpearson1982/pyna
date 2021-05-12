#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser(description="Learning argparse")
parser.add_argument("name", help="The name of your old neighbor")
parser.add_argument("dog_name", help="The name of your old neighbors dog")
parser.add_argument("--at_home", default="Not sure", help="Use if name is at home")
parser.add_argument("-woc", "--working_on_car", metavar="WORK_ON_CAR", default=True, help="Set False if no car in shop")
parser.add_argument("-f", "--fedora", default=False, action="store_true", help="Use this flag if name is wearing a fedora")

args = parser.parse_args()

print(f"All provided args:\n{args}\n")
print(f"Name: {args.name}")
print(f"Dog Name: {args.dog_name}")
print(f"At Home: {args.at_home}")
print(f"Working on Car: {args.working_on_car}")
print(f"Wearing a Fedora: {args.fedora}")
print(type(args.fedora))
if args.fedora == True:
    print("Awesome Hat!!!")

#print(parser)
