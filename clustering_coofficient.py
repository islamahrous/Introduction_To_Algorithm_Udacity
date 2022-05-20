def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G


def clust_co(G, v):
    neighbours = G[v].keys()
    link = 0
    if len(neighbours) == 1:
        return 0.0
    for i in neighbours:
        for j in neighbours:
            if j in G[i]:
                link += 0.5
    return 2 * link / (len(neighbours) * (len(neighbours) - 1))


flights = [('ORD', 'SEA'), ('ORD', 'LAX'), ('ORD', 'DFW'), ('ORD', 'PIT'),
           ('SEA', 'LAX'), ('LAX', 'DFW'), ('ATL', 'PIT'), ('ATL', 'RDU'),
           ('RDU', 'PHL'), ('PIT', 'PHL'), ('PHL', 'PVD')]

G = {}
for (x, y) in flights:
    make_link(G, x, y)
tot = 0
for v in G.keys():
    tot += clust_co(G, v)
print(tot / len(G.keys()))
