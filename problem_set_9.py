# Write a function, `count`
# that returns the units of time
# where each print statement is one unit of time
# and each evaluation of range also takes one unit of time


def count(n):
    # 2 for print("in a clique...") and range(n)
    # each is calculated once, n for range(j) which
    # is calculated n times and print(i, "is friends with", j)
    # is calculated sum(i) from 0 to (n-1) which is
    # n * (n - 1) / 2
    output = 2 + n + n * (n - 1) / 2
    return output


def clique(n):
    cnt = 0
    print("in a clique...")
    for j in range(n):
        for i in range(j):
            print(i, "is friends with", j)
            cnt += 1
    return cnt


print(count(5))




