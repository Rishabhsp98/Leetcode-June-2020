# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root == None:
            return 0
        self.total = 0
        self.findSum(root, 0)
        return self.total
    
    def findSum(self, root, summ):
        if root == None:
            return
        summ = summ * 10 + root.val
        
        if root.left == None and root.right == None:
            self.total+= summ
            return
        
        self.findSum(root.left, summ)
        self.findSum(root.right, summ)
        
    
        