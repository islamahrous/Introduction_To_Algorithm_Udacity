def find_eulerian_tour(graph):
    # this algorithm is not efficient at all, simply you have to
    # input the nodes with the same order as the tour would be
    graph_list = list(graph)
    graph_status = [1] * len(graph_list)
    tour = [graph_list[0][0], graph_list[0][1]]
    graph_list.remove(graph_list[0])
    graph_status[0] = 0
    i = 1
    while graph_status.count(1) != 0 and i != len(graph):
        if (tour[i] == graph[i][0]) and (graph_status[i] == 1):
            tour.append(graph[i][1])
            graph_status[i] = 0
            i += 1
    return tour


graph = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)]
print(find_eulerian_tour(graph))
