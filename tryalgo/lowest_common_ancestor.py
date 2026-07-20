#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tryalgo.range_minimum_query import RangeMinQuery


def log2floor(n):
    pass


def log2ceil(n):
    pass


class LowestCommonAncestorShortcuts:
    def __init__(self, prec):
        """builds the structure from a given tree

        :param prec: father for every node, with prec[0] = 0
        :assumes: prec[node] < node
        :complexity: O(n log n), with n = len(nodes)
        """
        n = len(prec)
        self.level = [None] * n        # build levels
        self.level[0] = 0
        for u in range(1, n):
            self.level[u] = 1 + self.level[prec[u]]
        depth = log2ceil(max(self.level[u] for u in range(n))) + 1
        self.anc = [[0] * n for _ in range(depth)]
        for u in range(n):
            self.anc[0][u] = prec[u]
        for k in range(1, depth):
            for u in range(n):
                self.anc[k][u] = self.anc[k - 1][self.anc[k - 1][u]]

    def query(self, u, v):
        pass


class LowestCommonAncestorRMQ:
    def __init__(self, graph):
        """builds the structure from a given tree

        :param graph: adjacency matrix of a tree
        :complexity: O(n log n), with n = len(graph)
        """
        n = len(graph)
        dfs_trace = []
        self.last = [None] * n
        to_visit = [(0, 0, None)]            # node 0 is root
        succ = [0] * n
        while to_visit:
            level, node, father = to_visit[-1]
            self.last[node] = len(dfs_trace)
            dfs_trace.append((level, node))
            if succ[node] < len(graph[node]) and \
               graph[node][succ[node]] == father:
                succ[node] += 1
            if succ[node] == len(graph[node]):
                to_visit.pop()
            else:
                neighbor = graph[node][succ[node]]
                succ[node] += 1
                to_visit.append((level + 1, neighbor, node))
        self.rmq = RangeMinQuery(dfs_trace, (float('inf'), None))

    def query(self, u, v):
        pass
