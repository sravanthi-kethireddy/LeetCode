class Node: 
  
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None
def isBst(root):
    stack, inOrder = [], float('-inf')
    while stack or root:
        while root:
            stack.append(root)
            print(stack)
            # print(root.data)
            root = root.left
        root = stack.pop()
        if root.val <= inOrder:
            return False
        inOrder = root.val
        root = root.right
    return True
def isValidBST(root, l=None, r=None):
    if root == None:
        return True
    if (l!=None and root.data<=l.data):
        return False
    if (r!=None and root.data>=r.data):
        return False
    return(isValidBST(root.left, l, root) and isValidBST(root.right,root,r))


def traversal(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while len(queue)>0:
        print (queue[0].data)
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

def levelOrderBFS(root):
    res, queue = [], [(root, 0)]
    while queue:
        curr, level = queue.pop(0)
        if curr:
            if len(res) < level + 1:
                res.append([])
            res[level].append(curr.data)
            queue.append((curr.left, level+1))
            queue.append((curr.right, level+1))
    for each in range(len(res)):
        if each % 2 != 0:
            res[each]=res[each][::-1]
    return res

def levelOrderDFS(root):
    res, stack = [], [(root, 0)]
    while stack:
        curr, level = stack.pop()
        if curr:
            if len(res) < level + 1:
                res.append([])
            res[level].append(curr.data)
            stack.append((curr.right, level+1))
            stack.append((curr.left, level+1))
    return res

root = Node(4) 
root.left = Node(2) 
root.right = Node(5) 
root.left.left = Node(1) 
root.left.right = Node(3) 
# print(isBst(root))
# print(isValidBST(root,None, None))
# traversal(root)
print(levelOrderBFS(root))
# print(levelOrderDFS(root))


# This function returns overall maximum path sum in 'res' 
# And returns max path sum going through root 
def findMaxUtil(root): 
      
    # Base Case 
    if root is None: 
        return 0 
  
    # l and r store maximum path sum going through left  
    # and right child of root respetively 
    l = findMaxUtil(root.left) 
    r = findMaxUtil(root.right) 
      
    # Max path for parent call of root. This path  
    # must include at most one child of root 
    max_single = max(max(l, r) + root.data, root.data) 
      
    # Max top represents the sum when the node under 
    # consideration is the root of the maxSum path and 
    # no ancestor of root are there in max sum path 
    max_top = max(max_single, l+r+ root.data) 
  
    # Static variable to store the changes 
    # Store the maximum result 
    findMaxUtil.res = max(findMaxUtil.res, max_top)  
  
    return max_single 
  
# Return maximum path sum in tree with given root 
def findMaxSum(root): 
      
    # Initialize result 
    findMaxUtil.res = float("-inf") 
      
    # Compute and return result 
    findMaxUtil(root) 
    return findMaxUtil.res 