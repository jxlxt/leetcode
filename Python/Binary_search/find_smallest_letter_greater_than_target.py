class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if letter[-1] <= target:
            return letters[0]
        
        low, high = 0, len(letters) - 1
        while low < high:
            mid = low + (high - low) // 2
            if letters[mid] > target:
                high = mid
            else:
                low = mid + 1
        return letters[low]
