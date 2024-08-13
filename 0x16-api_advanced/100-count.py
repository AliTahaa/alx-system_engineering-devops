#!/usr/bin/python3
""" Module """


def count_words(subreddit, words, word_counts={}, after=None):
    """
    Queries the Reddit API and returns the count of words in
    word_list
    """
    import requests

    raw_sub_info = requests.get("https://www.reddit.com/r/{}/hot.json"
                                .format(subreddit),
                                params={"after": after},
                                headers={"User-Agent": "My-User-Agent"},
                                allow_redirects=False)
    if raw_sub_info.status_code != 200:
        return None

    info = raw_sub_info.json()

    hot_titles = [child.get("data").get("title")
                  for child in info
                  .get("data")
                  .get("children")]
    if not hot_titles:
        return None

    words = list(dict.fromkeys(words))

    if word_counts == {}:
        word_counts = {word: 0 for word in words}

    for title in hot_titles:
        split_words = title.split(' ')
        for word in words:
            for s_word in split_words:
                if s_word.lower() == word.lower():
                    word_counts[word] += 1

    if not info.get("data").get("after"):
        sorted_counts = sorted(word_counts.items(), key=lambda kv: kv[0])
        sorted_counts = sorted(word_counts.items(),
                               key=lambda kv: kv[1], reverse=True)
        [print('{}: {}'.format(k, v)) for k, v in sorted_counts if v != 0]
    else:
        return count_words(subreddit, words, word_counts,
                           info.get("data").get("after"))
