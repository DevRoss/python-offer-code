#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 2019/8/22
from collections import deque

visited = set()
adj = dict()

edges = """1 2
2 3
3 4
3 5
1 6
6 7
7 8
8 4"""


def get_adj():
    _adj = dict()
    for line in edges.splitlines():
        a, b = list(line.split(' '))
        if a in _adj:
            _adj[a].append(b)
        else:
            _adj[a] = [b]

        if b in _adj:
            _adj[b].append(a)
        else:
            _adj[b] = [a]
    return _adj


def dfs(node, visited):
    print(node)
    for i in adj[node]:
        if i not in visited:
            visited.add(i)
            dfs(i, visited)


def bfs(begin_node):
    q = deque()
    q.append(begin_node)
    visited = set()
    while q:
        node = q.popleft()
        if node not in visited:
            visited.add(node)
            print(node)
            for i in adj[node]:
                if i not in visited:
                    q.append(i)


def traverse_dfs():
    visited = {'1'}
    begin_node = '1'
    dfs(begin_node, visited)


def traverse_bfs():
    begin_node = '1'
    bfs(begin_node)


if __name__ == '__main__':
    adj = get_adj()
    print('------------dfs------------')
    traverse_dfs()
    print('------------bfs------------')
    traverse_bfs()
