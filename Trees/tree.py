class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data) 
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print (self.data)
        if self.right:
            self.right.printTree()

    def height(self, root):
        if root is None:
            return -1
        else:
            if root.left==None and root.right==None:
                return max(self.height(root.left), self.height(root.right))+0
            else:
                return max(self.height(root.left), self.height(root.right))+1
    def traverse(self, queue, ans):
        treeNodes = ans
        if len(queue) == 0:
            return []
        node = queue[0]
        queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        ans.append(node.data)
        self.traverse(queue, ans)
        return ans

my_queue = []     
leaves = input("enter nodes: ")
leaves = leaves.split(' ')
leaves = [int(i) for i in leaves]
root = Node(leaves[int(0)])
my_queue.append(root)
for each in leaves[1:]:
    root.insert(int(each))
# root = Node(12)
# root.insert(6)
# root.insert(14)
# root.insert(3)
# root.printTree()
# print(root.height(root))
print(root.traverse(my_queue, []))