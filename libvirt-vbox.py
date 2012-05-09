#!/usr/bin/python -u
import libvirt
import sys
import os

#conn = libvirt.openReadOnly("qemu+tcp://192.168.171.110/system")
conn = libvirt.openReadOnly("qemu:///session")
if conn == None:
    print 'Failed to open connection to the hypervisor'
    sys.exit(1)

try:
    teste = conn.getSysInfo()
    (model, memory, cpus, mhz, nodes, socket, cores, threads) = conn.getInfo()
except:
    print 'Failed to extract the current node information'
    sys.exit(1)

print "Running on %d %s processors at %d MHz, %d MBytes of memory" % (
       cpus, model, mhz, memory)

if cpus > nodes * socket * cores * threads:
    print "Erroneous CPU information"
    sys.exit(1)

if cpus < nodes * socket * cores * threads:
    print "Strange, running in degrated mode, some CPU are not available"

print "OK"

print conn.numOfDomains()
print conn.listDomainsID()
for ID in conn.listDomainsID():
	dom = conn.lookupByID(ID)
	print dom.info()
	print dom.XMLDesc(4)


del conn

sys.exit(0)
