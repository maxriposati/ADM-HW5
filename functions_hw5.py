import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import heapq
from collections import defaultdict


def Dijkstra(G, start, end):
    '''
    This function evaluates the distance of the shortest path using Dijkstra algorithm.
    The function does not works if the author ids given in input are not in the graph or if they are not connected.
    Moreover, it uses the *heap* data structure to keep track of the visited nodes and of their distances.

    Input: the graph and two author ids (the starting node and the final node).
    
    Output: a tuple in which the first element is the distance of the shortest path
    and the second element is a list of all nodes involved to go from the starting node to the final node.
    '''
    # Check whether the two nodes are in the graph
    # Keep the checks separated so that we know which one we have to modify
    if start not in G.nodes():
        return("The start node is not in the graph.")
    if end not in G.nodes():
        return("The end node is not in the graph.")
    
    # Check whether there is no path between the start and end nodes:
    if  not nx.has_path(G,start,end): 
        return("There is no path between the start and end nodes.")
    
    # heapq object, list of tuples with (dist/cost, node)
    q = [(0, start, [])]
    # set of unseen nodes
    seen = set()
    
    while q:
        # dist and node of the closest node (closest to the previously seen node)
        dist, current, path = heapq.heappop(q)
        
        if current not in seen:
            # update the seen set
            seen.add(current)
            # update the path
            path = path + [current]
            # return if I found it
            if current == end:
                return (dist, path)
            # all current neighbors
            temp = G[current]
            # all unseen (not-visited) neighbors of current
            to_see = list(set(temp).difference(seen))
            
            # list of tuples with (updated-dist, node)
            # where node is one of the unseen neighbors and updated-dist is the distance from start to the node
            neigh = [(dist+temp[n]["weight"], n) for n in to_see]
            
            # add the new info ()
            for d, n in neigh:
                heapq.heappush(q, (d, n, path))
                
                
                
def BFS(start,graph):
    
    '''
    This function evaluates the distance of the shortest path using Breadth First Search algorithm.
    The function does not works if the author id given in input are not in the graph and returns an error string.
    Also if two nodes are not connected it returns a value equal -1. Moreover, it uses the defaultdict data 
    structure to keep track of the visited nodes and of their distances.

    Input: the graph and the author id (the starting node).
    
    Output: a dictionary in which the keys correspond to the node IDs and 
    the values corresponding to the distances of each node of the graph from the starting one.
    '''
    
    
    # Check if the start node is in the graph
    if start not in graph.nodes():
        return("The start node is not in the graph.")
    #defining an empty count dictionary of seen dictionaty with default tuple values (False,-1)
    #of vertices we have computed the shortest_path
    seen = defaultdict(lambda:(False,-1))
    #defining of the first initial start vertex with values (True,0)
    seen[start] = (True,0)
    #new queue abstract data structure with initial value of the starting vertex we want all the distances from
    queue = [start]
    #while queue is not empty
    while len(queue) != 0:
        #set as current vertex the first element inserted into the queue from that inside
        current = queue.pop(0)
        #define as d the the distance from the current vertex to the starting one
        d = seen[current][1] 
        #running a loop for all the neighbors/successors of the current node
        for neighbor in graph[current]:
            #condition: if we haven't seen this vertex until now --> TRUE
            if not seen[neighbor][0]:
                #we increase the distance of the current vertex by 1 and we assing TRUE value
                # in order to know that we have already visited it
                seen[neighbor] = (True,d+1)
                #we are appending into the queue the seen neighbor vertex
                queue.append(neighbor)
    # we create a results dictionary with default distances equal to -1
    sh_paths = defaultdict(lambda:-1)
    # we assing at every vertex the computed distance
    for vertex in seen.keys():
        sh_paths[vertex] = seen[vertex][1]
    return sh_paths





def blockRanking(inp_cat,categories,G):
    
    
    '''
    This function evaluates the ranking of every category from an input category using block ranking technique.
    The function returns a ranked dictionary of the distances of all the other categories of the graph.
    For the input category the distance is one and if a category has nodes with no path connecting the two categories,
    returns a nan values.

    Input: the input category, the categories dictionary and the graph.
    
    Output: a list of tuples with the values corresponding to the distance of each category of the graph from the input one
    and the name of each category. The first result corresponds to the input category and it has distance 0.
    '''

    #initialiazation of the block ranking vector with the iput category
    results = [(0,inp_cat)]
    #computing of shortest_path distance dictionary from a node to evey other node of the graph
    q = {cat:[] for cat in categories.keys()}


    #loop for every node of the input category
    for node in categories[inp_cat]:
    #computing of shortest_path distance dictionary from a node to evey other node of the graph
    #using BFS algorithmn
        distances = BFS(node,G)
        #nested loop for every category
        for categ in categories.keys():
            if categ != inp_cat:
                #empty list of the distances of every node of the targets category to the node of the starting one
                qq = []
                #nested loop for every node in the current category we have computed the shortest_path
                for j in categories[categ]:
                #if there is NOT a path between the 2 nodes the BFS function returns -1, else the distance          
                    if distances[j] != -1:
                       #append the node distance from the input one in the distance list.
                        qq.append(distances[j])
  #finally we compute the median for every key-category sublist of the vector and a weight equal to the length of the sublist
  #we do that in order to avoid extremely huge lists (memory error). At the end we compute the weighted average of the medians of the sublists
  #we assume that this weighted average converges to the real median.
                q[categ].append((len(qq),np.median(sorted(qq)))) #appending of the corresponding tuple with the weight and the median of the sublist
    
   
    #now for every category we have a list of tuples (w,median) with w:weight and the median of every sublist
    #instead of computing the median of a huge list we will calculate the weighted average of the median of smaller sublists
    #with weights equal to the lenght of the sublists for every category
    for categ in q.keys():
        if categ != inp_cat:
            w = [x[0] for x in q[categ]] #weight of sublist equal to the respective length
            d = [x[1] for x in q[categ]] #median of sublist
            results.append((np.round(np.dot(w,d)/np.sum(w)),categ))  #weighted average       
    return sorted(results)  #final format of the blockRanking vector sorted according to the categories distance


def scoring(categories,G):
    
    '''
    This function evaluates the score of every node. The function returns a dictionary with the score
    of all the nodes of the graph, using a ranked categories dictionart from an input categories to all
    the othe categories of the graph.

    Input: the new updated ranked categories dictionary and the graph.
    
    Output: a dictionary in which the keys correspond to the nodes od the graph and 
    the values to the final score of each node.
    '''
    
    #new empty dictionary with each article score with initial values equal to zero.
    score = {node:0 for node in G.nodes()} 
    #empty set for the nodes we have seen after every rep.
    seen = set()
    #empty list of the nodes of the subgraph H after every rep
    nodes = []
    for cat in categories.keys():
        #extending the nodes list with the articles of the current category
        nodes.extend(categories[cat])
        #subgraph creation
        H = G.subgraph(nodes)
        #nested loop for every node of the current category
        for node in categories[cat]:
            #nested loop for every predecessor of the current node 
            for pred in list(H.predecessors(node)):
                #if predecessor is in seen dictionary, so in other category than the current
                #we add the value-score that we have computed in previous steps
                if pred in seen:
                    score[node] += score[pred]
                #if the predecessor is not the seen dictionary, so it is in the same category of the
                #current node, we give the node score of 1
                else:
                    score[node] += 1
        #update seen dictionary
        for n in categories[cat]:         
            seen.add(n)
            
    return score