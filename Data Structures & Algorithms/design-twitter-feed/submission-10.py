class Twitter:
    """
    1. follow: hashmap(id, set())
    2. postTweet: hashmap(id, [timestamp, tweetId])
    3. getFeed: all followee + self add latest to min heap, fetch latest user's post
    then push in the user's second latest post
    """
    def __init__(self):
        self.followDic = {}
        self.postDic = {}
        self.seq = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.postDic:
            self.postDic[userId] = []
        self.postDic[userId].append([self.seq, tweetId])
        self.seq -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followee = self.followDic.get(userId, set()).copy()
        followee.add(userId)

        res = []
        heap = [] #[seq, tweetid, userId, idx] so later on we got ref to next item

        for user in followee:
            if user in self.postDic:
                idx = len(self.postDic[user]) - 1  # pick the one in the end
                seq, tweetid = self.postDic[user][idx]
                heapq.heappush(heap, [seq, tweetid, user, idx])

        while heap and len(res) < 10:
            seq, tweetid, userId, idx = heapq.heappop(heap)
            res.append(tweetid)
            if idx - 1 >= 0:  # self.postDic[user][idx-1] might be [-1],[-2]
                idx -= 1
                seq, tweetid = self.postDic[userId][idx]
                heapq.heappush(heap, [seq, tweetid, userId, idx])

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followDic:
            self.followDic[followerId] = set()
        self.followDic[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followDic[followerId]:
            self.followDic[followerId].remove(followeeId)
