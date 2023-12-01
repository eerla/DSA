# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        
        while curr:
            #track next node
            nextNode = curr.next
            #update current node's next node 
            curr.next = prev
            # Update prev and current
            prev = curr
            curr = nextNode
            # print(f'nextnode: {nextNode}, prev: {prev}, curr: {curr}', end = '======')
        return prev