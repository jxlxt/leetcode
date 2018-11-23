class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # creat two dict to store indegree and list map
        n = numCourses
        node_neighbor = {x: [] for x in range(n)}
        node_indegree = {x: 0 for x in range(n)}
        # build graph
        for from_node, to_node in prerequisites:
            node_indegree[from_node] += 1
            node_neighbor[to_node].append(from_node)
        # add start node
        start_node = [node for node in range(n) if node_indegree[node] == 0]
        queue, res = collections.deque(start_node), []
        # go through the whole graph by BFS
        while queue:
            node = queue.popleft()
            res.append(node)
            for neighbor in node_neighbor[node]:
                node_indegree[neighbor] -= 1
                if node_indegree[neighbor] == 0:
                    queue.append(neighbor)
        if len(res) == n:
            return res
        else:
            return []
