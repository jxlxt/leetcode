class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # Time complexity: O(M*N) M is the width of the matrix and N is the
        # height of the matrix
        # Space complexity: O(1)
        """
        Move to the upper right When the upper boundary is encountered, if it does not reach the right boundary, move to the right (offset: row +0, column +1), otherwise move downward (offset: row +1, column +0) )

When moving to the lower left encounters the left boundary, if it does not reach the lower boundary, it moves down (offset: row +1, column +0), otherwise it moves to the right (offset: row +0, column +1) )
        """
        if not matrix: return []
        # start point
        i, j, k = 0, 0, 1
        w, h, res = len(matrix), len(matrix[0]), []
        for _ in range(w*h):
            res.append(matrix[i][j])
            if k > 0:
                # offset to move upper right corner
                i, j = di - 1, dj + 1
            else:
                # offset to move bottom left corner
                i, j = di + 1, dj - 1
            if 0 <= di < w and 0 <= dj < h:
                i, j = di, dj
            else:
                # check for the corner
                if k > 0:
                    if j + 1 < h:
                        j += 1
                    else:
                        i += 1
                else:
                    if i + 1 < w:
                        i += 1
                    else:
                        j += 1
                k *= -1
        return ans
