# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:
#             return []
        
        # return ([root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right))
        po = []
        def dfs(root):
            nonlocal po
            if not root:
                return
            
            po.append(root.val)
            dfs(root.left)
            dfs(root.right)
            
        dfs(root)
        # print(po)
        return po