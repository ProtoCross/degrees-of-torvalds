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
from ordered_set import OrderedSet
import warnings
warnings.filterwarnings('ignore')

SEED_USER = 'linsheng9731'

fig = plt.figure(figsize=(15, 15))
ax = fig.add_subplot(111)

gitGraph = nx.Graph()

client = Github(ACCESS_TOKEN)
user = client.get_user(SEED_USER)
userSet = OrderedSet()

foundTorvalds = False
#Add first node on graph
gitGraph.add_node(user.login, type='user')
#degrees_modules.addStars(gitGraph, user)

users = degrees_modules.addUserFollowers(gitGraph, user)
userSet |= (users)

while foundTorvalds is False:
    for user in userSet:
        if user.following < 11000:
            userSet |= (degrees_modules.addFollowing(gitGraph, user))
        print('still alive after user ' + str(user))
        if gitGraph.has_node('torvalds') is True:
            foundTorvalds = True
            break
       

nx.write_gpickle(gitGraph, 'graph5.pkl')
print('pickle made!')

labels = {n:n for n in gitGraph.nodes()}
nx.draw(gitGraph, nx.spring_layout(gitGraph), arrows=True, ax=ax,
        node_size=100, edge_color='#aaaaaa', 
        node_color=degrees_modules.colorGraph(gitGraph), alpha=0.8, 
        font_size=12, labels = labels, node_shape='^')