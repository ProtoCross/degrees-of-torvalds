# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:46:29 2019

@author: Josh
"""

from github import Github
from github_token import ACCESS_TOKEN
import networkx as nx
import matplotlib.pyplot as plt
import degrees_modules
import warnings
warnings.filterwarnings('ignore')

client = Github(ACCESS_TOKEN)

fig = plt.figure(figsize=(15, 15))
ax = fig.add_subplot(111)

graph = nx.read_gpickle('graph4.pkl')
y = list()
path = list([p for p in nx.all_shortest_paths(graph,'audie2982','torvalds')])
for user in path:
    for x in user:
        y.append(client.get_user(x).get_repos().totalCount)

y.reverse()
print(y)
tree = nx.bfs_tree(graph, 'audie2982', 5)


'''
labels = {n:n for n in tree.nodes()}
nx.draw(tree, nx.kamada_kawai_layout(tree), arrows=True, ax=ax,
        node_size=100, edge_color='#aaaaaa', 
        node_color=degrees_modules.colorGraph(graph), alpha=0.8, 
        font_size=12, labels = labels, node_shape='^')
'''