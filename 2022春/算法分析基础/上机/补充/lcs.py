def LCS(X, Y):
    m = len(X)
    n = len(Y)
    X.insert(0, "0")
    Y.insert(0, "0")
    c = [([0] * (n + 1)) for i in range(m + 1)]  # 二维数组c存放公共子序列的长度
    b = [([0] * (n + 1)) for i in range(m + 1)]  # 二维数组b存放各个子问题最优值的来源
    for i in range(0, m + 1):
        for j in range(0, n + 1):
            if i == 0 or j == 0:
                c[i][j] = 0
            elif X[i] == Y[j]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = 0
            elif c[i][j - 1] >= c[i - 1][j]:
                c[i][j] = c[i][j - 1]
                b[i][j] = 1
            else:
                c[i][j] = c[i - 1][j]
                b[i][j] = -1
    return c, b


def printLCS(b, X, i, j):
    global res
    if i == 0 or j == 0:
        return 0
    if b[i][j] == 0:
        printLCS(b, X, i - 1, j - 1)
        res.append(X[i])
    elif b[i][j] == 1:
        printLCS(b, X, i, j - 1)
    else:
        printLCS(b, X, i - 1, j)


X = input()
Y = input()
res = []
m_ = list(map(str, X.strip().split()))
n_ = list(map(str, Y.strip().split()))
m = len(m_)
n = len(n_)
# print(m)
# print(n)
c, b = LCS(m_, n_)
printLCS(b, m_, m, n)
# print("其公共子序列为：",end='')
print(res)
