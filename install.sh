#!/bin/bash
USER=`whoami`
sudo -s
touch /opt/SimpleMail
cp Client.py Server.py simplemail_aliases simplemail_store SimpleMail_lib.py /opt/SimpleMail
cp simplemail /home/${USER}/.bin/
cp sm-server.conf /etc/init/
initctl reload-configuration
initctl start sm-server