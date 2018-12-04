import collections
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # (k - 1) * (n + 1) + p
        # which p is the frequency equals to the largest one
        task_count = collections.Counter(tasks).values()
        most_freq, p = max(task_count), 0
        for count in task_count:
            if count == most_freq:
                p += 1
        return max(len(tasks), (most_freq - 1) * (n + 1) + p)
