class Solution:
    def leastInterval(self, tasks, n):
        count = Counter(tasks)
        heap = [-cnt for cnt in count.values()]
        heapq.heapify(heap)

        time = 0
        q = deque()

        while heap or q:
            time += 1
            if heap:
                cnt = 1 + heapq.heappop(heap)

                if cnt:
                    q.append((cnt, time + n))

            if q and q[0][1] == time:
                cnt, _ = q.popleft()
                if cnt:
                    heapq.heappush(heap, cnt)

        return time

        

        