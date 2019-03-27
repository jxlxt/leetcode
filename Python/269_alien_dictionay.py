ifrom heapq import heappush, heappop, heapify
class Solution:
    def alienOrder(self, words: 'List[str]') -> 'str':
        # topological sort
        graph = self.build_graph(words)
        return self.topological_sort(graph)
        
    def build_graph(self, words):
        graph = {}
        for word in words:
            for c in word:
                if c not in graph:
                    graph[c] = set()
        n = len(words)
        for i in range(n-1):
            for j in range(min(len(words[i]), len(words[i+1]))):
                if words[i][j] != words[i+1][j]:
                    graph[words[i][j]].add(words[i+1][j])
                    break
        return graph
                   
    def topological_sort(self, graph):
        # initialize indegree
        indegree = {node: 0 for node in graph}
        # calculate indegree
        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] = indegree[neighbor] + 1
        # use min_heap instead of queue to maintain the smallest lexicographically order
        queue = [node for node in graph if indegree[node] == 0]
        heapify(queue)
        # bfs for topological sort
        res = ""
        while queue:
            node = heappop(queue)
            res += node
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    heappush(queue, neighbor)
        if len(res) == len(graph):
            return res
        return ""
                
