import collections


def make_link_g_or_r(S, node1, node2, g_or_r):
    if node1 not in S:
        S[node1] = {}
    S[node1][node2] = g_or_r
    if node2 not in S:
        S[node2] = {}
    S[node2][node1] = g_or_r
    return S


def create_rooted_spanning_tree(G, root):
    S = {}
    open_list = [root]
    while len(open_list) > 0:
        node = open_list.pop()
        neighbors = G[node]
        for n in neighbors:
            if n not in S:
                make_link_g_or_r(S, node, n, 'green')
                open_list.append(n)
            elif node not in S[n]:
                make_link_g_or_r(S, node, n, 'red')
    return S


def get_children(S, root, parent):
    return [n for n, e in S[root].items() if ((n != parent) and (e == 'green'))]


def get_children_all(S, root, parent):
    """returns the children from following
    green edges and the children from following
    red edges"""
    green = []
    red = []
    for n, e in S[root].items():
        if n == parent:
            continue
        if e == 'green':
            green.append(n)
        if e == 'red':
            red.append(n)
    return green, red


def _post_order(S, root, parent, val, po):
    children = get_children(S, root, parent)
    for c in children:
        val = _post_order(S, c, root, val, po)
    po[root] = val
    return val + 1


def post_order(S, root):
    po = {}
    _post_order(S, root, None, 1, po)
    return po


def _number_descendants(S, root, parent, nd):
    children = get_children(S, root, parent)
    nd_val = 1
    for c in children:
        nd_val += _number_descendants(S, c, root, nd)
    nd[root] = nd_val
    return nd_val


def number_of_descendants(S, root):
    nd = {}
    _number_descendants(S, root, None, nd)
    return nd


def _general_post_order(S, root, parent, po, gpo, comp):
    green, red = get_children_all(S, root, parent)
    val = po[root]
    for c in green:
        # recursively find the low/high post order value of the children
        test = _general_post_order(S, c, root, po, gpo, comp)
        # and save the low/highest one
        if comp(val, test):
            val = test
    for c in red:
        test = po[c]
        # and also look at the direct children
        # from following red edges
        # and save the low/highest one if needed
        if comp(val, test):
            val = test
    gpo[root] = val
    return val


def lowest_post_order(S, root, po):
    lpo = {}
    _general_post_order(S, root, None, po, lpo, lambda x, y: x > y)
    return lpo


def highest_post_order(S, root, po):
    hpo = {}
    _general_post_order(S, root, None, po, hpo, lambda x, y: x < y)
    return hpo


G = {'a': {'b': 1, 'c': 1},
     'b': {'a': 1, 'd': 1},
     'c': {'a': 1, 'd': 1},
     'd': {'c': 1, 'b': 1, 'e': 1},
     'e': {'d': 1, 'g': 1, 'f': 1},
     'f': {'e': 1, 'g': 1},
     'g': {'e': 1, 'f': 1}
     }
root = 'a'
S = create_rooted_spanning_tree(G, root)
# print(S)
po = {}
po = post_order(S, root)
print(po)
nd = {}
nd = number_of_descendants(S, root)
# print(nd)
lpo = lowest_post_order(S, root, po)
# print(lpo)
hpo = highest_post_order(S, root, po)
# print(hpo)
bridges = []
open_list = [(root, None)]
# walk down the tree and see which edges are
# tree edges
while len(open_list) > 0:
    node, parent = open_list.pop()
    for child in get_children(S, node, parent):
        # all of these edges are automatically green (get_children only
        # follows green edges)
        # so only need to check the other two conditions
        if hpo[child] <= po[child] and lpo[child] > (po[child] - nd[child]):
            bridges.append((node, child))
        open_list.append((child, node))
print(bridges)





