#!/bin/bash
USER=`whoami`
INSTALL_DIR=/opt/SimpleMail
sudo -s
chmod +x simplemail
touch ${INSTALL_DIR}
cp src/* resources/* ${INSTALL_DIR}
chmod a+rw ${INSTALL_DIR}/simplemail_aliases
chmod a+rw ${INSTALL_DIR}/simplemail_store
cp install_files/simplemail /usr/local/bin
cp install-files/sm-server.conf /etc/init/
initctl reload-configuration
initctl start sm-server