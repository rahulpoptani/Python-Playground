'''
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.
void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
'''

from Common.Tags import HEAP, DESIGN, HASHMAP

import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time = 0
        # userId -> list of (-timestamp, tweetId)  [negative for max-heap via min-heap]
        self.tweets = defaultdict(list)
        # followerId -> set of followeeIds
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        # All users whose tweets we care about
        relevant = self.following[userId] | {userId}

        # Seed the heap with each user's most recent tweet
        # Heap entry: (-timestamp, tweetId, userId, index into that user's list)
        heap = []
        for uid in relevant:
            user_tweets = self.tweets[uid]
            if user_tweets:
                idx = len(user_tweets) - 1           # most recent
                neg_time, tweet_id = user_tweets[idx]
                heapq.heappush(heap, (neg_time, tweet_id, uid, idx))

        feed = []
        while heap and len(feed) < 10:
            neg_time, tweet_id, uid, idx = heapq.heappop(heap)
            feed.append(tweet_id)

            # Advance to that user's next (older) tweet
            if idx > 0:
                nidx = idx - 1
                neg_time, tweet_id = user_tweets[idx]
                heapq.heappush(heap, (neg_time, tweet_id, uid, nidx))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)

#  test case
if __name__ == "__main__":
    twitter = Twitter()
    twitter.postTweet(1, 5)
    print(twitter.getNewsFeed(1))  # [5]
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    print(twitter.getNewsFeed(1))  # [6, 5]
    twitter.unfollow(1, 2)
    print(twitter.getNewsFeed(1))  # [5]