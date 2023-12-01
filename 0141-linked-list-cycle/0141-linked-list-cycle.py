# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
#         curr = head
#         valset = set()
#         while curr is not None:
#             if curr not in valset:
#                 valset.add(curr)
#                 curr = curr.next
#             else:
#                 return True
            
            
#         return False

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
            if slow == fast:
                return True
        return False