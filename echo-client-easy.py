import socket
import sys
import time

def get_constants(prefix):
    """Create a dictionary mapping socket module constants to their names."""
    return dict( (getattr(socket, n), n)
                 for n in dir(socket)
                 if n.startswith(prefix)
                 )

families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

# Create a TCP/IP socket
sock = socket.create_connection(('localhost', 10000))

print >>sys.stderr, 'Family  :', families[sock.family]
print >>sys.stderr, 'Type    :', types[sock.type]
print >>sys.stderr, 'Protocol:', protocols[sock.proto]
print >>sys.stderr

# Send data
message = 'This is the message.  It will be repeated.'
print >>sys.stderr, 'sending "%s"' % message
sock.sendall(message)

while True:
    data = raw_input("please input command: ")
    try:
        if data == "q":
            confirm = raw_input("do you want to disconnect? yes or not: ")
            if confirm == "yes":
                print >>sys.stderr, 'you are disconnecting...'
                break
            else:
                print >>sys.stderr, 'rolling back...'
        else:
            print >>sys.stderr, 'data prepared.'
    finally:
        sock.sendall(data)
        print >>sys.stderr, 'sent to server.'
        time.sleep(2)

sock.close()
