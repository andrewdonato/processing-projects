nodeToDraw = None
maxDepth = None
root = None



class Node:
    def __init__(self, data, depth = 0):
        self.left = None
        self.right = None
        self.data = data
        self.depth = depth
        
    def printData(self):
        print(self.data)
        
    def insert(self, data, depth=0):
        newDepth = self.depth + 1
        if self.data:
            if data < self.data:
                if self.left == None:
                    self.left = Node(data, newDepth)
                else:
                    self.left.insert(data, newDepth)
            elif data > self.data:
                if self.right == None:
                    self.right = Node(data, newDepth)
                else:
                    self.right.insert(data, newDepth)
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
        

    def drawTreePreorder(self, root):
        # rect(x,y,w,h)
        rectWidth = 10
        rectHeight = 10
        xDifference = self.data - root.data
        yDifference = self.depth
        rect(width/2 + 1 * xDifference, height-2*rectHeight-self.depth*20, rectWidth, rectHeight)
        if self.left:
            self.left.drawTreePreorder(root)
        if self.right:
            self.right.drawTreePreorder(root)

            
def findMaxHeight(node, pDepth, maxDepthNode):    
    global maxDepth
    if node == None:
        return
    nDepth = pDepth + 1
    if (nDepth > maxDepth):
        maxDepth = nDepth
        madDepthNode = node
    findMaxHeight(node.left, nDepth, maxDepthNode)
    findMaxHeight(node.right, nDepth, maxDepthNode)
                                            
            

def setup():
    global nodeToDraw
    size(500, 500)        

def draw():
    # nodeToDraw.drawTreePreorder(root)
    root.drawTreePreorder(root)

    # rect(width/2, height/10, 20, 20)


    


# root = Node(4, 0)
# for i in range(0, 8, 1):
#     root.insert(i)
root = Node(100, 0)
for i in range(0, 200, 10):
    # root.insert(i)
    root.insert(int(random(0, 200)))



# print "This is root: %s" %(root.data)
# print "printTreeInorder:"
# root.printTreeInorder()
# print "printTreePreorder:"
# root.printTreePreorder()
# print "printTreePostorder:"
# root.printTreePostorder()
# nodeToDraw = root


findMaxHeight(root, -1, root)
print maxDepth
