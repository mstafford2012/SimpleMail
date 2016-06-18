import json
import socket

isColored = True
MAILSTORE_FILENAME = 'simplemail_store'
ALIASES_FILENAME = 'simplemail_aliases'

def get_aliases():

    alias_file = open('/opt/SimpleMail/simplemail_aliases', 'r')
    aliases = json.load(alias_file)
    alias_file.close()

    return aliases

def get_mail():

    mail_file = open('/opt/SimpleMail/simplemail_store', 'r')
    mail = json.load(mail_file)
    mail_file.close()

    return mail


def set_mail(mail):

    mail_file = open(MAILSTORE_FILENAME, 'w')
    mail_file.write(json.dumps(mail))
    mail_file.flush()
    mail_file.close()

def get_alias(ip):

    if ip in get_aliases().values():
        for name in get_aliases():
            if get_aliases()[name] == ip:
                return name
    else:
        return ip


lib_outward_ip = (
    [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1],
                 [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in
                   [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
