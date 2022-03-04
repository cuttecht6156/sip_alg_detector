SIP ALG DETECTOR

Run server.py on the host
Run client.py on the client

Running client.py immeidately sends a SIP Invite to the host, there is no return on the client side.

server.py obviously must be running before running client.py.

Currently this only works within the local host, edit the client.py line 16 to adjust the host's IP address.

P.S. A firewall will likely block any incoming traffic on the host, so beware.