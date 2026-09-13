# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False

'''use 2 pointers, fast and slow pointer 
fast pointer goes 2 steps 
slow pointer goes 1 steps
if there's a cycle, 2 pointers will match eventually
'''