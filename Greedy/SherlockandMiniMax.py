def recersive(n):
    if n == 0:
        return []
    first = recersive(n - 1)
    second = []
    count = 0
    for ch in first:
        second.append('0 ' + ch)
        count += 1
    third = []
    for i in range(count - 1, -1, -1):
        third.append('1 ' + first[i])
    return second + third


if __name__ == '__main__':
    n = int(input())
    res = recersive(n)
    for obj in res:
        print(obj)
