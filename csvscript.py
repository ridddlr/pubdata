#!/usr/bin/env python

import urllib
import sys
import optparse

def uopen(loc):
    url = 'http://updata.s3.amazonaws.com/' + loc
    resp = urllib.urlopen(url)
    return resp
    
def uprint(loc):
    for line in uread(loc):
        print 'line:', line

def getVal(tuple, schema, attr):
    index = schema.index(attr)
    value = tuple[index]
    return value

def getArray(line):
    newlinearray = line.split('\n')
    strippedline = newlinearray[0]
    array = strippedline.split(',')
    return array

def projdata(inputname, projattrs):
    print projattrs

    instream = uopen(inputname)

    #determine schema from first line
    firstline = instream.readline()
    schema = getArray(firstline)

    for line in instream:
        if line != '\n':
            tuple = getArray(line)
            projtuple = []
            for attr in projattrs:
                val = getVal(tuple, schema, attr)
                projtuple.append(val)
            print projtuple

def viewall(inputname):
    instream = uopen(inputname)

    #determine schema from first line
    firstline = instream.readline()
    schema = getArray(firstline)
    print schema
    projattrs = schema

    for line in instream:
        if line != '\n':
            tuple = getArray(line)
            projtuple = []
            for attr in projattrs:
                val = getVal(tuple, schema, attr)
                projtuple.append(val)
            print projtuple

def main(argv=None):
    if argv is None:
        argv = sys.argv

    p = optparse.OptionParser()

    (options, args) = p.parse_args()

    options = options.__dict__
    if len(args) == 0:
        print 'Please specify input file:'
        print 'python csvscript.py inputfile'
        sys.exit()
    inputname = sys.argv[1]

    #view all data
    viewall(inputname)

    #project out attrs
    #projattrs = ['a1', 'h5']
    #projdata(inputname, projattrs)


if __name__ == "__main__":
    sys.exit(main())

