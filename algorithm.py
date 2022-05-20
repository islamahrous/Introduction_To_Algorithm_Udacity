# my algorithm
"""def create_tour_algorithm_1(nodes):
    rotated_nodes = collections.deque(nodes)
    rotated_nodes.rotate()
    tpl = tuple(zip(nodes, list(rotated_nodes)))
    return tpl

def create_tour_algorithm_2(nodes):
    for item in nodes[:-1]:
        lst.append((item, item + 1))
    lst.append((nodes[-1], nodes[0]))
    return tuple(lst)"""


# the professor algorithm
"""def create_tour(nodes):
    tour = []
    l = len(nodes)
    for i in range(l):
        t = (nodes[i], nodes[(i + 1) % l])
        tour.append(t)
    return (tour)"""

""" the following algorithm has two problems:
    1. there is no definitions for some functions
    2. i think there is something missing, when you 
        start to check odd degree nodes and connect 
        them to turn to even degree nodes, the tour 
        list should be updated thereof"""
def create_tour_random(nodes):
    connected = []
    degree = {}
    unconnected = [n for n in nodes]
    tour = []
    x = poprandom(unconnected)
    y = poprandom(unconnected)
    connected.append(x)
    connected.append(y)
    tour.append((x, y))
    degree[x] = 1
    degree[y] = 1
    while len(unconnected) > 0:
        x = pickrandom(connected)
        y = poprandom(unconnected)
        connected.append(y)
        tour.append((x, y))
        degree[x] += 1
        degree[y] = 1
    odd_nodes = [k for k, v in degree.items() if v % 2 == 1]
    even_nodes = [k for k, v in degree.items() if v % 2 == 0]
    while len(odd_nodes) > 0:
        x = poprandom(odd_nodes)
        cn =check_nodes(x, odd_nodes, tour)
        if cn is not None:
            even_nodes.append(x)
            even_nodes.append(cn)
        else:
            cn = check_nodes(x, even_nodes, tour)
            odd_nodes.append(cn)
            even_nodes.append(x)
    return tour




nodes = ['20', '21', '22', '23', '24', '25']
print(create_tour_random(nodes))
