def car_fuel(n, k, d):
    """Fueling the car.

    Args:
        n: the maximum driving distance when the fuel is full
        k: the number of gas stations
        d: the distance between every gas stations
           The first element means the distance between the departure place
           and the first gas station. And the last element means the distance
           between the destination and the last gas station.

    Returns:
        count: the fueling times
        shops: the gas stations for fueling

    Example:
        >>> n, k = 7, 7
        >>> d = [1, 2, 3, 4, 5, 1, 6, 6]
        >>> print(car_fuel(n, k, d))
    """
    count = 0
    able_drive = n
    shops = []
    for i in range(k + 1):
        if able_drive < d[i]:
            count += 1
            shops.append(i)
            able_drive = n
        able_drive -= d[i]
        if able_drive < 0:
            count = "No Solution"
            break
    # return count, shops
    print(count)
    for i in shops:
        print(i, end=" ")


def merge(n, a):
    """The best merging algorithm.

    Args:
        n: the number of sequences
        a: the length of every sequence

    Returns:
        count: the number of merging

    Example:
        >>> n = 4
        >>> a = [5, 12, 11, 2]
        >>> print(merge(n, a))
    """
    count, i = 0, 0
    a = heapSort(a)
    while i < n - 1:
        count = count + a[i] + a[i + 1] - 1
        a[i] = a[i] + a[i + 1]
        a[i + 1] = 0
        i += 1
        a = heapSort(a)
    return count


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
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    car_fuel(n, k, d)


if __name__ == "__main__":
    main()
