class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # total gas - total cost > 0, means it can go through the circule
        # if at the station i, gas[i] - cost[i] < 0, it cannot make as start
        total, temp, start = 0, 0, 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            temp += gas[i] - cost[i]
            if temp < 0:
                start = i + 1
                temp = 0
        if total < 0:
            return -1
        else:
            return start
