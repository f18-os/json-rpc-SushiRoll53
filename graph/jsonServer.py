import socket
from node import *
from bsonrpc import JSONRpc
from bsonrpc import request, service_class
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
	JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)


# Class providing functions for the client to use:
@service_class
class ServerServices(object):

  @request
  def increment(self, strRoot):
    fileR = open("request.json","r")
    line = fileR.readline()
    # verify if the String form of the graph
    # it is similar to the one on the json file
    if line is not strRoot:
      root2 = toGraph(strRoot)
      increment(root2)
      root2 = toString(root2)
      return root2
    else:
      return strRoot

# Quick-and-dirty TCP Server:
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('localhost', 50001))
ss.listen(10)

while True:
  s, _ = ss.accept()
  # JSONRpc object spawns internal thread to serve the connection.
  JSONRpc(s, ServerServices(),framing_cls=JSONFramingNone)
