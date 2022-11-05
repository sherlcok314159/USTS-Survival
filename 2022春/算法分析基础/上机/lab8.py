"""该模块采用Beam Search的思想来近似：
   1. 在第一次旅游时选择前K个可以直达的城市
   2. 接着在K个候选城市中分别进行贪心旅游"""
import pandas as pd


def greed_single_search(idx, pres_idxs, matrix):
    temp_c, temp_idx = 9999, 0
    for (i, c) in enumerate(matrix[idx]):
        # 9999 means unavailable
        if c == 9999:
            continue
        # do not repeat the city
        if i in pres_idxs:
            continue
        temp_c = c
        temp_idx = i
    return temp_c, temp_idx


def grid_all_search(idx, pres_idxs, k, matrix):
    possible_costs, possible_indexes = [], []
    for (i, c) in enumerate(matrix[idx]):
        # 9999 means unavailable
        if c == 9999:
            continue
        # do not repeat the city
        if i in pres_idxs:
            continue
        possible_costs.append(c)
        possible_indexes.append(i)

    possible_options = sorted(
        zip(possible_costs, possible_indexes), key=lambda x: x[0], reverse=False
    )
    possible_costs = [i[0] for i in possible_options]
    possible_indexes = [i[1] for i in possible_options]
    # return the first-k indexes
    return possible_costs[:k], possible_indexes[:k]


def beam_search(idx, pres_idxs, K, N, matrix):
    costs, indexes = [], []
    possible_costs, possible_indexes = grid_all_search(idx, pres_idxs, K, matrix)
    for (p_cost, p_idx) in zip(possible_costs, possible_indexes):
        # include multiple paths
        total_cost = p_cost
        pres_idxs = [idx]
        pres_idxs.append(p_idx)
        for _ in range(len(matrix)):
            temp_c, temp_idx = greed_single_search(p_idx, pres_idxs, matrix)
            if temp_c == 9999:
                break
            if total_cost + temp_c > N:
                break
            total_cost += temp_c
            pres_idxs.append(temp_idx)
            p_idx = temp_idx
        costs.append(total_cost)
        indexes.append(pres_idxs)

    final_result = sorted(zip(costs, indexes), key=lambda x: len(x[1]), reverse=True)
    return final_result[0]


def main():
    ##### ORIGNAL INDEX #####
    # index 20 > NanJing
    idx = 20
    pres_idxs = [idx]
    ##### N means the budget #####
    N = 1e10
    ##### BEAM SIZE #####
    K = 10
    ##### TAKE CARE OF THE DATA PATH #####
    data_path = r"F:\2022学年\算法\上机\上机8\train_cost.csv"
    df = pd.read_csv(data_path).values.tolist()

    # build the adj matrix
    matrix = [i[1:] for i in df]
    cities = [i[0] for i in df]

    final_costs, final_indexes = beam_search(idx, pres_idxs, K, N, matrix)
    for i in final_indexes:
        city = cities[i]
        print("->" + city, end=" ")

    print("\n最终花费为：%d" % final_costs)


if __name__ == "__main__":
    main()
