class node:
    def __init__(self, name, children = []):
        self.name = name
        self.children = children
        self.val = 0
    def show(self, level=0):
        print("%s%s val=%d:" % (level*"  ", self.name, self.val))
        for c in self.children: 
            c.show(level + 1)


def increment(graph):
    graph.val += 1;
    for c in graph.children:
        increment(c)

def toString(graph):
    # Takes a graph and parse it in one long string, divide it by dollar sings $
    data = graph.name+"$"+str(graph.val)+"$"
    for c in graph.children:
        data += c.name+"$"+str(c.val)+"$"
    return data

def toGraph(strGraph):
    # Takes the string version of a graph and built a tree from it
    splstr = strGraph.split("$")
    root = node(splstr[0], [node(splstr[i]) for i in range(2,len(splstr)-1,2)])
    root.val = int(splstr[1])
    root.children[0] = root.children[1]
    for i,c in zip(range(3,len(splstr)-1,2),root.children):
        c.val = int(splstr[i])
    return root
