# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 09:08:05 2019

@author: s525501
"""
#Import needed packages
from github import Github
from github_token import ACCESS_TOKEN
import degrees_modules
import networkx as nx
import matplotlib.pyplot as plt
from ordered_set import OrderedSet
import warnings
warnings.filterwarnings('ignore')

#Seed the user for the first node
SEED_USER = 'wilsjame'

fig = plt.figure(figsize=(15, 15))
ax = fig.add_subplot(111)

gitGraph = nx.Graph()

#Set up github api requirements
client = Github(ACCESS_TOKEN)
user = client.get_user(SEED_USER)

userSet = OrderedSet()

#Add first node on graph
gitGraph.add_node(user.login, type='user')

#Update user set for seed's followers
users = degrees_modules.addUserFollowers(gitGraph, user)
userSet |= (users)

#Continuously branch out using followers until torvalds is found
def useFollowers(userSet):
    foundTorvalds = False
    while foundTorvalds is False:
        for user in userSet:
            if user.following < 11000:
                userSet |= (degrees_modules.addFollowing(gitGraph, user))
            print('still alive after user ' + str(user))
            if gitGraph.has_node('torvalds') is True:
                foundTorvalds = True
                break

#Branch out using repositories and stargazers  
def useGazers(userSet):
    foundTorvalds = False
    while foundTorvalds is False:
        for user in userSet:
            repos = degrees_modules.addStars(gitGraph, user)
            for repo in repos:
                userSet |= degrees_modules.addStargazers(gitGraph, repo)
            if gitGraph.has_node('torvalds') is True:
                foundTorvalds = True
                break


#useFollowers(userSet)
useGazers(userSet)

#Store the generated graph for manipulation
nx.write_gpickle(gitGraph, 'graphStars.pkl')
print('pickle made!')