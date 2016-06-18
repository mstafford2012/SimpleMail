#!/bin/bash
USER=`whoami`
INSTALL_DIR=/opt/SimpleMail
sudo -s
chmod +x simplemail
touch ${INSTALL_DIR}
cp Client.py Server.py simplemail_aliases simplemail_store SimpleMail_lib.py ${INSTALL_DIR}
chmod a+rw ${INSTALL_DIR}/simplemail_aliases
chmod a+rw ${INSTALL_DIR}/simplemail_store
cp simplemail /usr/local/bin
cp sm-server.conf /etc/init/
initctl reload-configuration
initctl start sm-server