# SimpleMail v0.1

For easily sending messages and reading sent messages in terminal.

Send simple messages to a peer `simplemail Scott "Hey! Working the night shift?"` Notice the use of names like "Scott" which can be aliased to an IP address.  This alias is applied when reading messages as well.  For example, I use the alias: `simplemail alias Milton 192.168.1.128` and then all messages from that address are marked from 'Milton'.

View inbox `simplemail inbox`


```
0 [ ] Stephen: Hey this is just to see how the inbox looks, espec...
1 [ ] Aaron: Hey Milton, How's it going?
2 [ ] Tyler: test
```

Then we read a message  `simplemail inbox 0`

```
From: Stephen Fri Jun 17, 2016 11:32:48 PM
--------------------------------------------------
Hey this is just to see how the inbox looks,
especially when a single message is viewed.
--------------------------------------------------
```
                 
Then back to the inbox
```
0 [x] Stephen: Hey this is just to see how the inbox looks, espec...
1 [ ] Aaron: Hey Milton, How's it going?
2 [ ] Tyler: test
```

And the message is marked as viewed.

Also, messages can be sent to 'all' which means broadcast the message to everyone on your network, So one person can send the same message to everyone.

#### All Commands
 
       simplemail (<ip> or <alias>) \"<Message>\"  Send a message"
       simplemail all \"<Message>\"          Broadcast a message to your network"
       simplemail alias <name> <ip-address>  Set an alias"
       simplemail alias                      See all aliases"
       simplemail inbox                      Show all received messages"
       simplemail inbox <int>                View a single message"
       simplemail delete <int>               Delete a single message"
       simplemail delete all                 Delete all messages"
       simplemail delete read                Delete all read messages"



This is a very early version, so create some issues with ideas for improvements, and expect to see more features!


Also, as of now, I am the only author.