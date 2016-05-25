from __future__ import absolute_import
from __future__ import unicode_literals

def tweet_url(tweet, mobile=False):
    domain = "mobile.twitter.com" if mobile else "twitter.com"

    return "http://{}/{}/status/{}".format(
        domain, tweet.author.screen_name, tweet.id)
