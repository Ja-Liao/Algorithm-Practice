class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        heapq.heapify(heap)
        users = self.followMap[userId] | {userId}

        for user in users:
            for t, tweetId in self.tweetMap[user][-10:]:  # Only last 10 to save time
                heapq.heappush(heap, (-t, tweetId))  # max-heap behavior using negative timestamp

        res = []
        for _ in range(min(10, len(heap))):
            res.append(heapq.heappop(heap)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
