class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        make hash map for each node
        use minheap and keep track of total cost and num of stops
        if num of stops > k, return -1
        else keep going and return res as highest cost
        '''
        hashmap = {i:[] for i in range(n)}
        for srcs, des, cost in flights:
            hashmap[srcs].append([des, cost])

        heap = [(0, src, 0)]
        heapq.heapify(heap)
        # res = 0
        # num = 0
        # seen = set()
        dist = {(src, 0): 0}

        while heap:
            cost, node, stops = heapq.heappop(heap)
            # seen.add(node)
            # res += cost
            # num += 1
            # if num > k:
            #     return -1
            if node == dst:
                return cost
            # if node in seen:
            #     continue
            if stops <= k:
                for nodes, costs in hashmap[node]:
                    new_cost = cost + costs
                    state = (nodes, stops + 1)
                    if state not in dist or new_cost < dist[state]:
                        dist[state] = new_cost
                        heapq.heappush(heap, (cost + costs, nodes, stops + 1))

        return -1
        




