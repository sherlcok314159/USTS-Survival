"""该模块应用地图上的欧几里得距离满足三角不等式来对TSP问题近似
   1. 得到最小生成树
   2. 对最小生成树进行前序遍历(即深度优先搜索)
   3. 记下2中每一次遍历的点(重复不标记)
   4. 按照3中得到的顺序构造哈密顿图，记下代价"""
import pandas as pd


def prim(graph, vertex_num):
    """To get minimum spanning tree in Prim."""
    T = []
    INF = 1e10
    visit = [False] * vertex_num
    dist = [INF] * vertex_num
    for i in range(vertex_num):
        # In Case first loop cannot find the minimum distance
        minDist = INF + 1
        nextIndex = -1
        # to find the closest point w.r.t i
        for j in range(vertex_num):
            if dist[j] < minDist and not visit[j]:
                minDist = dist[j]
                nextIndex = j

        T.append(nextIndex)
        visit[nextIndex] = True
        for j in range(vertex_num):
            if dist[j] > graph[nextIndex][j] and not visit[j]:
                dist[j] = graph[nextIndex][j]

    return T


def DFS(graph, s):
    """Depth-First Search Algorithm."""
    order, stack = [], []
    stack.append(s)
    seen = []
    seen.append(s)
    while stack:
        vertex = stack.pop()
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.append(w)
        order.append(vertex)
    return order


def main():
    ##### TAKE CARE OF THE DATA PATH #####
    # data_path = r"F:\2022学年\算法\上机\上机7\dis.csv"
    # data_path = r"F:\2022学年\算法\上机\上机8\train_cost.csv"
    data_path = r"F:\2022学年\算法\上机\上机8\train_time.csv"
    df = pd.read_csv(data_path).values.tolist()
    # build the adj matrix
    matrix = [i[1:] for i in df]
    cities = [i[0] for i in df]
    graph = {}
    # build the minimum spanning tree
    tree = prim(matrix, len(df))
    last_value = tree[-1]
    pre_store = 0
    for (i, j) in zip(tree, tree[1:]):
        graph[i] = [j]
        if j == last_value:
            pre_store = i

    graph[last_value] = [pre_store]

    # pre-order search the tree
    order = DFS(graph, 0)

    price = 0
    for (from_, to_) in zip(order, order[1:]):
        price += matrix[from_][to_]

    # print to the console
    orig_place = order[0]
    print(f"> {cities[orig_place]}", end=" ")
    for (i, j) in zip(order, order[1:]):
        print(f"> {cities[j]}", end=" ")

    # back to the original
    print(f"> {cities[orig_place]}")
    price += matrix[j][orig_place]
    print("The Total Price is %d" % price)


if __name__ == "__main__":
    main()
