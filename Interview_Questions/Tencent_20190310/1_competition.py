# -*- coding: UTF-8 -*-
# description: 在一场比赛中，有n个检查点，比赛的要求是到达n-1个检查点即可，这些检查点排列在X轴上，位置分别为x1,x2,...,xn,且允许以任意
#              顺序访问检查点，比赛的开始位置为a,现在问完成比赛所需经过的最小距离是多少。

# example: input:3 10  (输入包含两行，第一行为两个参数n,a,其中1<=n<=1e5,-1e6<=a<=1e6)
#                1 7 12  (第二行为n个整数，表示x1,x2,...,xn, 且-1e7<=xi<=1e6)
#
#          output:7    (输出一个整数表示问题的解)


"""
@param string line 一个测试用例
@return string 处理后的结果
"""


def solution(line):
    points = [int(x) for y in line.split('\n') for x in y.strip().split()]
    n = points.pop(0)
    a = points.pop(0)
    if a <= points[0]:
        return points[-2] - a
    elif a >= points[-1]:
        return a - points[1]
    else:  # 排除上面两种情况，说明起码有两个点，而a在两者间
        tmp_1 = min(a - points[0] + points[-2] - points[0], abs(points[-2] - a) + points[-2] - points[0])
        tmp_2 = min(abs(a - points[1]) + points[-1] - points[1], points[-1] - a + points[-1] - points[1])
        return min(tmp_1, tmp_2)


test = "3 10\n 1 7 12"
print(solution(test))


# 一共有n个点，设从小到大排序，x1到xn。由于要访问n-1个点，即抛弃一个点不访问。
# 设抛弃的点在中间，即2到n-1,由于要访问1和n,这些中间的点可以顺便访问，而不增加负担，
# 反而可以访问中间的点而不访问最小点或者最大点来减小负担。所以不访问的那个点要么是1,要么是n。而这依赖于a的位置。

# 假设a小于等于点1，则不访问的点是n。假设a大于等于点n,则不访问的点是1。这些都是平凡的情况。
# 设a在点1和点n之间，不失一般性，设不访问的点是n,则要访问点1到点n-1。
# 则最佳的访问的候选情况只有两种，一种是先向左访问到1，再向右访问到n-1，另外一种则恰好相反。
# 因为如果在中间某点转向，则有一段距离会被重复三次。一定是在点1或者点n-1处转向。
# 这两种访问中，前者重复了一遍a到点1，后者重复了一遍a到点n，比较则可知道最佳的访问。
# 则综上有：a<=x1时：d=X_(n-1) - a
#          a>=xn时：d= a - x2
#          x1<a<xn时：d在以下情况选最小的:
#                    1.不访问点n,则为 min{ a-x1+x(n-1)-x1, |x(n-1)-a|+x(n-1)-x1 }
#                    2.不访问点1,则为 min{ |a-x2|+xn-x2, xn-a+xn-x2}
