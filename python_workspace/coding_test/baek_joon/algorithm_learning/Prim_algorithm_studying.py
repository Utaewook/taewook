# 힙 구조 활용해 구현
from heapq import *
from collections import defaultdict

def read_graph():
    myedges = []
    f = open('mst_graph.txt','r')
    while True:
        line = f.readline()
        if not line:
            break
        c,u,v = line.split()
        myedges.append((int(c),u,v))
    return myedges

def prim(start_node,edges):
    mst = list()
    adjacent_edges = defaultdict(list)
    for weight, n1, n2 in edges:
        adjacent_edges[n1].append((weight,n1,n2))
        adjacent_edges[n2].append((weight,n2,n1))

    connected_nodes = set(start_node)
    candidate_edge_list = adjacent_edges[start_node]
    heapify(candidate_edge_list)

    while candidate_edge_list:
        weight,n1,n2 = heappop(candidate_edge_list)
        if n2 not in connected_nodes:
            connected_nodes.add(n2)
            mst.append((weight,n1,n2))

            for edge in adjacent_edges[n2]:
                if edge[2] not in connected_nodes:
                    heappush(candidate_edge_list,edge)

    return mst


print(prim("A", read_graph()))