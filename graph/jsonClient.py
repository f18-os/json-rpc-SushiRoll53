import socket
from node import *
from bsonrpc import JSONRpc
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
	JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)

# Cut-the-corners TCP Client:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50001))

rpc = JSONRpc(s,framing_cls=JSONFramingNone)
server = rpc.get_peer_proxy()

# Creates a graph
leaf1 = node("leaf1")
leaf2 = node("leaf2")
root = node("root", [leaf1, leaf1, leaf2])

# Show graph before increment
print("graph before increment")
root.show()

# Make graph into a string
strRoot = toString(root)
# Execute in server:
root2 = server.increment(strRoot)
root2 = toGraph(root2)
print("graph after increment")
root2.show()


rpc.close() # Closes the socket 's' also


