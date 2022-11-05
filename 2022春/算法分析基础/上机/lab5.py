global v, e, graph
global cn, bestn
global corder, bestorder
global vis
vis = [0 for i in range(100)]
corder = [0 for i in range(100)]
bestorder = [0 for i in range(100)]


def istuan(cur):
    global vis, graph
    for i in range(cur):
        if (vis[i] == 1) and (graph[i][cur] == 0):
            return 0
    return 1


def backtrack(cur):
    global v, bestn, corder, cn, vis
    if cur > v:
        if cn > bestn:
            bestn = cn
            for i in range(v + 1):
                if corder[i] != 0:
                    print(corder[i], "", end="")
        print()
        return
    if istuan(cur):
        cn += 1
        vis[cur] = 1
        corder[cur] = cur
        backtrack(cur + 1)
        cn -= 1
        vis[cur] = 0
        corder[cur] = 0
    if (cn + v - cur) > bestn:
        backtrack(cur + 1)


if __name__ == "__main__":
    global graph, cn, bestn
    cn = 0
    bestn = 0
    v = 5
    e = 7
    graph = [[0 for i in range(v + 1)] for j in range(v + 1)]
    print(graph)
    for k in range(1, e + 1):
        i, j = map(int, input().split())
        graph[i][j] = 1
    print(graph)
    backtrack(1)
    print(bestn)
