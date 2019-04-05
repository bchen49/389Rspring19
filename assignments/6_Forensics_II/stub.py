#!/usr/bin/env python2

import sys
import struct


# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)

def is_ascii(s)
	return all(ord(c) < 128 for c in s)


# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1

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
ctr = 8;

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

timestamp = struct.unpack("<L",data[ctr:ctr+4])
ctr = ctr+4

author = struct.unpack("<s",data[ctr:ctr+8])
author.ljust(8,'0x0')
ctr = ctr + 8

section = struct.unpack("<d",data[ctr,ctr+4])
ctr = ctr + 4

if int(section) <= 0:
	bork("Bad section, must be greater than 0")

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: %d" % int(timestamp))
print("AUTHOR: %s" % str(author))
print("SECTION COUNT: %d" % int(section))


# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")

ctr = sizeoff(header)

for x in range(int(section))
	stype = struct.unpack("<h",data[ctr,ctr+4])
	ctr = ctr + 4
	slen = struct.unpack("<d",data[ctr,ctr+4])
	ctr = ctr + 4
	svalue = 0

	if(int(slen) > 0):
		svalue = struct.unpack("=s",data[ctr,ctr+slen])

	#ASCII encode
	if(hex(stype) == "0x1"):
		if(is_ascii(svalue)):
			print("Section Type: SECTION_ASCII")
			print("Section Length: %d" % int(slen))
			print("Section Value: %s" % svalue)
		else:
			bork("Bad Section")

	if(hex(stype) == "0x2"):
		try:
			svalue.decode('utf-8')
			print("Section Type: SECTION_AUTF8")
			print("Section Length: %d" % int(slen))
			print("Section Value: %s" % svalue)
		except UnicodeError:
			print("Bad Section")
	if(hex(stype) == "0x3"):
		




	
