# Generate a combination lock graph given a list of nodes
#

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G


def create_combo_lock(nodes):
    G = {}
    for node in nodes[:-1]:
        make_link(G, node, node + 1)
    for node in nodes[1:]:
        if node not in list(G[0]):
            make_link(G, nodes[0], node)
    # your code here
    return G


create_combo_lock([0, 1, 2, 3, 4])
print(create_combo_lock([0, 1, 2, 3, 4]))