def find_best_pos(x, y):
    """Find the best position of the post office.

    Args:
        x: the horizontal ordinates of the residential areas
        y: the vertical ordinates of the residential areas

    Returns:
        total_dis: the minimum sum of the distances between
                   the post office and the residential areas
        a: the horizontal ordinate of the best position
        b: the vertical ordinate of the best position

    Example:
        >>> x = [2, 7, 3, 6, 1, 4]
        >>> y = [3, 2, 6, 9, 5, 8]
        >>> print(find_best_pos(x, y))
    """
    total_dis = 0
    length = len(x)
    x = heapSort(x)
    y = heapSort(y)
    a = x[length // 2]
    b = y[length // 2]
    for i in range(length):
        total_dis += abs(a - x[i])
        total_dis += abs(b - y[i])
    return total_dis, a, b


def heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and array[i] < array[l]:
        largest = l
    if r < n and array[largest] < array[r]:
        largest = r
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)


def heapSort(array):
    n = len(array)
    for i in range(n, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    return array


def main():
    n = int(input())
    x, y = [], []
    for i in range(n):
        xy = list(map(int, input().split()))
        x.append(xy[0])
        y.append(xy[1])
    total_dis, a, b = find_best_pos(x, y)
    print(total_dis)


if __name__ == "__main__":
    main()
