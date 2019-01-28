#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 1/5/19 11:30 AM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: unique_path.py
# @Software: PyCharm



def mpath(x1, y1, x2, y2, maze):
    stack = []
    dirs = [lambda x, y: (x + 1, y),
            lambda x, y: (x - 1, y),
            lambda x, y: (x, y - 1),
            lambda x, y: (x, y + 1)]
    stack.append((x1, y1))
    row, col = len(maze), len(maze[0])
    while len(stack) > 0:
        curNode = stack[-1]
        if curNode[0] == x2 and curNode[1] == y2:
            # 到达终点
            for p in stack:
                print(p)
            return True
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            if 0 <= nextNode[0] < row and 0 <= nextNode[1] < col:
                if maze[nextNode[0]][nextNode[1]] == 0:
                    # 找到了下一个
                    stack.append(nextNode)
                    maze[nextNode[0]][nextNode[1]] = -1  # 标记为已经走过，防止死循环
                    break
        else:  # 四个方向都没找到
            maze[curNode[0]][curNode[1]] = -1  # 死路一条,下次别走了
            stack.pop()  # 回溯
    print("no way out")
    return False

# 输入数据
# row, col, start, end, num_of_obstacle, point of obstacle
# 行， 列， 出发点坐标， 终点坐标，障碍数量， 障碍坐标
row, col = 3, 3
maze = [[0 for _ in range(row)] for _ in range(col)]
start = [0, 0]
end = [2, 2]
obstacle = [(1, 0), (1, 1,), (2, 0), (2, 1)]
for x, y in obstacle:
    maze[x][y] = 1
mpath(start[0], start[1], end[0], end[1], maze)
