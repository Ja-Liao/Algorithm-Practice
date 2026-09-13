"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        temp = curr
        hashmap = {None:None}

        while curr:
            node = Node(curr.val)
            hashmap[curr] = node
            curr = curr.next

        curr = temp
        while curr:
            copy = hashmap[curr]
            copy.next = hashmap[curr.next]
            copy.random = hashmap[curr.random]
            curr = curr.next

        return hashmap[temp]
        

        return temp