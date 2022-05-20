import math


def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G


# program for RING network
# a_ring = {}
# n = 5
# for i in range(n):
#     make_link(a_ring, i, (i+1) % n)
# print(len(a_ring))
# print(sum([len(a_ring[node]) for node in a_ring.keys()])/2)
# print(a_ring)


# program for GRID network
a_ring = {}
n = 256
side = int(math.sqrt(n))
for i in range(side):
    for j in range(side):
        if i < (side - 1):
            make_link(a_ring, (i, j), ((i+1), j))
        if j < (side - 1):
            make_link(a_ring, (i, j), (i, (j+1)))

print(len(a_ring))
print(sum([len(a_ring[node]) for node in a_ring.keys()])/2)
print(a_ring)
