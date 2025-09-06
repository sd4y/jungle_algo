def solve(a: list) -> int:
    n = len(a)
    result = 0
    for i in range(n):
        result += a[i]
    return result
