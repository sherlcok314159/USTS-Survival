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


# n => 序列数目
# a => 各序列中元素数
# count => 排序次数
def merge(n, a):
    count, i = 0, 0
    # 升序排列
    a = heapSort(a)
    while i < n - 1:
        # m + n - 1次
        count = count + a[i] + a[i + 1] - 1
        # 合并
        a[i] = a[i] + a[i + 1]
        a[i + 1] = 0
        i += 1
        a = heapSort(a)
    # return count
    print(count)


def main():
    n = int(input())
    a = list(map(int, input().split()))
    merge(n, a)


if __name__ == "__main__":
    main()
