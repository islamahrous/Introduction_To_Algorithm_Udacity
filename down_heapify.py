# import random
# L = [random.randrange(1, 100) for i in range(20)]
L = [16, 59, 63, 1, 99, 76, 9, 43, 63, 38, 91, 94, 5, 2, 26, 51, 2, 96, 9, 79]


def left(i):
    return i*2 + 1


def right(i):
    return i*2 + 2


def leaf(L, i):
    return left(i) > len(L)


def one_child(L, i):
    return right(i) == len(L)   # can't be > because it won't satisfy the condition


def down_heapify(L, i):
    if leaf(L, i):
        return L
    if one_child(L, i):
        if L[left(i)] > L[i]:
            return L
        (L[left(i)], L[i]) = (L[i], L[left(i)])
    if min(L[left(i)], L[right(i)]) >= L[i]:    # >= because if equal it is ok
        return L
    if L[left(i)] < L[right(i)]:
        (L[left(i)], L[i]) = (L[i], L[left(i)])
        down_heapify(L, left(i))
        return L
    if L[left(i)] > L[right(i)]:
        (L[right(i)], L[i]) = (L[i], L[right(i)])
        down_heapify(L, right(i))
        return L
    return L


down_heapify(L, 1)
print(L)
