class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def in_bounds(r, c):
            return 0 <= r < n and 0 <= c < n

        def precompute():
            q = deque()
            min_dist = {}
            for r in range(n):
                for c in range(n):
                    if grid[r][c] == 1:
                        q.append([r, c, 0])
                        min_dist[(r, c)] = 0
            while q:
                r, c, dist = q.popleft()
                nei = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
                for r2, c2 in nei:
                    if in_bounds(r2, c2) and (r2, c2) not in min_dist:
                        min_dist[(r2, c2)] = dist + 1
                        q.append([r2, c2, dist + 1])
            return min_dist
        
        min_dist = precompute()

        maxHeap = [(-min_dist[(0, 0)], 0, 0)] # dist, r, c
        visit = set()

        while maxHeap:
            dist, r, c = heapq.heappop(maxHeap)
            dist = -dist

            if (r, c) in visit:
                continue

            visit.add((r, c))

            if (r, c) == (n - 1, n - 1):
                return dist

            nei = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
            for r2, c2 in nei:
                if in_bounds(r2, c2) and (r2, c2) not in visit:
                    dist2 = min(dist, min_dist[(r2, c2)])
                    heapq.heappush(maxHeap, (-dist2, r2, c2))
            

        
