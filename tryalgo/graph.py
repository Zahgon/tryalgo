#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List, Dict, Union, Any

def readval(file, ty):
    pass


def readtab(fi, ty):
    pass


def read_graph(filename, directed=False, weighted=False, default_weight=None):
    pass


def write_graph(dotfile, graph, directed=False,
                node_label=None, arc_label=None, comment="",
                node_mark=set(), arc_mark=set()):
    """Writes a graph to a file in the DOT format

    :param dotfile: the filename.
    :param graph: directed graph in listlist or listdict format
    :param directed: true if graph is directed, false if undirected
    :param weight: in matrix format or same listdict graph or None
    :param node_label: vertex label table or None
    :param arc_label: arc label matrix or None
    :param comment: comment string for the dot file or None
    :param node_mark: set of nodes to be shown in gray
    :param arc_marc: set of arcs to be shown in red
    :complexity: `O(|V| + |E|)`
    """
    with open(dotfile, 'w') as f:
        if directed:
            f.write("digraph G{\n")
        else:
            f.write("graph G{\n")
        if comment:
            f.write('label="%s";\n' % comment)
        V = range(len(graph))
        for u in V:
            if node_mark and u in node_mark:
                f.write('%d [style=filled, color="lightgrey", ' % u)
            else:
                f.write('%d [' % u)
            if node_label:
                f.write('label="%u [%s]"];\n' % (u, node_label[u]))
            else:
                f.write('shape=circle, label="%u"];\n' % u)
        if isinstance(arc_mark, list):
            arc_mark = set((u, arc_mark[u]) for u in V)
        for u in V:
            for v in graph[u]:
                if not directed and u > v:
                    continue   # don't show twice the edge
                if arc_label and arc_label[u][v] is None:
                    continue   # suppress arcs with no label
                if directed:
                    arc = "%d -> %d " % (u, v)
                else:
                    arc = "%d -- %d " % (u, v)
                if arc_mark and ((v, u) in arc_mark or
                                 (not directed and (u, v) in arc_mark)):
                    pen = 'color="red"'
                else:
                    pen = ""
                if arc_label:
                    tag = 'label="%s"' % arc_label[u][v]
                else:
                    tag = ""
                if tag and pen:
                    sep = ", "
                else:
                    sep = ""
                f.write(arc + "[" + tag + sep + pen + "];\n")
        f.write("}")


def tree_prec_to_adj(prec, root=0):
    """Transforms a tree given as predecessor table into adjacency list form

    :param prec: predecessor table representing a tree, prec[u] == v iff u is
        successor of v, except for the root where prec[root] == root
    :param root: root vertex of the tree
    :returns: undirected graph in listlist representation
    :complexity: linear
    """
    n = len(prec)
    graph = [[prec[u]] for u in range(n)]   # add predecessors
    graph[root] = []
    for u in range(n):                      # add successors
        if u != root:
            graph[prec[u]].append(u)
    return graph


def tree_adj_to_prec(graph, root=0):
    """Transforms a tree given as adjacency list into predecessor table form.
    if graph is not a tree: will return a DFS spanning tree

    :param graph: directed graph in listlist or listdict format
    :returns: tree in predecessor table representation
    :complexity: linear
    """
    prec = [None] * len(graph)
    prec[root] = root            # mark to visit root only once
    to_visit = [root]
    while to_visit:              # DFS
        node = to_visit.pop()
        for neighbor in graph[node]:
            if prec[neighbor] is None:
                prec[neighbor] = node
                to_visit.append(neighbor)
    prec[root] = None            # put the standard mark for root
    return prec


def add_reverse_arcs(graph, capac=None):
    """Utility function for flow algorithms that need for every arc (u,v),
    the existence of an (v,u) arc, by default with zero capacity.
    graph can be in adjacency list, possibly with capacity matrix capac.
    or graph can be in adjacency dictionary, then capac parameter is ignored.

    :param capac: arc capacity matrix
    :param graph: in listlist representation, or in listdict representation,
        in this case capac is ignored
    :complexity: linear
    :returns: nothing, but graph is modified
    """
    for u, _ in enumerate(graph):
        for v in graph[u]:
            if u not in graph[v]:
                if type(graph[v]) is list:
                    graph[v].append(u)
                    if capac:
                        capac[v][u] = 0
                else:
                    assert type(graph[v]) is dict
                    graph[v][u] = 0







def matrix_to_listlist(weight):
    """transforms a squared weight matrix in a adjacency table of type listlist
    encoding the directed graph corresponding to the entries of the matrix
    different from None

    :param weight: squared weight matrix, weight[u][v] != None iff arc (u, v)
        exists
    :complexity: linear
    :returns: the unweighted directed graph in the listlist representation,
        listlist[u] contains all v for which arc (u,v) exists.
    """
    graph = [[] for _ in range(len(weight))]
    for u, _ in enumerate(graph):
        for v in range(len(graph)):
            if weight[u][v] is not None:
                graph[u].append(v)
    return graph


def listlist_and_matrix_to_listdict(graph, weight=None):
    """Transforms the weighted adjacency list representation of a graph
    of type listlist + optional weight matrix
    into the listdict representation

    :param graph: in listlist representation
    :param weight: optional weight matrix
    :returns: graph in listdict representation
    :complexity: linear
    """
    if weight:
        return [{v: weight[u][v] for v in graph[u]} for u in range(len(graph))]
    else:
        return [{v: None for v in graph[u]} for u in range(len(graph))]


def listdict_to_listlist_and_matrix(sparse):
    """Transforms the adjacency list representation of a graph
    of type listdict into the listlist + weight matrix representation

    :param sparse: graph in listdict representation
    :returns: couple with listlist representation, and weight matrix
    :complexity: linear
    """
    V = range(len(sparse))
    graph = [[] for _ in V]
    weight = [[None for v in V] for u in V]
    for u in V:
        for v in sparse[u]:
            graph[u].append(v)
            weight[u][v] = sparse[u][v]
    return graph, weight


def dictdict_to_listdict(dictgraph):
    """Transforms a dict-dict graph representation into a
    adjacency dictionary representation (list-dict)

    :param dictgraph: dictionary mapping vertices to dictionary
        such that dictgraph[u][v] is weight of arc (u,v)
    :complexity: linear
    :returns: tuple with graph (listdict), name_to_node (dict),
        node_to_name (list)
    """
    n = len(dictgraph)                            # vertices
    node_to_name = list(dictgraph.keys())         # bijection indices <-> names
    node_to_name.sort()                           # to make it more readable
    name_to_node = {}
    for i in range(n):
        name_to_node[node_to_name[i]] = i
    sparse = [{} for _ in range(n)]               # build sparse graph
    for u in dictgraph:
        for v in dictgraph[u]:
            sparse[name_to_node[u]][name_to_node[v]] = dictgraph[u][v]
    return sparse, name_to_node, node_to_name



def extract_path(prec, v):
    """extracts a path in form of vertex list from source to vertex v
       given a precedence table prec leading to the source

    :param prec: precedence table of a tree
    :param v: vertex on the tree
    :returns: path from root to v, in form of a list
    :complexity: linear
    """
    L = []
    while v is not None:
        L.append(v)
        v = prec[v]
        assert v not in L  # prevent infinite loops for a bad formed table prec
    return L[::-1]



def make_flow_labels(graph, flow, capac):
    """Generate arc labels for a flow in a graph with capacities.

    :param graph: adjacency list or adjacency dictionary
    :param flow:  flow matrix or adjacency dictionary
    :param capac: capacity matrix or adjacency dictionary
    :returns: listdic graph representation, with the arc label strings
    """
    V = range(len(graph))
    arc_label = [{v: "" for v in graph[u]} for u in V]
    for u in V:
        for v in graph[u]:
            if flow[u][v] >= 0:
                arc_label[u][v] = "%s/%s" % (flow[u][v], capac[u][v])
            else:
                arc_label[u][v] = None   # do not show negative flow arcs
    return arc_label



class GraphNamedVertices:
    def __init__(self):
        self.neighbors = []
        self.name2node = {}
        self.node2name = []
        self.weight = []

    def __len__(self):
        return len(self.node2name)

    def __getitem__(self, v):
        return self.neighbors[v]

    def add_node(self, name):
        pass

    def add_edge(self, name_u, name_v, weight_uv=None):
        pass

    def add_arc(self, name_u, name_v, weight_uv=None):
        pass

Graph = Union[List[List[int]], List[Dict[int, Any]], GraphNamedVertices]
