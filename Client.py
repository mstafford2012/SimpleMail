import sys
import collections
from termcolor import colored
import textwrap
import datetime
import ipaddr
from SimpleMail_lib import *

offer_help = "Type \'simplemail help\' to see help."

def main(args):

    outward_ip = ipaddr.IPv4Network(lib_outward_ip + "/24")

    aliases = get_aliases()

    if len(args) < 2 or len(args) > 4:
        print "Wrong number of arguments. ", offer_help
        exit(1)

    if args[1] == "alias":

        alias_command(aliases, args)

    elif args[1] == "help":

        show_help()

    elif args[1] == "inbox":

        show_inbox(args)

    elif args[1] == "delete":

        delete_message(args)

    else:

        send_message(aliases, args, outward_ip)


def delete_message(args):

    if len(args) == 3:

        if args[2] == 'all':
            set_mail(dict())

        elif all(char.isdigit() for char in args[2]):
            mail = collections.OrderedDict(reversed(sorted(get_mail().items())))
            del mail[mail.items()[int(args[2])][0]]
            set_mail(mail)

        elif args[2] == 'read':
            mail = collections.OrderedDict(reversed(sorted(get_mail().items())))

            for time, msg in mail.items():
                if msg[u'Read'] == 'yes':
                    del mail[time]

            set_mail(mail)

        else:
            print args[2] + " didn't match for 'delete' command... ", offer_help

    else:
        print "Wrong number of arguments for delete... ", offer_help


def send_message(aliases, args, outward_ip):

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    target_ip = ""
    try:
        if args[1] == 'all':
            target_ip = str(outward_ip.broadcast)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        else:
            ipaddr.IPv4Network(args[1])
            target_ip = args[1]

            # legal ip given

    except ValueError:
        # Try to use as alias

        if args[1] in aliases:
            target_ip = aliases[args[1]]

        else:
            print "Could not send message and no alias for ", args[1], " ", offer_help
            exit(1)

    if len(args) == 3:
        sock.sendto(args[2], (target_ip, 5005))
    else:
        print "No message... Type \'simplemail help\' to see help."


def alias_command(aliases, args):
    if len(args) == 4:

        alias_file = open(ALIASES_FILENAME, 'w')

        try:
            ipaddr.IPv4Network(args[3])
            aliases[args[2]] = args[3]

        except ValueError, ipaddr.AddressValueError:
            print "Expected an IP address ", offer_help

        alias_file.write(json.dumps(aliases))
        alias_file.flush()
        alias_file.close()

    else:

        for key in aliases:
            print key, aliases[key]


def show_inbox(args):

    width = 50

    mail = collections.OrderedDict(reversed(sorted(get_mail().items())))

    if len(args) == 3 and all(char.isdigit() for char in args[2]):

        (timestamp, msg) = mail.items()[int(args[2])]
        print colored("From: " + get_alias(msg[u'From'][0]), "blue"),

        t = datetime.datetime.fromtimestamp(float(timestamp))
        print colored(t.strftime('%a %b %d, %Y %I:%M:%S %p') + '\n', "yellow") + ('-' * width)

        for line in textwrap.wrap(msg[u'Body'], width):
            print line

        print '-'*width

        msg[u'Read'] = "yes"
        set_mail(mail)

    else:
        i = 0
        for timestamp in mail:

            print i,
            i += 1

            width = 50

            msg = mail[timestamp]
            read = msg[u'Read'] == "yes"

            if read:
                print "[x]",
            else:
                print "[ ]",

            sender = get_alias(msg[u'From'][0])

            body = str(msg[u'Body'])
            body.replace('\n', '').replace('\t', '')

            if len(body) > width-3:
                print sender+":", body[:width] + "..."
            else:
                print sender + ":", body


def show_help():
    print "Usage: simplemail (<ip> or <alias>) \"<Message>\"  Send a message"
    print "       simplemail all \"<Message>\"          Broadcast a message to your network"
    print "       simplemail alias <name> <ip-address>  Set an alias"
    print "       simplemail alias                      See all aliases"
    print "       simplemail inbox                      Show all received messages"
    print "       simplemail inbox <int>                View a single message"
    print "       simplemail delete <int>               Delete a single message"
    print "       simplemail delete all                 Delete all messages"
    print "       simplemail delete read                Delete all read messages"


if __name__ == "__main__":

    main(sys.argv)


