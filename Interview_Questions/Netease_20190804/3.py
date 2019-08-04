# 题目大意是一个正整数N的X进制和Y进制的两种表示被连在了一起，得到了一个无法识别的数字Z。现在输入X,Y,Z，输出N的十进制表示。
# 比如输入“5 2 113221101000101”，则正确的输出是837。

import sys
T = int(sys.stdin.readline().strip())
keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
values = [10, 11, 12, 13, 14, 15]
d = dict(zip(keys, values))

for _ in range(T):
    sample = input().strip().split()
    X, Y, Z = int(sample[0]), int(sample[1]), sample[2]
    length = len(Z)

    if X == Y:
        print(str(int(Z[:length // 2], X)))

    elif X < Y:
        mid = 0
        while mid < length:
            if Z[mid] in d:
                tmp = d[Z[mid]]
            else:
                tmp = int(Z[mid])
            if tmp >= X:
                mid -= 1
                break
            mid += 1
        print(mid)
        for i in range(mid, 0, -1):
            if int(Z[:i+1], X) == int(Z[i+1:], Y):
                print(str(int(Z[:i+1], X)))

    else:
        mid = length - 1
        while mid > 0:
            if Z[mid] in d:
                tmp = d[Z[mid]]
            else:
                tmp = int(Z[mid])
            if tmp >= Y:
                mid += 1
                break
            mid -= 1

        for i in range(max(1, mid), length):
            if int(Z[:i], X) == int(Z[i:], Y):
                print(str(int(Z[:i], X)))
