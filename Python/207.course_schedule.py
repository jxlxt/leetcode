class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        n = numCourses
        node_neighbor = {x: [] for x in range(n)}
        node_indegree = {x: 0 for x in range(n)}
        
        for from_node, to_node in prerequisites:
            node_indegree[to_node] += 1
            node_neighbor[from_node].append(to_node)
            
        start_node = [node for node in range(n) if node_indegree[node] == 0]
        queue, res = collections.deque(start_node), []
        
        while queue:
            node = queue.popleft()
            res.append(node)
            for neighbor in node_neighbor[node]:
                node_indegree[neighbor] -= 1
                if node_indegree[neighbor] == 0:
                    queue.append(neighbor)
        return len(res) == n
