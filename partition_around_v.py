#
# Write partition to return a new array with
# all values less then `v` to the left
# and all values greater then `v` to the right
#

def partition(L, v):
    P = []
    # your code here
    left, right = rank(L, v)
    right.remove(v)
    P = left + right
    P.insert(len(left), v)
    return P


def rank(L, v):
    pos = 0
    left = []
    right = []
    for val in L:
        if val < v:
            pos += 1
            left.append(val)
        else:
            right.append(val)
    return left, right


L = [12, 20, 25, 30, 15, 7, 17, 45, 43, 54]
v = 17
print(partition(L, v))