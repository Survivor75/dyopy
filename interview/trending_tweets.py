from collections import Counter


class TrendingHashTagsService:

    def __init__(self):
        self.hashtags = Counter()

    def get_top_n_hashtags(self, n=10):
        return self.hashtags.most_common(n)

    def update_trending_hashtags(self, tweet):
        hashtags = self.extract_hashtags(tweet)
        self.hashtags.update(hashtags)

    def extract_hashtags(self, tweet):
        return [i for i in tweet.split() if i.startswith("#")]


if __name__ == '__main__':

    trending_hashtags = TrendingHashTagsService()

    # Using a context manager here, in case when file size is huge it will not load the entire file into memory all at once

    with open("tweets.txt", 'r', encoding='utf-8') as reader:
        tweet = reader.readline()

        while tweet != '':

            trending_hashtags.update_trending_hashtags(tweet)
            tweet = reader.readline()

    result = trending_hashtags.get_top_n_hashtags(50)

    print(result)
