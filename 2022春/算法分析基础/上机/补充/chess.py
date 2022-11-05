import math
def chesstable(row,column,x,y,size):#row,column左上角，x，y特殊棋格，size行数
    global title
    global chess
    if size == 1:# 递归终止条件
        return
    title = title + 1
    number = title
    half = size // 2
    centerrow = row + half#中间点的位置
    centercolumn = column + half
    
    #特殊棋格在左上方
    if(x < centerrow and y < centercolumn):
        chesstable(row,column,x,y,half)#与原问题相同，递归
    else:
        chess[centerrow - 1][centercolumn -1] = number#不在则填充左上棋盘的右下角
        chesstable(row,column,centerrow - 1,centercolumn -1,half)#然后覆盖其他格子
    #特殊棋格在右上棋盘
    if(x < centerrow and y >= centercolumn):
        chesstable(row,centercolumn,x,y,half)
    else:
        chess[centerrow -1][centercolumn] = number
        chesstable(row,centercolumn,centerrow - 1,centercolumn,half)
    #特殊棋格在左下棋盘
    if(x >= centerrow and y < centercolumn):
        chesstable(centerrow,column,x,y,half)
    else:
        chess[centerrow][centercolumn - 1] = number
        chesstable(centerrow,column,centerrow,centercolumn - 1,half)
    #特殊棋格在右下棋盘
    if(x >= centerrow and y >= centercolumn):
        chesstable(centerrow,centercolumn,x,y,half)
    else:
        chess[centerrow][centercolumn] = number
        chesstable(centerrow,centercolumn,centerrow,centercolumn,half)   
def show(chess):
    n = len(chess)
    for i in range(n):
        for j in range(n):
            print(chess[i][j],end = ' ')
        print('')
title = 0
#print("请输入棋盘的大小：")
N = int(input())
size = 1
for i in range(N):
    size *= 2
chess = [[-1 for i in range(size)] for j in range(size)]
#print("请输入特殊棋格的位置：")
x,y = map(int,input().split())
chesstable(0,0,x-1,y-1,size)
show(chess)