# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.vals = []
        def getVals(root):
            if not root:
                pass
            
            if root.left:
                self.vals.append(getVals(root.left))
                
            
            self.vals.append(root.val)
            
            if root.right:
                self.vals.append(getVals(root.right))
        
        getVals(root)
        self.vals = [val for val in self.vals if val is not None]
        # print(self.vals)
        return self.vals[k-1]
        
        