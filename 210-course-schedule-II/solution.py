class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        # build graph
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        q = collections.deque()

        # start with indegree 0 nodes
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        order = []

        while q:
            curr = q.popleft()
            order.append(curr)

            for neighbor in graph[curr]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    q.append(neighbor)

        # if cycle exists
        if len(order) != numCourses:
            return []

        return order
