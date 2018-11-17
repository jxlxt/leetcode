class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or target is None or len(matrix) == 0:
            return False
        row, column = len(matrix), len(matrix[0])
        # for i in range(row):
        #     for j in range(column):
        #         if matrix[i][j] == target:
        #             return True
        # return False
        # up, down, left, right = 0, row - 1, 0, column - 1
        # while up <= down:
        #     mid = down + (up - down) // 2
        #     if matrix[mid][0] == target:
        #         return True
        #     elif matrix[mid][0] < target:
        #         up = mid + 1
        #     else:
        #         down = mid - 1
        # if down == -1: return False
        # row_index = down
        # while left <= right:
        #     mid = left + (right - left) // 2
        #     if matrix[row_index][mid] == target:
        #         return True
        #     elif matrix[row_index][mid] < target:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # return False
        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1
        
        while low <= high:
            mid = (low + high) // 2
            num = matrix[mid // cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False
