# -*- coding: UTF-8 -*-
# description: 小Q正在攀登一座宝塔，塔总共有n层，但是每两层之间的净高却不相同,所以造成了小Q爬过每层的时间也不同，如果某一层的高度为x,
#              那么爬过这一层所需的时间也是x。此外，小Q还会使用一种魔法，每用一次就可以让他向上跳一层或两层。但是每次跳完后，小Q都会将魔法力
#              用完，必须爬过至少一层才能再次跳跃，可以认为小Q需要跳两次一层才休息,最后也可以跳到塔外即超过塔高，跳是不消耗时间的。
#              现在，小Q想用最短的时间爬到塔顶，这个最短时间是多少？

# example: input:5          (输入的第一行是一个数n,n表示塔的层数，n<=1e4)
#                3 5 1 8 4  (第二行为n个整数，h1,h2,...,hn,为从下往上每层的高度，1<=hi<=100)
#
#          output:1         (输出一个数表示最短时间)


"""
@param string line 一个测试用例
@return string 处理后的结果
"""


def solution(line):
    heights = [int(x) for y in line.split('\n') for x in y.strip().split()]
    num_layers = heights[0]
    if num_layers <= 2:
        return 0
    dp = [[0 for i in range(3)] for j in range(num_layers + 1)]
    dp[2] = [0, heights[1], heights[2]]
    dp[3] = [heights[1], heights[2], heights[3]]
    for i in range(4, num_layers + 1):  # 注意dp和heights从1开始计数,0处填充的是其他数据
        dp[i][0] = min(dp[i - 1][1], dp[i - 2][2])
        dp[i][1] = min(dp[i - 1][2], dp[i - 2][1] + heights[i - 1], dp[i - 2][0] + heights[i - 1])
        dp[i][2] = min(dp[i - 1][0] + heights[i], dp[i - 2][1] + heights[i])
    return min(dp[num_layers])


test = "5\n 3 5 18 8 4"
print(solution(test))

# 只要出现了爬的状态，则魔力变为2。最开始的状态是dp[0][2]=0
# 在n层的状态由以下构成{dp[n-1][2],   dp[n-1][1],   dp[n-1][0]+height[n],
#                   dp[n-2][2],   dp[n-2][1]+height[n],   dp[n-2][1]+height[n-1],   dp[n-2][0]+height[n-1]}
# 可以分成以下三组:
# dp[n][0]= min{dp[n-1][1],  dp[n-2][2]}
# dp[n][1]= min{dp[n-1][2],  dp[n-2][1]+height[n-1], dp[n-2][0]+height[n-1]}
# dp[n][2]= min{dp[n-1][0]+height[n],    dp[n-2][1]+height[n]}
#
# 那最短的时间就是 min{dp[n][0],dp[n][1],dp[n][2]}
