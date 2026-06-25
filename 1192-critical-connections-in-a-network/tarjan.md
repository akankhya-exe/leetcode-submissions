Purpose of Tarjan's Algorithm

Tarjan's Algorithm is a graph traversal algorithm that uses Depth-First Search (DFS) to efficiently identify important structural properties of a graph in O(V + E) time. While it is commonly used to find Strongly Connected Components (SCCs) in directed graphs, it can also be adapted to identify bridges (critical connections) and articulation points in undirected graphs. In LeetCode 1192 (Critical Connections in a Network), Tarjan's Algorithm is used to detect all critical connections—edges whose removal disconnects the graph.

Brief Explanation

A normal DFS only explores the graph and determines whether nodes are reachable, but it cannot determine whether an edge is a critical connection without repeatedly removing edges and traversing the graph again. Tarjan's Algorithm enhances DFS by assigning each node a discovery time and computing a low-link value, which represents the earliest discovered node that can be reached from the current node through DFS tree edges and back edges. During traversal, if a child node cannot reach any ancestor of its parent (i.e., low[child] > discovery[parent]), then the edge connecting them is the only path between those parts of the graph and is therefore a critical connection (bridge). This allows all critical connections to be identified efficiently in a single DFS traversal.

Time Complexity: O(V + E)
Space Complexity: O(V + E) (adjacency list and recursion stack)
