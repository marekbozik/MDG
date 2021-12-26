
class Node:
    def __init__(self, name : str):
        self.name = name
        self.lchild = []
    def addChild(self, name):
        self.lchild.append(name)


nodes = {}

node_file = open('nodes.txt', 'r')
for node in node_file.readlines():
    nodes[node.strip()] = Node(node.strip())
    


children_file = open('children.txt', 'r')
for child in children_file.readlines():
    n = ""
    for c in child:
        n += c
        if c == ']':
            break
    con = False
    appe = ""
    for c in child:
        if c == '>':
            con = True
            continue
        if con == False:
            continue
        appe += c
    nodes[n].lchild.append(appe.strip())

def loop(srcN, currN):
    if srcN.name == currN.name:
        print(srcN.name)
        return
    for c in nodes[currN.name].lchild:
        loop(srcN, nodes[c])


for n in nodes:
    for c in nodes[n].lchild:
        loop(nodes[n], nodes[c])



print('end')