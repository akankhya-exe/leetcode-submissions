class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)

        ans = [0] * n

        indegree = [0] * n
        
        for i in edges:
            indegree[i] += 1
        
        q = collections.deque()

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        
        order = []

        while q:
            node = q.popleft()
            order.append(node)

            nxt = edges[node]
            indegree[nxt] -= 1

            if indegree[nxt] == 0:
                q.append(nxt)
        
        for i in range(n):
            if indegree[i] > 0:
                curr = i
                cnt = 0

                while True:
                    cnt += 1
                    curr = edges[curr]

                    if curr == i:
                        break
                curr = i

                while True:
                    ans[curr] = cnt
                    indegree[curr] = 0 # so it's not processed again
                    curr = edges[curr]

                    if curr == i:
                        break
        
        for node in reversed(order):
            ans[node] = ans[edges[node]] + 1
        
        return ans
        
