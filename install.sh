#!/bin/bash

# Variables
USER=`whoami`
INSTALL_DIR=/opt/SimpleMail

# Use sudo privileges
sudo -s

# Install required packages
apt-get install pip
pip install termcolor textwrap ipaddr

# Create and fill install dir
touch ${INSTALL_DIR}
cp src/* resources/* ${INSTALL_DIR}
chmod a+rw ${INSTALL_DIR}/simplemail_aliases
chmod a+rw ${INSTALL_DIR}/simplemail_store

# Create command
cp install_files/simplemail /usr/local/bin
chmod +x usr/local/bin/simplemail

# Install the server as a service
cp install-files/sm-server.conf /etc/init/
initctl reload-configuration
initctl start sm-server