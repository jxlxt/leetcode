class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        left, right, start, end = [], [], newInterval.start, newInterval.end
        for interval in intervals:
            if interval.end < newInterval.start:
                left.append(interval)
            elif interval.start > newInterval.end:
                right.append(interval)
            else:
                start = min(interval.start, start)
                end = max(interval.end, end)
        return left + [Interval(start, end)] + right
