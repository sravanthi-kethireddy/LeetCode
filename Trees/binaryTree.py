class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# Function to insert nodes in level order  
def insertLevelOrder(arr, root, i, n): 
    # Base case for recursion  
    if i < n: 
        temp = Node(arr[i])  
        root = temp  
  
        # insert left child  
        root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n) 

  
        # insert right child  
        root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n) 
    # print(root.data)
    return root
# InOrder fashion  
def inOrder(root): 
    if root != None: 
        inOrder(root.left)  
        print(root.data,end=" ")  
        inOrder(root.right) 
def isValidBST(root):
        return isValidBSTRecu(root, float("-inf"), float("inf"))

def isValidBSTRecu(root, low, high):
    if root is None:
        return True

    return low < root.data and root.data < high \
        and isValidBSTRecu(root.left, low, root.data) \
        and isValidBSTRecu(root.right, root.data, high)

def isValidBST2(root):
    prev, cur = None, root
    while cur:
        if cur.left is None:
            if prev and prev.data >= cur.data:
                return False
            prev = cur
            cur = cur.right
        else:
            node = cur.left
            while node.right and node.right != cur:
                node = node.right

            if node.right is None:
                node.right = cur
                cur = cur.left
            else:
                if prev and prev.data >= cur.data:
                    return False
                node.right = None
                prev = cur
                cur = cur.right

    return True


# Driver Code 
if __name__ == '__main__': 
    arr = [1, 2, 3, 4, 5, 6, 6, 6, 6] 
    arr = [1,2,3]
    n = len(arr) 
    root = None
    root = insertLevelOrder(arr, root, 0, n)  
    ans = isValidBST2(root)
    print(ans)
    # inOrder(root) 
