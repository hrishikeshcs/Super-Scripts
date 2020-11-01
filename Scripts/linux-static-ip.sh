#!/bin/bash

# Set static address
### defaults for a raspberry Pi image ###
# Please change ip address (desired ip of device), router(gateway), and domain name servers (dns) to the appropriate addresses.

echo "" >> /etc/dhcpcd.conf
echo "interface enxb827eb068ce3" >> /etc/dhcpcd.conf
echo "  static ip_address=10.10.10.5/24" >> /etc/dhcpcd.conf
echo "  static routers=10.10.10.254" >> /etc/dhcpcd.conf
echo "  static domain_name_servers=10.10.10.6" >> /etc/dhcpcd.conf
echo "" >> /etc/dhcpcd.conf
echo "slaac hardware" >> /etc/dhcpcd.conf

### Used for testing anc check ###
#nano /etc/dhcpcd.conf
#init 6

### Created by Rob Fitz
