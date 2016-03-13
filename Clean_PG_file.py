#!/usr/bin/python

import sys, os, time
from optparse import OptionParser




################################### Functions

def timestamp():
	return time.strftime("[%a, %d %b %Y, %H:%M:%S] ", time.localtime())

###################################



################################### Arguments management

usage = "usage: %prog FILE"
parser = OptionParser(usage=usage)



(options, args) = parser.parse_args()
if len(args) != 1:
	parser.error("incorrect number of arguments")
else:
	File=args[0]



print >> sys.stderr, "--------------------------"
print >> sys.stderr, timestamp() + "Starting."
print >> sys.stderr, "Input file=" + str(File)
print >> sys.stderr, "--------------------------"


###################################





################################### Reading file

try:
    f = open(File)
    line=f.readline()
    while line!="":
        print line
        line=f.readline()

except IOError:
	print >> sys.stderr, timestamp() + "Error. Can not open input file: " + str(File)	
