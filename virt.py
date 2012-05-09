#!/usr/bin/python
#############################################
# Criado em: 22/10/2010 11:34:01
# Sergio Cioban Filho
#############################################

import libvirt
import sys

conn = libvirt.openReadOnly("vbox:///session")
if conn == None:
    print 'Failed to open connection to the hypervisor'
    sys.exit(1)

try:
    dom0 = conn.lookupByName("VPN")
except:
    print 'Failed to find the main domain'
    sys.exit(1)

print "VPN: id %d running %s" % (dom0.ID(), dom0.OSType())
print dom0.info()
