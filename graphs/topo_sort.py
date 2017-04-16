from collections import defaultdict

def topo_sort(graph_input):
    nodes = set()
    graph = defaultdict(list)

    for p, c in graph_input:
        nodes.update([p, c])
        if c not in graph[p]:
            graph[p].append(c)
    color = {n: "white" for n in nodes}
    result = []
    for u in graph.keys():
        if color[u] == "white":
            topo_sort_util(u, graph, color, result)
    result.reverse()
    return result

def topo_sort_util(u, graph, color, result):
    color[u] = "gray"
    for v in graph[u]:
        if color[v] == "white":
            topo_sort_util(v, graph, color, result)
        if color[v] == "gray":
            raise Exception("Cycle")
    color[u] = "black"
    result.append(u)


graph = [(1,3),(1,2),(3,4),(5,6),(6,3),(3,8),(8,11)]

print topo_sort(graph)

#Vertex-5, Vertex-6, Vertex-1, Vertex-2, Vertex-3, Vertex-8, Vertex-11, Vertex-4