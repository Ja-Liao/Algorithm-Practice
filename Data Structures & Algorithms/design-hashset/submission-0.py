class ListNode:
    def __init__(self, key = -1):
        self.next = None
        self.key = key

class MyHashSet:
    def __init__(self):
        self.hash = [ListNode(0) for _ in range(10000)]

    def add(self, key: int) -> None:
        cur = self.hash[key % 10000]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        cur = self.hash[key % 10000]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        cur = self.hash[key % 10000].next
        while cur:
            if cur.key == key:
                return True
            cur = cur.next

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)