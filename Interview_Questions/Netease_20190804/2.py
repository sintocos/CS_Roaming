# 题目大意是对于一个由大写字母构成的字符串，如果其中有连续的M(M>=4)个按字典递增顺序相邻的大写字母，则对其进行缩写，缩写为"首个字母-结束字母"的形式。
# 比如“XYZABCDMMMM”缩写成"XYZA-DMMMM"。

import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    s = input().strip()
    length = len(s)

    if length <= 3:
        print(s)
        continue

    output = ""
    left = 0
    while left < length:
        right = left
        while right + 1 < length and ord(s[right+1]) - ord(s[right]) == 1:
            right += 1
        if right - left >= 3:
            output += s[left] + "-" + s[right]
        else:
            output += s[left:right+1]
        left = right + 1
    print(output)
