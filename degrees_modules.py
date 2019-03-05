# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 09:10:09 2019

@author: s525501
"""

from github_token import ACCESS_TOKEN

# Get user repos and add to graph
def addUserRepos(graph, user):
    repos = user.get_repos()
    for repo in repos:
        graph.add_node(repo.name, type='repo')
        graph.add_edge(user.login, repo.name, type='owns')
    return repos

# Get repo stargazers and add to graph
def addStargazers(graph, repo):
    gazers = repo.get_stargazers()
    for gaze in gazers:
        graph.add_node(gaze.login, type='user')
        graph.add_edge(gaze.login, repo.name, type='gazes')
    return gazers

# Get a user's followers and add to graph
def addUserFollowers(graph, user):
    followers = user.get_followers()
    for follow in followers:
        graph.add_node(follow.login, type='user')
        graph.add_edge(follow.login, user.login, type='follows')
    return followers
    
# Get a user's starred repositories and add to graph
def addStars(graph, user):
    stars = user.get_starred()
    for star in stars:
        graph.add_node(star.name, type='repo')
        graph.add_edge(user.login, star.name, type='starred')

# Get users that someone follows and add to graph
def addFollowing(graph, user):
    following = user.get_following()
    for person in following:
        graph.add_node(person.login, type='user')
        graph.add_edge(user.login, person.login, type='is following')
    
# Color graph nodes to destinguish between repos and users
def colorGraph(graph):
    colorMap = {'user': 'red', 'repo': 'blue'}
    colorList = []
    for node in graph.nodes():
        nodeType = graph.nodes.data()[node]['type']
        colorList.append(colorMap.get(nodeType, 'black'))
    return colorList