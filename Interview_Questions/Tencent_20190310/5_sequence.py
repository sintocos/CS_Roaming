# -*- coding: UTF-8 -*-
# description: 小Q得到了一个长度为n的序列A, A中的数各不相同，对于A中的每一个Ai, 求min |Ai-Aj|,其中1<=j<i
#              以及令上式取到最小值的j(记为Pi)。若最小值点不唯一，则选择使Aj较小的那个。

# example: input:3    (输入为两行，第一行是整数n,第二行n个数表示A1到An,用空格隔开，其中n<=1e5,|Ai|<=1e9)
#                1 5 3
#
#          output:4 1 (输出为n-1行，每行2个用空格隔开的整数，分别表示当i取2到n时，对应的min|Ai-Aj|和Pi的值，其中1<=j<i)
#                 2 1

"""
@param string line 一个测试用例
@return string 处理后的结果
"""


def solution(line):
    A=  [int(x) for y in line.split('\n') for x in y.strip().split()]
    n = A.pop(0)
    res =""
    for i in range(1,n):
        tmp = float('inf')
        tmp_aj,tmp_pi=0,0
        for j in range(i):
            if abs(A[i]-A[j])<tmp:
                tmp = abs(A[i]-A[j])
                tmp_aj = A[j]
                tmp_pi = j
            elif abs(A[i] - A[j])==tmp and tmp_aj>A[j]:
                tmp_aj =A[j]
                tmp_pi = j
        res += str(tmp)+" "+str(tmp_pi+1)+"\n"
    return res

test="3\n1 5 3"
print(solution(test))









