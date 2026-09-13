class Solution:
    def leastInterval(self, tasks, n):
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # stores pairs of [remainingCount, timeWhenAvailable]

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1   # add 1 because cnt is negative
                if cnt:  # still tasks remaining
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time

        

        