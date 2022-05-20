def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G


def centrality(G, v):
    distance_from_start = {}
    path_from_start = {}
    open_list = [v]
    distance_from_start[v] = 0
    path_from_start[v] = [v]
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbour in G[current].keys():
            if neighbour not in distance_from_start:
                distance_from_start[neighbour] = distance_from_start[current] + 1
                path_from_start[neighbour] = path_from_start[current] + [neighbour]
                open_list.append(neighbour)
    return (sum(distance_from_start.values()) + 0.0) / len(distance_from_start)


def read_graph(edges):
    G = {}
    for node_1, node_2 in edges:
        make_link(G, node_1, node_2)
    return G


marveldb = [('spider_man', 'coc1'), ('spider_man', 'maxsec3'), ('thor', 'maxsec3'),
            ('thor', 'wcae1'), ('hulk', 'maxsec3'), ('hulk', 'ff368'),
            ('blackwidow', 'coc1'), ('blackwidow', 'ff368')]
v = 'spider_man'
print(centrality(read_graph(marveldb), v))

