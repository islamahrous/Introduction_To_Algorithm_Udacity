def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G


def connected_components(G, node, marked):
    marked[node] = True
    total_marked = 1
    for neighbour in G[node]:
        if neighbour not in marked:
            total_marked += connected_components(G, neighbour, marked)
    return total_marked


def list_component_sizes(G):
    marked = {}
    for node in G.keys():
        if node not in marked:
            print("components of node", node, ":", connected_components(G, node, marked))


connections = [('a', 'g'), ('a', 'd'), ('d', 'g'), ('g', 'c'), ('b', 'f'),
               ('f', 'e'), ('e', 'h')]
G = {}
for (x, y) in connections:
    make_link(G, x, y)
print(G)
list_component_sizes(G)