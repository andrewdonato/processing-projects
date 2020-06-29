root = None
nodeToDraw = None
maxDepth = None
root = None
count = 0           
maxDepthNode = None
nodes = {}
seedValue = 100
nodeFrequency = 5 #lower is more

class Node:
    def __init__(self, data, parentNode, depth, color):
        self.left = None
        self.right = None
        self.data = data
        self.depth = depth
        self.parent = parentNode
        self.x = None
        self.y = None
        self.color = color
        
    def printData(self):
        print(self.data)
        
    def insert(self, data, parentNode=None, depth=0, color=255):
        global nodes
        newDepth = self.depth + 1
        if self.data:
            # print "parentNode : %s" %(parentNode.data)
            # currentNode = Node(data, self, newDepth, color-20)
            if data < self.data:
                if self.left == None:
                    self.left = Node(data, self, newDepth, color-20)
                    # print "leftNode newData : %s, self.data : %s" %(data, self.data)
                    # adds to nodes dictionary
                    # nodes[data] = Node(data, self, newDepth, color-20)
                    # adds to nodes dictionary
                    nodes[data] = self.left
                else:
                    self.left.insert(data, self, newDepth, color-20)
                    # print "left.insert newData : %s, self.data : %s" %(data, self.data)
            elif data > self.data:
                if self.right == None:
                    self.right = Node(data, self, newDepth, color-20)
                    # print "rightNode newData : %s, self.data : %s" %(data, self.data)
                    # adds to nodes dictionary
                    # nodes[data] = Node(data, self, newDepth, color-20)
                    nodes[data] = self.right
                else:
                    self.right.insert(data, self, newDepth, color-20)
                    # print "right.insert newData : %s, self.data : %s" %(data, self.data)
            else: 
                pass
                # print "Node %s already exists" %(self.data)
            
        else:
            self.data = data
    
    def printTreeInorder(self):
        if self.left:
            self.left.printTreeInorder()
        # print(self.data)
        print "data: %s, depth: %s" %(self.data, self.depth)
        if self.right:
            self.right.printTreeInorder()
    
    def printTreePreorder(self):
       # print(self.data)        
       print "data: %s, depth: %s" %(self.data, self.depth)
       if self.left:
           self.left.printTreePreorder()
       if self.right:
           self.right.printTreePreorder()
    
    def printTreePostorder(self):
        if self.left:
            self.left.printTreePostorder()
        if self.right:
            self.right.printTreePostorder()
        # print(self.data)
        print "data: %s, depth: %s" %(self.data, self.depth)
        
    def findCoordinates(self, root):        
        self.x = width/2 + self.data - root.data
        self.y = height/(self.depth+1) - 20


    def drawTreePreorder(self, root):
        self.findCoordinates(root)
        rectWidth = 10
        rectHeight = 10
        

        # if self.data == maxDepthNode.data:
        if self.depth == maxDepth:
            fill(240, self.color, 20)
        else:        
            fill(34, self.color, 34)
        # pushMatrix()
        # translate(self.x, self.y)
        # rotate(45)
        if self.data != root.data:
            # textSize(12) #might be default
            textSize(11)
            text(self.data, self.x-5, self.y+5)
            # rect(self.x, self.y, rectWidth, rectHeight)
        # popMatrix()
        # rotate(-45)
        if self.left:
            self.left.drawTreePreorder(root)
        if self.right:
            self.right.drawTreePreorder(root)
        
        # stroke(205,133,63)
        stroke(139,69,19)
        if self.parent:
            line(self.parent.x, self.parent.y, self.x, self.y)

def createTree(root):
    randomized = int(random(0, 9999))
    randomSeed(randomized)
    # randomSeed(456)
    # randomSeed(4296)
    # randomSeed(4747)
    # randomSeed(1358) #10
    # randomSeed(7427)
    # randomSeed(8458)
    randomSeed(1326)
    print "randomSeed(%s)" %(randomized)    
    
    # root.insert(90)
    # root.insert(70)
    # for i in range(0, 200, 5):
    for i in range(0, 2*seedValue, nodeFrequency):
        # root.insert(i, root)
        # root.insert(int(random(0, 200)), root)
        root.insert(int(random(0, 2*seedValue)), root)
    

def findMaxHeightTopToBottom(node, pDepth):    
    global maxDepth, count, maxDepthNode
    if node == None:
        return
    nDepth = pDepth + 1
    if (nDepth > maxDepth):
        maxDepth = nDepth
        maxDepthNode = node
    count = count + 1
    findMaxHeightTopToBottom(node.left, nDepth)
    findMaxHeightTopToBottom(node.right, nDepth)
                                                        
def findMaxHeightBottomToTop(node):
    if node == None:
        return -1
    return max(findMaxHeightBottomToTop(node.left), findMaxHeightBottomToTop(node.right)) + 1

def isBalancedBottomToTop(node):
    if node == None:
        return 0
    leftHeight = isBalancedBottomToTop(node.left)
    rightHeight = isBalancedBottomToTop(node.right)
    
    if (leftHeight == -1) or (rightHeight == -1):
        return -1
    if abs(leftHeight - rightHeight) > 1:
        return -1
    # print "self.data : %s, leftHeight : %s , rightHeight : %s" %(node.data, leftHeight, rightHeight)
    
    return 1 + max(leftHeight, rightHeight)
    
def findLowestCommonAncestorWithParent(nodeAKey, nodeBKey):
    if (nodeAKey not in nodes) or (nodeBKey not in nodes):
        return
    aNode = nodes[nodeAKey]
    bNode = nodes[nodeBKey]
    if aNode == None or bNode == None:
        return -1
    
    aPointer = aNode
    bPointer = bNode
    # print "aNode : %s, parent : %s" %(aNode.data, aNode.parent.data)
    # print "bNode : %s, parent : %s" %(bNode.data, bNode.parent.data)
    print "aPointer : %s, parent : %s" %(aPointer.data, aPointer.parent.data)
    print "bPointer : %s, parent : %s" %(bPointer.data, bPointer.parent.data)
    
    # find aDepth
    aDepth = -1
    while aPointer != None:
        aDepth += 1
        aPointer = aPointer.parent
        # print aPointer.data
        
    # find bDepth
    bDepth = -1
    while bPointer != None:
        bDepth += 1
        bPointer = bPointer.parent
        # print bPointer.data
        
    print "aDepth : %s, bDepth : %s" %(aDepth, bDepth)
    
    if aDepth > bDepth:
        x = aNode
        y = bNode
    else:
        x = bNode
        y = aNode
    
    for i in range(0, abs(aDepth - bDepth)):
        x = x.parent
    
    while x != y:
        x = x.parent
        y = y.parent
    
    return x.data
    
def findLowestCommonAncestorWithoutParent(nodeAKey, nodeBKey):
    nodeA = nodes[nodeAKey]
    nodeB = nodes[nodeBKey]
    



def setup():
    global maxDepth, nodeToDraw, root, count
    size(500, 500)   
    # root = Node(100, None, 0, 255)     
    root = Node(seedValue, None, 0, 255)
    nodeToDraw = root
    createTree(root)
    findMaxHeightTopToBottom(root, -1)
    print "Bottom to Top : %s"    %(findMaxHeightBottomToTop(root))
    print "isBalanced : %s" %(isBalancedBottomToTop(root))
    
    print "count : %s" %(count)
    print "maxDepth : %s" %(maxDepth)
    print "maxDepthNode.data: %s" %(maxDepthNode.data)
    print "Nodes : %s" %(nodes.keys())
    # for x in nodes:
        # print "key : %s, node : %s, parent : %s" %(x, nodes[x].data, nodes[x].parent.data)
    # print "Find LCA of %s and %s : %s" %("139", "149", findLowestCommonAncestorWithParent(139, 149))
    # print "Find LCA of %s and %s : %s" %("18", "76", findLowestCommonAncestorWithParent(18, 76))
    print "Find LCA-with-Parents of %s and %s : %s" %("10", "68", findLowestCommonAncestorWithParent(10, 68))

    
def draw():
    background(0)
    nodeToDraw.drawTreePreorder(root)
