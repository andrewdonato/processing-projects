root = None
nodeToDraw = None
maxDepth = None
root = None
count = 0           
maxDepthNode = None


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
        newDepth = self.depth + 1
        if self.data:
            if data < self.data:
                if self.left == None:
                    self.left = Node(data, self, newDepth, color-20)
                else:
                    self.left.insert(data, self, newDepth, color-20)
            elif data > self.data:
                if self.right == None:
                    self.right = Node(data, self, newDepth, color-20)
                else:
                    self.right.insert(data, self, newDepth, color-20)
            else: 
                print "Node %s already exists" %(self.data)
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

        if self.data == maxDepthNode.data:
            fill(240, self.color, 20)
        else:        
            fill(34, self.color, 34)
        # pushMatrix()
        # translate(self.x, self.y)
        # rotate(45)
        rect(self.x, self.y, rectWidth, rectHeight)
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
    print "self.data : %s, leftHeight : %s , rightHeight : %s" %(node.data, leftHeight, rightHeight)
    
    return 1 + max(leftHeight, rightHeight)
    


def createTree(root):
    randomized = int(random(0, 9999))
    randomSeed(randomized)
    # randomSeed(456)
    # randomSeed(4296)
    # randomSeed(4747)
    # randomSeed(1358) #10
    randomSeed(7427)
    print "randomSeed(%s)" %(randomized)    
    
    # root.insert(90)
    # root.insert(70)
    for i in range(0, 200, 5):
        
        # root.insert(i, root)
        root.insert(int(random(0, 200)), root)


def setup():
    global maxDepth, nodeToDraw, root, count
    size(500, 500)   
    root = Node(100, None, 0, 255)     
    nodeToDraw = root
    createTree(root)
    findMaxHeightTopToBottom(root, -1)
    print "Bottom to Top : %s"    %(findMaxHeightBottomToTop(root))
    print "isBalanced : %s" %(isBalancedBottomToTop(root))
    
    print "count : %s" %(count)
    print "maxDepth : %s" %(maxDepth)
    print "maxDepthNode.data: %s" %(maxDepthNode.data)

def draw():
    background(0)
    nodeToDraw.drawTreePreorder(root)
