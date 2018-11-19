class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # corner case
        if not board: return True
        if not word: return False
        row, col = len(board), len(board[0])
        for i in range(row):
            for j in range(col):
                if self.search(word, board, 0, i, j):
                    return True
        return False
    # check whether can find the word start at (i, j) position
    def search(self, word, board, depth, i, j):
        if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or word[depth] != board[i][j]:
            return False
        # all the character are checked
        if depth == len(word) - 1:
            return True
        # fisrt character is founded, check the remaining part
        cur = board[i][j]
        # avoid visit again
        board[i][j] = 0
        # search four directions to check whether can find the character
        search = self.search(word, board, depth+1, i+1, j) or self.search(word, board, depth+1, i-1, j) \
                or self.search(word, board, depth+1, i, j+1) or self.search(word, board, depth+1, i, j-1)
        board[i][j] = cur
        return search
