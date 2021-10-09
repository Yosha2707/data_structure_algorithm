# Code : BFS Traversal
# Send Feedback
# Given an undirected and disconnected graph G(V, E), print its BFS traversal.
# Note:
# 1. Here you need to consider that you need to print BFS path starting from vertex 0 only. 
# 2. V is the number of vertices present in graph G and vertices are numbered from 0 to V-1. 
# 3. E is the number of edges present in graph G.
# 4. Take graph input in the adjacency matrix.
# 5. Handle for Disconnected Graphs as well
# Input Format :
# The first line of input contains two integers, that denote the value of V and E.
# Each of the following E lines contains space separated two integers, that denote that there exists an edge between vertex a and b.
# Output Format :
# Print the BFS Traversal, as described in the task.
# Constraints :
# 0 <= V <= 1000
# 0 <= E <= (V * (V - 1)) / 2
# 0 <= a <= V - 1
# 0 <= b <= V - 1
# Time Limit: 1 second
# Sample Input 1:
# 4 4
# 0 1
# 0 3
# 1 2
# 2 3
# Sample Output 1:
# 0 1 3 2

___________________________________________________________________________
# Code : Has Path
# Send Feedback
# Given an undirected graph G(V, E) and two vertices v1 and v2 (as integers), check if there exists any path between them or not. Print true if the path exists and false otherwise.
# Note:
# 1. V is the number of vertices present in graph G and vertices are numbered from 0 to V-1. 
# 2. E is the number of edges present in graph G.
# Input Format :
# The first line of input contains two integers, that denote the value of V and E.
# Each of the following E lines contains two integers, that denote that there exists an edge between vertex 'a' and 'b'.
# The following line contain two integers, that denote the value of v1 and v2.
# Output Format :
# The first and only line of output contains true, if there is a path between v1 and v2 and false otherwise.
# Constraints :
# 0 <= V <= 1000
# 0 <= E <= 1000
# 0 <= a <= V - 1
# 0 <= b <= V - 1
# 0 <= v1 <= V - 1
# 0 <= v2 <= V - 1
# Time Limit: 1 second
# Sample Input 1 :
# 4 4
# 0 1
# 0 3
# 1 2
# 2 3
# 1 3
# Sample Output 1 :
# true
# Sample Input 2 :
# 6 3
# 5 3
# 0 1
# 3 4
# 0 3
# Sample Output 2 :
# false


___________________________________________________________________________

# Code : Get Path - DFS
# Send Feedback
# Given an undirected graph G(V, E) and two vertices v1 and v2(as integers), find and print the path from v1 to v2 (if exists). Print nothing if there is no path between v1 and v2.
# Find the path using DFS and print the first path that you encountered.
# Note:
# 1. V is the number of vertices present in graph G and vertices are numbered from 0 to V-1. 
# 2. E is the number of edges present in graph G.
# 3. Print the path in reverse order. That is, print v2 first, then intermediate vertices and v1 at last.
# 4. Save the input graph in Adjacency Matrix.
# Input Format :
# The first line of input contains two integers, that denote the value of V and E.
# Each of the following E lines contains two integers, that denote that there exists an edge between vertex 'a' and 'b'.
# The following line contain two integers, that denote the value of v1 and v2.
# Output Format :
# Print the path from v1 to v2 in reverse order.
# Constraints :
# 2 <= V <= 1000
# 1 <= E <= (V * (V - 1)) / 2
# 0 <= a <= V - 1
# 0 <= b <= V - 1
# 0 <= v1 <= 2^31 - 1
# 0 <= v2 <= 2^31 - 1
# Time Limit: 1 second
# Sample Input 1 :
# 4 4
# 0 1
# 0 3
# 1 2
# 2 3
# 1 3
# Sample Output 1 :
# 3 0 1
# Sample Input 2 :
# 6 3
# 5 3
# 0 1
# 3 4
# 0 3
# Sample Output 2 :

___________________________________________________________________________

# Code : Get Path - BFS
# Send Feedback
# Given an undirected graph G(V, E) and two vertices v1 and v2 (as integers), find and print the path from v1 to v2 (if exists). Print nothing if there is no path between v1 and v2.
# Find the path using BFS and print the shortest path available.
# Note:
# 1. V is the number of vertices present in graph G and vertices are numbered from 0 to V-1. 
# 2. E is the number of edges present in graph G.
# 3. Print the path in reverse order. That is, print v2 first, then intermediate vertices and v1 at last.
# 4. Save the input graph in Adjacency Matrix.
# Input Format :
# The first line of input contains two integers, that denote the value of V and E.
# Each of the following E lines contains two integers, that denote that there exists an edge between vertex a and b.
# The following line contain two integers, that denote the value of v1 and v2.
# Output Format :
# Print the path from v1 to v2 in reverse order.
# Constraints :
# 2 <= V <= 1000
# 1 <= E <= (V * (V - 1)) / 2
# 0 <= a <= V - 1
# 0 <= b <= V - 1
# 0 <= v1 <= 2^31 - 1
# 0 <= v2 <= 2^31 - 1
# Time Limit: 1 second
# Sample Input 1 :
# 4 4
# 0 1
# 0 3
# 1 2
# 2 3
# 1 3
# Sample Output 1 :
# 3 0 1
# Sample Input 2 :
# 6 3
# 5 3
# 0 1
# 3 4
# 0 3
# Sample Output 2 :

___________________________________________________________________________

# Code : Is Connected ?
# Send Feedback
# Given an undirected graph G(V,E), check if the graph G is connected graph or not.
# Note:
# 1. V is the number of vertices present in graph G and vertices are numbered from 0 to V-1. 
# 2. E is the number of edges present in graph G.
# Input Format :
# The first line of input contains two integers, that denote the value of V and E.
# Each of the following E lines contains two integers, that denote that there exists an edge between vertex a and b.
# Output Format :
# The first and only line of output contains "true" if the given graph is connected or "false", otherwise.
# Constraints :
# 0 <= V <= 1000
# 0 <= E <= (V * (V - 1)) / 2
# 0 <= a <= V - 1
# 0 <= b <= V - 1
# Time Limit: 1 second
# Sample Input 1:
# 4 4
# 0 1
# 0 3
# 1 2
# 2 3
# Sample Output 1:
# true
# Sample Input 2:
# 4 3
# 0 1
# 1 3 
# 0 3
# Sample Output 2:
# false 
# Sample Output 2 Explanation
# The graph is not connected, even though vertices 0,1 and 3 are connected to each other but there isn’t any path from vertices 0,1,3 to vertex 2. 

___________________________________________________________________________

# Code : All connected components
# Send Feedback
# Given an undirected graph G(V,E), find and print all the connected components of the given graph G.
# Note:
# 1. V is the number of vertices present in graph G and vertices are numbered from 0 to V-1. 
# 2. E is the number of edges present in graph G.
# 3. You need to take input in main and create a function which should return all the connected components. And then print them in the main, not inside function.
# Print different components in new line. And each component should be printed in increasing order (separated by space). Order of different components doesn't matter.
# Input Format :
# The first line of input contains two integers, that denote the value of V and E.
# Each of the following E lines contains two space separated integers, that denote that there exists an edge between vertex a and b.
# Output Format :
# Print different components in new line. And each component should be printed in increasing order of vertices (separated by space). Order of different components doesn't matter.
# Constraints :
# 0 <= V <= 1000
# 0 <= E <= (V * (V - 1)) / 2
# 0 <= a <= V - 1
# 0 <= b <= V - 1
# Sample Input 1:
# 4 2
# 0 1
# 2 3
# Sample Output 1:
# 0 1 
# 2 3 
# Sample Input 2:
# 4 3
# 0 1
# 1 3 
# 0 3
# Sample Output 2:
# 0 1 3 
# 2

___________________________________________________________________________

# Prim's Algorithm Problem
# Send Feedback
# Given an undirected, connected and weighted graph G(V, E) with V number of vertices (which are numbered from 0 to V-1) and E number of edges.
# Find and print the Minimum Spanning Tree (MST) using Prim's algorithm.
# For printing MST follow the steps -
# 1. In one line, print an edge which is part of MST in the format - 
# v1 v2 w
# where, v1 and v2 are the vertices of the edge which is included in MST and whose weight is w. And v1  <= v2 i.e. print the smaller vertex first while printing an edge.
# 2. Print V-1 edges in above format in different lines.
# Note : Order of different edges doesn't matter.
# Input Format :
# Line 1: Two Integers V and E (separated by space)
# Next E lines : Three integers ei, ej and wi, denoting that there exists an edge between vertex ei and vertex ej with weight wi (separated by space)
# Output Format :
# Print the MST, as described in the task.
# Constraints :
# 2 <= V, E <= 10^5
# 1 <= Wi <= 10^5
# Time Limit: 1 sec
# Sample Input 1 :
# 4 4
# 0 1 3
# 0 3 5
# 1 2 1
# 2 3 8
# Sample Output 1 :
# 0 1 3
# 1 2 1
# 0 3 5

___________________________________________________________________________

# Dijkstra's Algorithm
# Send Feedback
# Given an undirected, connected and weighted graph G(V, E) with V number of vertices (which are numbered from 0 to V-1) and E number of edges.
# Find and print the shortest distance from the source vertex (i.e. Vertex 0) to all other vertices (including source vertex also) using Dijkstra's Algorithm.
# Input Format :
# Line 1: Two Integers V and E (separated by space)
# Next E lines : Three integers ei, ej and wi, denoting that there exists an edge between vertex ei and vertex ej with weight wi (separated by space)
# Output Format :
# For each vertex, print its vertex number and its distance from source, in a separate line. The vertex number and its distance needs to be separated by a single space.
# Note : Order of vertices in output doesn't matter.
# Constraints :
# 2 <= V, E <= 10^5
# Time Limit: 1 sec
# Sample Input 1 :
# 4 4
# 0 1 3
# 0 3 5
# 1 2 1
# 2 3 8
# Sample Output 1 :
# 0 0
# 1 3
# 2 4
# 3 5

___________________________________________________________________________