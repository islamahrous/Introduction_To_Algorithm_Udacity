#
# Write partition to return a new array with
# all values less then `v` to the left
# and all values greater then `v` to the right
#
import random


def partition(L, v):
    smaller = []
    bigger = []
    for val in L:
        if val < v: smaller += [val]
        if val > v: bigger += [val]
    return smaller, [v], bigger


def top_k(L, k):
    v = L[random.randrange(len(L))]
    left, middle, right = partition(L, v)
    if len(left) == k: return left
    if len(left) + 1 == k: return left + [v]
    if len(left) > k: return top_k(left, k)
    return left + [v] + top_k(right, k-len(left)-1)


L = [12, 20, 25, 30, 15, 7, 17, 45, 43, 54]
k = 3
print(top_k(L, k))