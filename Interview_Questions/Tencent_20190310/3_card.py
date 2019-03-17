# -*- coding: UTF-8 -*-
# description: 小Q有一叠纸牌,一共有n张,从上往下依次编号为1到n。现在小Q要对这叠纸牌反复做以下操作:
#                   把当前位于顶端的牌扔掉，然后把新的顶端的牌放到新叠牌的底部。
#              小Q会一直操作到只剩下一张牌为止。小Q想知道每次丢掉的牌的编号。

# example: input:7          (输入为一行，只有一个数字n, 1<=n<=1e6)
#
#          output:1 3 5 7 4 2 6         (输出n个用空格间隔的整数，表示每次丢掉的牌的编号)


"""
@param string line 一个测试用例
@return string 处理后的结果
"""


def solution(line):
    cards = [str(x + 1) for x in range(int(line))]
    res = []
    while len(cards) > 2:
        res += [cards.pop(0)]
        cards.append(cards.pop(0))
    return " ".join(res + cards)


print(solution(8))
