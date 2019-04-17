class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        # minDistance = len(words)
        # index_1, index_2 = -1, -1
        # for i in range(len(words)):
        #     if words[i] == word1:
        #         index_1 = i
        #     elif words[i] == word2:
        #         index_2 = i
        #     if index_1 != -1 and index_2 != -1:
        #         minDistance = min(minDistance, abs(index_1 - index_2))
        # return minDistance
        # Solution 2
        minDist = len(words)
        curr, idx = None, 0
        for i, w in enumerate(words):
            if w not in (word1, word2):
                continue
            if curr and w != curr:
                minDist = min(minDist, i - idx)
            curr, idx = w, i
        return minDist
