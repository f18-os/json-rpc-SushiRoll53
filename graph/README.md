## jsonClient.py and jsonServer.py
I implemented two new functions inside `node.py` 
* toString(graph)
  * Takes a graph and rearrange it and put it into one line string, so it can be read and re-build later with their corresponding values es connections.
* toGraph(string)
  * Take a string that should be a graph in one line string and build a graph from the string.

Then I made `jsonClient.py` and `jsonServer.py`
* `jsonClient.py`
  * Simply creates and populates a tree
  * It prints the tree and its values
  * Then it uses `toString(graph)` to make it a string 
  * Then request a increment sendint the string to the server
  * Receive a string back, then parse it to a graph and prints it with its new values
  
* `jsonServer.py`
  * Waits for a client's request
  * When increment is called
    * it takes a string, parse it to a graph and calls increment from `node.py`
    * then parse the new incremented graph to a string again
    * it sends it back to the client
  

## Intructions
This directory includes 

* `node.py`: which
  * defines a node class. 
    * contains a name, list of children, and a count that's initially zero
    * implements a `show(graph)` method recursively prints the nodes within graph  
  * An `increment(graph)` method that increments the counts of all nodes within graph. 
* `localDemo.py`: which creates a dag of nodes, which it prints, increments, and prints again.

Your tasks are
* to create 
  * a jsonrpc server that exports the `increment(graph)` function
  * a client that demonstrates the effect of `increment()` being remotely executed on the graph from localDemo.py.
  * a file named `request.json` containing a the manually genrated contents of jsonrpc request to `increment()`
   equivalent to the one produced by your client.   You should use nc to confirm that it's correct.
