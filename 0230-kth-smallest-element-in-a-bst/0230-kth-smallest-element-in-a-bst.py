# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def getVals(root):
            if not root:
                return []
            return getVals(root.left) + [root.val] + getVals(root.right)
            
#             if root.left:
#                 self.vals.append(getVals(root.left))
            
#             if root:
#                 self.vals.append(root.val)
            
#             if root.right:
#                 self.vals.append(getVals(root.right))

        
        vals = getVals(root)
        # self.vals = [val for val in self.vals if val is not None]
        # print(vals)
        return vals[k-1]
        

        # if root is None:
        #     return []
        # return (self.kthSmallest(root.left,1) + [root.val] + self.kthSmallest(root.right,1))