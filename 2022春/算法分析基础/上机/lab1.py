def heapify(array, n, i):
    largest = i
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
    if l < n and array[i] < array[l]:
        largest = l
    if r < n and array[largest] < array[r]:
        largest = r
    if largest != i:
        array[i], array[largest] = array[largest], array[i]  # 交换
        heapify(array, n, largest)


def heapSort(array):
    n = len(array)
    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(array, n, i)

    # 一个个交换元素
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]  # 交换
        heapify(array, i, 0)
    return array


def main():
    lis = list(map(int, input().split(",")))
    sorted_lis = heapSort(lis)
    for a in sorted_lis[:-1]:
        print(a, end=",")
    print(sorted_lis[-1], end="")


if __name__ == "__main__":
    main()
