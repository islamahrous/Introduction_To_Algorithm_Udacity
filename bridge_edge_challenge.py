# Bridge Edges v4
#
# Find the bridge edges in a graph given the
# algorithm in lecture.
# Complete the intermediate steps
#  - create_rooted_spanning_tree
#  - post_order
#  - number_of_descendants
#  - lowest_post_order
#  - highest_post_order
#
# And then combine them together in
# `bridge_edges`

# So far, we've represented graphs
# as a dictionary where G[n1][n2] == 1
# meant there was an edge between n1 and n2
#
# In order to represent a spanning tree
# we need to create two classes of edges
# we'll refer to them as "green" and "red"
# for the green and red edges as specified in lecture
#
# So, for example, the graph given in lecture
# G = {'a': {'c': 1, 'b': 1},
#      'b': {'a': 1, 'd': 1},
#      'c': {'a': 1, 'd': 1},
#      'd': {'c': 1, 'b': 1, 'e': 1},
#      'e': {'d': 1, 'g': 1, 'f': 1},
#      'f': {'e': 1, 'g': 1},
#      'g': {'e': 1, 'f': 1}
#      }
# would be written as a spanning tree
# S = {'a': {'c': 'green', 'b': 'green'},
#      'b': {'a': 'green', 'd': 'red'},
#      'c': {'a': 'green', 'd': 'green'},
#      'd': {'c': 'green', 'b': 'red', 'e': 'green'},
#      'e': {'d': 'green', 'g': 'green', 'f': 'green'},
#      'f': {'e': 'green', 'g': 'red'},
#      'g': {'e': 'green', 'f': 'red'}
#      }
#


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
    # your code here
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


# This is just one possible solution
# There are other ways to create a
# spanning tree, and the grader will
# accept any valid result
# feel free to edit the test to
# match the solution your program produces
def test_create_rooted_spanning_tree():
    G = {'a': {'b': 1, 'c': 1},
         'b': {'a': 1, 'd': 1},
         'c': {'a': 1, 'd': 1},
         'd': {'c': 1, 'b': 1, 'e': 1},
         'e': {'d': 1, 'g': 1, 'f': 1},
         'f': {'e': 1, 'g': 1},
         'g': {'e': 1, 'f': 1}
         }
    S = create_rooted_spanning_tree(G, "a")
    assert S == {'a': {'c': 'green', 'b': 'green'},
                 'b': {'a': 'green', 'd': 'red'},
                 'c': {'a': 'green', 'd': 'green'},
                 'd': {'c': 'green', 'b': 'red', 'e': 'green'},
                 'e': {'d': 'green', 'g': 'green', 'f': 'green'},
                 'f': {'e': 'green', 'g': 'red'},
                 'g': {'e': 'green', 'f': 'red'}
                 }


###########
def get_children(S, root, parent):
    return [n for n, e in S[root].items() if ((n != parent) and (e == 'green'))]


def _post_order(S, root, parent, val, po):
    children = get_children(S, root, parent)
    for c in children:
        val = _post_order(S, c, root, val, po)
    po[root] = val
    return val + 1


def post_order(S, root):
    # return mapping between nodes of S and the post-order value
    # of that node
    po = {}
    _post_order(S, root, None, 1, po)
    return po


# This is just one possible solution
# There are other ways to create a
# spanning tree, and the grader will
# accept any valid result.
# feel free to edit the test to
# match the solution your program produces
def test_post_order():
    S = {'a': {'b': 'green', 'c': 'green'},
         'b': {'a': 'green', 'd': 'red'},
         'c': {'a': 'green', 'd': 'green'},
         'd': {'c': 'green', 'b': 'red', 'e': 'green'},
         'e': {'d': 'green', 'g': 'green', 'f': 'green'},
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'}
         }
    po = post_order(S, 'a')
    assert po == {'a': 7, 'b': 1, 'c': 6, 'd': 5, 'e': 4, 'f': 3, 'g': 2}


##############
def _number_descendants(S, root, parent, nd):
    children = get_children(S, root, parent)
    nd_val = 1
    for c in children:
        nd_val += _number_descendants(S, c, root, nd)
    nd[root] = nd_val
    return nd_val


def number_of_descendants(S, root):
    # return mapping between nodes of S and the number of descendants
    # of that node
    nd = {}
    _number_descendants(S, root, None, nd)
    return nd


def test_number_of_descendants():
    S = {'a': {'b': 'green', 'c': 'green'},
         'b': {'a': 'green', 'd': 'red'},
         'c': {'a': 'green', 'd': 'green'},
         'd': {'c': 'green', 'b': 'red', 'e': 'green'},
         'e': {'d': 'green', 'g': 'green', 'f': 'green'},
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'}
         }
    nd = number_of_descendants(S, 'a')
    assert nd == {'a': 7, 'b': 1, 'c': 5, 'd': 4, 'e': 3, 'f': 1, 'g': 1}


###############
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
    # return a mapping of the nodes in S
    # to the lowest post order value
    # below that node
    # (and you're allowed to follow 1 red edge)
    lpo = {}
    _general_post_order(S, root, None, po, lpo, lambda x, y: x > y)
    return lpo


def test_lowest_post_order():
    S = {'a': {'b': 'green', 'c': 'green'},
         'b': {'a': 'green', 'd': 'red'},
         'c': {'a': 'green', 'd': 'green'},
         'd': {'c': 'green', 'b': 'red', 'e': 'green'},
         'e': {'d': 'green', 'g': 'green', 'f': 'green'},
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'}
         }
    po = post_order(S, 'a')
    l = lowest_post_order(S, 'a', po)
    assert l == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 2, 'f': 2, 'g': 2}


################

def highest_post_order(S, root, po):
    # return a mapping of the nodes in S
    # to the highest post order value
    # below that node
    # (and you're allowed to follow 1 red edge)
    hpo = {}
    _general_post_order(S, root, None, po, hpo, lambda x, y: x < y)
    return hpo


def test_highest_post_order():
    S = {'a': {'b': 'green', 'c': 'green'},
         'b': {'a': 'green', 'd': 'red'},
         'c': {'a': 'green', 'd': 'green'},
         'd': {'c': 'green', 'b': 'red', 'e': 'green'},
         'e': {'d': 'green', 'g': 'green', 'f': 'green'},
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'}
         }
    po = post_order(S, 'a')
    h = highest_post_order(S, 'a', po)
    assert h == {'a': 7, 'b': 5, 'c': 6, 'd': 5, 'e': 4, 'f': 3, 'g': 3}


#################

def bridge_edges(G, root):
    # use the four functions above
    # and then determine which edges in G are bridge edges
    # return them as a list of tuples ie: [(n1, n2), (n4, n5)]
    S = create_rooted_spanning_tree(G, root)
    po = post_order(S, root)
    nd = number_of_descendants(S, root)
    lpo = lowest_post_order(S, root, po)
    hpo = highest_post_order(S, root, po)
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
    return bridges


def test_bridge_edges():
    G = {'a': {'b': 1, 'c': 1},
         'b': {'a': 1, 'd': 1},
         'c': {'a': 1, 'd': 1},
         'd': {'c': 1, 'b': 1, 'e': 1},
         'e': {'d': 1, 'g': 1, 'f': 1},
         'f': {'e': 1, 'g': 1},
         'g': {'e': 1, 'f': 1}
         }
    bridges = bridge_edges(G, 'a')
    assert bridges == [('d', 'e')]
