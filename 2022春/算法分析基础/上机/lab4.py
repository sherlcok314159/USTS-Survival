def lcs(s1: str, s2: str) -> str:
    """Calculate the longest common subsequence.

    Example:
        >>> s1, s2 = "BCDA", "UCPA"
        >>> print(lcs(s1, s2))
    """
    matrix = [["" for x in range(len(s2))] for x in range(len(s1))]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                if i == 0 or j == 0:
                    matrix[i][j] = s1[i]
                else:
                    matrix[i][j] = matrix[i - 1][j - 1] + s1[i]
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
    cs = matrix[-1][-1]
    return cs


def main():
    s1 = "".join(input().split(" "))
    s2 = "".join(input().split(" "))
    print(list(lcs(s1, s2)))


main()
# s1, s2 = "BCDA", "UCPA"
# print(f"s1: {s1}, s2: {s2}")
