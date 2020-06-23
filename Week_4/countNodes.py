#Approach 1: Time Complexity: O(n) - Best, Average, Worst
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
    
        

#Approach 2: Time Complexity: O(2h) where h is the height. Best case.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        hleft, hright = 0, 0
        pleft, pright = root, root
        while pleft!= None:
            hleft+=1
            pleft = pleft.left
        
        while pright!= None:
            hright+=1
            pright = pright.right
        
        if hleft == hright:
            return (2**hleft) -1
        
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
    
        
        