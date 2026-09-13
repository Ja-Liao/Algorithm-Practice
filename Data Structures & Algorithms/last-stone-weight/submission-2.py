class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # negate values to simulate max heap
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            s1 = -heapq.heappop(heap)  # largest
            s2 = -heapq.heappop(heap)  # second largest

            if s1 != s2:
                heapq.heappush(heap, -(s1 - s2))

        return -heap[0] if heap else 0
