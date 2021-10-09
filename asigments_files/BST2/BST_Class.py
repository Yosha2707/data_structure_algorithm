# BST Class
# Send Feedback
# Implement the BST class which includes following functions -
# 1. search
# Given an element, find if that is present in BST or not. Return true or false.
# 2. insert -
# Given an element, insert that element in the BST at the correct position. If element is equal to the data of the node, insert it in the left subtree.
# 3. delete -
# Given an element, remove that element from the BST. If the element which is to be deleted has both children, replace that with the minimum element from right sub-tree.
# 4. printTree (recursive) -
# Print the BST in ithe following format -
# For printing a node with data N, you need to follow the exact format -
# N:L:x,R:y
# where, N is data of any node present in the binary tree. x and y are the values of left and right child of node N. Print the children only if it is not null.
# There is no space in between.
# You need to print all nodes in the recursive format in different lines.


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    
    def __init__(self):
        self.root = None
        self.numNodes = 0
    
    
    def printTreeHelper(self, root):
        if root == None:
            return 
        
        print(root.data, end=":")
        
        if root.left != None:
            print('L', end=":")
            print(root.left.data, end = ",")
            
        if root.right != None:
            print('R', end=":")
            print(root.right.data)
        else:
            print()
            
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)
        
    def printTree(self):
        self.printTreeHelper(self.root)
    
    def searchHelper(self, root, data):
        if root == None:
            return False
        
        if root.data == data:
            return True 
        
        if data >= root.data:
            return self.searchHelper(root.right, data)
        else:
            return self.searchHelper(root.left, data)
        
    def search(self, data):
        return self.searchHelper(self.root, data)

    
    def insertHelper(self, root, data):
        if root == None:
            return BinaryTreeNode(data)
        else:
            if data <= root.data:
                root.left = self.insertHelper(root.left, data)
            else:
                root.right = self.insertHelper(root.right, data)
                
            return root
                    
    def insert(self, data):
        self.numNodes = self.numNodes + 1
        root = self.insertHelper(self.root, data)
        self.root = root
	
    def minOfTree(self, root):
        if root == None:
            return 10000000
        
        if root.left == None:
            return root.data

        return self.minOfTree(root.left)



    def deleteHelper(self, root, data):
        if root == None:
            return False, None

        if data < root.data:
            isDeleted , rootleft = self.deleteHelper(root.left, data)
            root.left = rootleft
            return isDeleted, root
        elif data > root.data:
            isDeleted, rootRight = self.deleteHelper(root.right, data)
            root.right = rootRight
            return isDeleted, root
        elif data == root.data:
            if root.left == None and root.right == None:
                return True, None
            elif root.right == None:
                return True, root.left
            elif root.left == None:
                return True, root.right
            else:
                minOfRight = self.minOfTree(root.right)
                root.data = minOfRight
                isDeleted , newrootRight = self.deleteHelper(root.right, minOfRight)
                root.right = newrootRight
                return True, root 



    def delete(self, data):
        isDeleted, newRoot = self.deleteHelper(self.root, data)
        if isDeleted == True:
            self.numNodes = self.numNodes - 1
            self.root = newRoot
        
        

    def count(self):
        return self.numNodes
        
b = BST()
q = int(input())
while (q > 0) :
    li = [int(ele) for ele in input().strip().split()]
    choice = li[0]
    q-=1
    if choice == 1:
        data = li[1]
        b.insert(data)
    elif choice == 2:
        data = li[1]
        b.delete(data)
    elif choice == 3:
        data = li[1]
        ans = b.search(data)
        if ans is True:
            print('true')
        else:
            print('false')
    else:
        b.printTree()