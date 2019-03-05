# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 09:08:05 2019

@author: s525501
"""

from github import Github
from github_token import ACCESS_TOKEN
import degrees_modules
import networkx as nx
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

SEED_USER = 'neloe'

fig = plt.figure(figsize=(15, 15))
ax = fig.add_subplot(111)

gitGraph = nx.DiGraph()

client = Github(ACCESS_TOKEN)
user = client.get_user(SEED_USER)

gitGraph.add_node(user.login, type='user')
repos = degrees_modules.addStars(gitGraph, user)

labels = {n:n for n in gitGraph.nodes()}
nx.draw(gitGraph, nx.spring_layout(gitGraph), arrows=True, ax=ax,
        node_size=100, edge_color='#aaaaaa', 
        node_color=degrees_modules.colorGraph(gitGraph), alpha=0.8, 
        font_size=12, labels = labels, node_shape='^')