import collections

def duplicates(arr):
    return sum(num//2 for num in collections.Counter(arr).values())