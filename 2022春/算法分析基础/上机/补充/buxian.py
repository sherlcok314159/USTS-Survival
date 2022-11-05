import numpy as np
from queue import Queue


class Position(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col


def FindPath(start, finish, n, m, grid):  # 起始点，结束点，路径长，路径
    global path, PathLen1
    if start.row == finish.row and start.col == finish.col:
        Pathlen = 0
        return True
    grid[0, 0 : m + 1] = grid[n + 1, 0 : m + 1] = 1  # 设置四周的围墙
    grid[0 : n + 1, 0] = grid[0 : n + 1, m + 1] = 1
    offset = [
        Position(0, 1),
        Position(1, 0),
        Position(0, -1),
        Position(-1, 0),
    ]  # 右，下，左，上
    NumofNbers = 4
    here = start
    nbr = Position(0, 0)
    grid[start.row][start.col] = 2
    Q = Queue(maxsize=0)  # 创建一个队列
    while True:
        for i in range(NumofNbers):  # 当前点的四周的点
            nbr.row = here.row + offset[i].row
            nbr.col = here.col + offset[i].col
            if grid[nbr.row, nbr.col] == 0:  # 该方格未被标记
                grid[nbr.row, nbr.col] = grid[here.row, here.col] + 1
                if nbr.row == finish.row and nbr.col == finish.col:  # 完成布线直接结束循环
                    break
                nbr1 = Position(nbr.row, nbr.col)
                Q.put(nbr1)  # 将当前点加入队列
        if nbr.row == finish.row and nbr.col == finish.col:  # 完成布线结束循环
            break
        if Q.empty():  # 队列为空，表示无解
            return False
        here = Q.get()  # 下一个拓展结点
    Pathlen = grid[finish.row, finish.col] - 2
    PathLen1 = Pathlen
    here = finish
    for j in range(Pathlen - 1, -1, -1):  # 回溯寻找路径
        path.append(Position(here.row, here.col))  # 将当前点加入路径
        for i in range(NumofNbers):
            nbr.row = here.row + offset[i].row
            nbr.col = here.col + offset[i].col
            if grid[nbr.row, nbr.col] == j + 2:  # 找到上一个坐标
                break
        here = Position(nbr.row, nbr.col)  # 更新为上一个坐标
    return True


def main():
    global path, PathLen1
    # print("请输入方阵的行数和列数：", end='\n')
    n, m = map(int, input().split(" "))
    grid = np.zeros((n + 2, m + 2), dtype=int)
    # print("请输入方阵，不能通过的地方输入1，能通过的地方输入0：")
    for i in range(1, n + 1):
        grid[i, 1 : n + 1] = np.array(input().split(), dtype=int)
    # print("请输入起点坐标：", end='\n')
    start_x, start_y = map(int, input().split(" "))
    # print("请输入终点坐标：", end='\n')
    finish_x, finish_y = map(int, input().split(" "))
    start = Position(start_x, start_y)
    finish = Position(finish_x, finish_y)
    if FindPath(start, finish, n, m, grid):
        print(PathLen1)
        path.append(start)
        path = np.flipud(path)
        for i in range(len(path) - 1):
            print(path[i].row, end=",")
            print(path[i].col, end="-->")
        print(path[-1].row, end=",")
        print(path[-1].col)
    else:
        print("没有路径！")


global path, PathLen1
PathLen1 = 0  # 用于保存路线长度
path = []  # 保存路线
if __name__ == "__main__":
    main()

# 测试输入
# 6 6
#
# 0 0 1 0 0 0
#
# 0 0 1 1 0 0
#
# 0 0 0 0 1 0
#
# 0 0 0 1 1 0
#
# 1 0 0 0 1 0
#
# 1 1 1 0 0 0
#
# 1 2
# 4 3
