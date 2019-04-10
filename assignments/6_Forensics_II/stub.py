#!/usr/bin/env python2

import sys
import struct

from datetime import datetime

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1
SECTION_COUNT = 0   #used to compare to validate

if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))


timestamp, author, section_count = struct.unpack("<L8sL", data[8:24])

#TODO: author validation

#validate section count
if section_count <= SECTION_COUNT:
    bork("Bad section count! Got %d, expected greater than %d" % (int(section_count), int(SECTION_COUNT)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

#convert string to int
timestamp_int = int(timestamp)

#format Unix time to readable format
timestamp = datetime.utcfromtimestamp(timestamp_int).strftime('%Y-%m-%d %H:%M:%S')

print("TIMESTAMP: %s" % timestamp)

print("AUTHOR: %s" % author)

print("SECTION COUNT: %s" % section_count)

print("-------  BODY  -------")
#TODO: BODY
