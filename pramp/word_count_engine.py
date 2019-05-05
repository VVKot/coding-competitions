from collections import OrderedDict
from typing import List, Dict


def word_count_engine(document: str) -> List[List[str]]:
    word_count = get_word_count(document)
    buckets = get_sorted_word_buckets(word_count)
    return [x for bucket in buckets for x in bucket]


def get_word_count(document: str) -> Dict[str, int]:
    word_count = OrderedDict()  # type: Dict[str, int]
    curr_word = ""
    for ch in document:
        if ch.isalpha():
            curr_word += ch.lower()
        elif ch.isspace() and curr_word:
            increment_dict(word_count, curr_word)
            curr_word = ""
    if curr_word:
        increment_dict(word_count, curr_word)
    return word_count


def increment_dict(dict_: Dict, val: str) -> None:
    if val in dict_:
        dict_[val] += 1
    else:
        dict_[val] = 1


def get_sorted_word_buckets(word_count: Dict) -> List[List[List[str]]]:
    bucket_count = max(word_count.values()) + 1
    buckets = [[] for _ in range(bucket_count)]  # type:  List[List[List[str]]]
    for k, v in word_count.items():
        buckets[v].append([k, str(v)])
    return list(reversed(buckets))
