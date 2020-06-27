nodeToDraw = None
maxDepth = None
root = None
count = 0            


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
        # self.y = height*maxDepth/(self.depth + 1)
        self.y = height/(self.depth+1) - 20
        # fraction = height/maxDepth    
        # self.y = height - (self.depth*fraction)
        # self.y = height-2*10-self.depth*20
        

    def drawTreePreorder(self, root):
        self.findCoordinates(root)
        # rect(x,y,w,h)
        rectWidth = 10
        rectHeight = 10
        # if self.parent == None:
        #     fill(0,255,0)
        # else:
        #     fill(self.color, 0, 0)
        # fill(self.color, 0, 0)
        fill(34, self.color, 34)

        rect(self.x, self.y, rectWidth, rectHeight)
        if self.left:
            self.left.drawTreePreorder(root)
        if self.right:
            self.right.drawTreePreorder(root)
        
        if self.parent:
            line(self.parent.x, self.parent.y, self.x, self.y)

    
    # def drawTreePreorder(self, root):
    #     self.findCoordinates(root)
    #     # rect(x,y,w,h)
    #     rectWidth = 10
    #     rectHeight = 10
    #     xDifference = self.data - root.data
    #     yDifference = self.depth
    #     rect(width/2 + 1 * xDifference, height-2*rectHeight-self.depth*20, rectWidth, rectHeight)
    #     if self.left:
    #         self.left.drawTreePreorder(root)
    #     if self.right:
    #         self.right.drawTreePreorder(root)


def findMaxHeightTopToBottom(node, pDepth, maxDepthNode):    
    global maxDepth, count
    if node == None:
        return
    nDepth = pDepth + 1
    if (nDepth > maxDepth):
        maxDepth = nDepth
        madDepthNode = node
    
    # if  node.parent:
    #     print "node: %s, parent: %s" %(node.data, node.parent.data)
    # else:
    #     print "node: %s, has no parent" %(node.data)
    count = count + 1
    
    findMaxHeightTopToBottom(node.left, nDepth, maxDepthNode)
    findMaxHeightTopToBottom(node.right, nDepth, maxDepthNode)
                                                        

def setup():
    global maxDepth, nodeToDraw
    size(500, 500)        
    findMaxHeightTopToBottom(root, -1, root)
    print count
    # print maxDepth

def draw():
    # nodeToDraw.drawTreePreorder(root)
    root.drawTreePreorder(root)
    # line(width/2, 0, width/2, height)
    
    # rect(width/2, height/2, 20, 20)
    # rect(width/2, height/4, 20, 20)
    # rect(width/2, height/8, 20, 20)
    # rect(width/2, height/10, 30, 30)
    # rect(width/2, height/20, 40, 40)


    


# root = Node(4, 0)
# for i in range(0, 8, 1):
#     root.insert(i)
randomized = int(random(0, 9999))
randomSeed(randomized)
# randomSeed(456)
# randomSeed(4296)
# randomSeed(4747)
print "randomSeed(%s)" %(randomized)

root = Node(100, None, 0, 255)

for i in range(0, 200, 5):
    # root.insert(i, root)
    root.insert(int(random(0, 200)), root)



# print "This is root: %s" %(root.data)
# print "printTreeInorder:"
# root.printTreeInorder()
# print "printTreePreorder:"
# root.printTreePreorder()
# print "printTreePostorder:"
# root.printTreePostorder()
# nodeToDraw = root
