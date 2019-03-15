# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:46:29 2019

@author: Josh
"""

import networkx as nx
import matplotlib.pyplot as plt
import degrees_modules
import warnings
warnings.filterwarnings('ignore')

fig = plt.figure(figsize=(15, 15))
ax = fig.add_subplot(111)

graph = nx.read_gpickle('graph3.pkl')

#path = nx.all_shortest_paths(fixedGraph, 'neloe', 'torvalds')
print([p for p in nx.all_shortest_paths(graph,'nypzxy','torvalds')])

tree = nx.bfs_tree(graph, 'nypzxy', 5)

labels = {n:n for n in tree.nodes()}
nx.draw(tree, nx.kamada_kawai_layout(tree), arrows=True, ax=ax,
        node_size=100, edge_color='#aaaaaa', 
        node_color=degrees_modules.colorGraph(graph), alpha=0.8, 
        font_size=12, labels = labels, node_shape='^')