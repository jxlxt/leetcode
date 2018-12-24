class Solution:
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        start_str = ''.join([str(i) for i in (board[0] + board[1])])
        swap_pos = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
        visited, step = set(), 0
        cur_list, next_list = [start_str], []
        while cur_list:
            for cur in cur_list:
                if cur == '123450':
                    return step
                ind = cur.index('0')
                for pos in swap_pos[ind]:
                    next_str_list = [ch for ch in cur]
                    next_str_list[ind], next_str_list[pos] = next_str_list[pos], next_str_list[ind]
                    next_str = ''.join(next_str_list)
                    if next_str not in visited:
                        visited.add(next_str)
                        next_list.append(next_str)
            cur_list, next_list = next_list, []
            step += 1
        return -1

