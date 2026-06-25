class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u) 

        disc = [-1] * n # doubles as a visited sest
        low = [-1] * n

        time = 0
        bridges = []

        def dfs(node, parent):
            nonlocal time

            disc[node] = low[node] = time
            time += 1

            for nei in graph[node]:

                if nei == parent:
                    continue

                if disc[nei] == -1:
                    dfs(nei, node)

                    low[node] = min(low[node], low[nei])

                    if low[nei] > disc[node]:
                        bridges.append([node, nei])

                else:
                    low[node] = min(low[node], disc[nei])
