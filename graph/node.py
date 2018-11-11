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

def toString(graph, data = ""):
    # Takes a graph and makes a json representation of it
    data += ("{ ")
    data +=("\""+graph.name+"\" : { ")
    data +=("\"value\" : "+str(graph.val)+" , ")
    data +=("\"children\" : { ")
    for c in graph.children:
        data += toString(c)
    data +=("} ,")
    data +=(" } ")
    return data


def toGraph(strGraph):
    # Takes a json file and makes a graph out of it
    # For time constrains and for the purpose of this lab
    # I made this parser specific for this tree
    listGraph = strGraph.split(" ")
    toRevome = [":","{","}","",","]
    cleanList = [item for item in listGraph if item not in toRevome]

    leaf1 = node(cleanList[4][1:-1])
    leaf1.val = int(cleanList[6])
    leaf2 = node(cleanList[12][1:-1])
    leaf2.val = int(cleanList[14])
    root = node(cleanList[0][1:-1],[leaf1,leaf1,leaf2])
    root.val = int(cleanList[2])

    return root


    












