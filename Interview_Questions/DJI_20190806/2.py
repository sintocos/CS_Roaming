# 给一个整数N(1<N<10**18),判断能否将N的各个数位重排，得到一个新的数(不能含前缀0)是2的整数次幂。
# 能则返回true,不能则返回false。
# 此题和Leetcode 869一致，不过将范围由10**9放大到10**18。

# 一种方法是全排列，产生所有的排列组合，然后判断一个排列是不是2的幂。先检查该数字有没有前置0，再不断除以2直到当前数为奇数，如果结果是1，说明是2的幂。
# 时间复杂度： O((logN)! * logN)。 空间复杂度： O(logN)。

# 另外一种方法是计数，检查两个数的组成数字是不是一样的，即检查N是不是和这些2的幂拥有一样的数字构成。
# 具体的代码如下，时间复杂度： O((logN）**2),空间复杂度： O(logN)。


import collections


def reorder_test(self, N):
    count = collections.Counter(str(N))
    return any(count == collections.Counter(str(1 << b)) for b in range(60))  # 2**60次方可以保证大于10**18

