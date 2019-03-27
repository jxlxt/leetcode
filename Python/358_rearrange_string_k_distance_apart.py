import heapq
import collections
"""
first, we count the frequency of each character in the string. Then, we put the result into a heap which is sorted frequency desending.
'a': 3, 'b':2, 'c':1
next we iterate the heapq untill its empty. Also we need to make sure that the same character distance is equal to k
"""
class Solution:
    def rearrangeString(self, s:str, k:int) -> str:
        # corner case
        if k == 0:
            return s
        count = collections.Counter(s)
        res, heap = [], []
        queue = collections.deque()
        for key in count:
            heapq.heappush(heap, (-count[key], key))
        while heap:
            freq, char = heapq.heappop(heap)
            res.append(char)
            freq += 1
            queue.append((freq, char))
            if len(queue) < k:
                continue
            front = queue.popleft()
            if front[0] < 0: # character frequency > 0
                heapq.heappush(heap, front)
        return "".join(res) if len(res) == len(s) else ""
        
        
# two array to store the information of count
#     def rearrangeString(self, s: str, k: int) -> str:
#         count = [0] * 26
#         valid = [0] * 26
#         for c in s:
#             count[ord(c) - ord('a')] += 1
#         res = []
#         for i in range(len(s)):
#             curr = self.findMax(count ,valid, i)
#             if curr == -1:
#                 return ""
#             count[curr] -= 1
#             valid[curr] = i + k
#             res.append(chr(ord('a')+curr))
#         return "".join(res)
        
#     def findMax(self, count, valid, index):
#         max_value = -float('inf')
#         candidate_pos = -1
#         for i in range(len(count)):
#             if count[i] > max_value and index >= valid[i] and count[i] > 0:
#                 max_value = count[i]
#                 candidate_pos = i
#         return candidate_pos
