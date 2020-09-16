import praw
import os
import numpy as np
import time


# retrieving info w environment variables
USERNAME = os.environ.get('REDDIT_NLP_USERNAME')
PASSWORD = os.environ.get('REDDIT_NLP_PASSWORD')
CLIENT_ID = os.environ.get('REDDIT_NLP_CLIENT_ID')
CLIENT_SECRET = os.environ.get('REDDIT_NLP_SECRET')
END_OF_COMMENT_STR = '\n -----------------END_OF_COMMENT--------------- \n\n'

reddit= praw.Reddit(user_agent='Comment Extraction (by u/Reddit_nlp_pa)',
                    client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                    username=USERNAME, password=PASSWORD)


def get_r_all_posts(reddit_instance):
    r_all_posts_scores = []
    for r_all_submission in reddit_instance.subreddit('all').hot(limit=1000):
        r_all_posts_scores.append(r_all_submission.score)
    return r_all_posts_scores


print('Starting script')
start = time.time()
r_all_posts = get_r_all_posts(reddit)
posts_ndarray = np.asarray(r_all_posts)
end = time.time()
print(f'Elapsed time {end-start}')
print(f'number of posts: {len(r_all_posts)}')
print(f'upvote mean: {posts_ndarray.mean()}\nupvote min: {posts_ndarray.min()}\nupvote max: {posts_ndarray.max()}\n')
print(f'50th percentile: {np.percentile(posts_ndarray, 50)}')
print(f'20th percentile: {np.percentile(posts_ndarray, 20)}')
print(f'10th percentile: {np.percentile(posts_ndarray, 10)}')
print(f'5th percentile: {np.percentile(posts_ndarray, 5)}')
print(f'1st percentile: {np.percentile(posts_ndarray, 1)}')

print(f'2x2 is :  {{2*2}}')

