class Twitter:

    """
    Key Concept: 資料結構怎麼樣才快、要從眾多followee 中 fetch top 10 latest怎麼做
    1. Hashmap - Key=ID, Value=hashset 可以讓每個ID查詢,刪除 O(1)
    2. Hashmap - Key=ID, Value=[stamp, ID] 可以排序每個貼文的絕對時間軸
    3. FetchTop10 可以用 "Merge K sorted list" 的想法來想，只需要讓每個 list 的「目前最前緣」  
    互相競爭,誰贏了就往前推進那一個 list 的指標,讓下一個候選補上來
    """

    def __init__(self):
        self.followDic = {}
        self.postDic = {}
        self.stamp = 0  # timestamp, counting backwards: 0, -1, -2

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.postDic:
            self.postDic[userId] = []
        self.postDic[userId].append([self.stamp, tweetId])
        self.stamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []
        
        # 把followee set 存取出來，沒有此userID的話給空 set
        # 用 .copy() 是因為接下來要加入自己,不能動到原始的 followMap 資料
        followee = self.followDic.get(userId, set()).copy()
        followee.add(userId)

        # 先把每個人的最新貼文放進去
        for user in followee:
            # 如果這個user從來沒有發過任何推文,他根本不會是 self.postDic 這個dict裡的一個key
            if user in self.postDic:
                idx = len(self.postDic[user]) - 1
                stamp, tweetid = self.postDic[user][idx]
                heapq.heappush(heap, [stamp, tweetid, idx, user])

        # 把所有人之中最新貼文取出後，補進他的第二新貼文（用min heap）
        while heap and len(res) < 10:
            stamp, tweetid, idx, user = heapq.heappop(heap)
            res.append(tweetid)
            if idx - 1 >= 0:  # if self.postDic[user][idx-1]: 是錯的，-1 出現不行
                idx -= 1
                stamp, tweetid = self.postDic[user][idx]
                heapq.heappush(heap, [stamp, tweetid, idx, user])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followDic:
            self.followDic[followerId] = set()
        
        self.followDic[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followDic[followerId]:
            self.followDic[followerId].remove(followeeId)

        
