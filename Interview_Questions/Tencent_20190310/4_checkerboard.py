# -*- coding: UTF-8 -*-
# description: 妞妞公主有一块黑白棋盘，该棋盘共有n行m列，任意相邻的两个格子都是不同的颜色(黑或白)，坐标为(1,1)的格子是白色的。
#              这一天牛牛来看妞妞公主，和妞妞公主说：只要你告诉我n和m,我就能马上算出黑色方块和白色方块的数量
#              妞妞公主说：这太简单了。这样吧，我在这n行m列中选择一个左下角坐标为(x0,y0),右上角坐标为(x1,y1)的矩形，把这个矩形里的共
#                       (x1-x0+1)*(y1-y0+1)个方块全部涂白，你还能算出黑色方块和白色方块的数量吗？
#              牛牛说：so easy，你可以在执行涂白操作后再选一个左下角坐标为(x2,y2),右上角坐标为(x3,y3)的矩形，把这个矩形里面的方块
#                       全部涂黑，我仍然能够马上算出黑色方块和白色方块的数量。
#              妞妞公主表示不相信，开始提问了T次。请问你能帮牛牛算出每次提问时棋盘的黑白方块数量吗？

# example: input:3  (输入一共包含3*T+1行，第一行输入表示T,表示提问的次数,接下来的3*T行表示T次提问,这里是3次提问)
#                1 3      (第(1+3*i)行是两个整数n,m, 表示第i次提问时棋盘的大小)
#                1 1 1 3  (第(2+3*i)行是四个整数x0,y0,x1,y1, 表示第i次提问时涂白操作时选取的两个坐标)
#                1 1 1 3  (第(3+3*i)行是四个整数x2,y2,x3,y3, 表示第i次提问时涂黑操作时选取的两个坐标)
#                3 3
#                1 1 2 3
#                2 1 3 3
#                3 4
#                2 1 2 4
#                1 2 3 3
#               (数据限制： 1<=T<=1e4, 1<=x<=n<=1e9, 1<=y<=m<=1e9, x0<=x1, y0<=y1, x2<=x3, y2<=y3)
#
#          output:0 3    (输出T行，每行两个整数表示白色方块的数量和黑色方块的数量)
#                 3 6
#                 4 8

"""
@param string line 一个测试用例
@return string 处理后的结果
"""


def solution(line):
    def square_num(i1, j1, i2, j2):
        total = (i2 - i1 + 1) * (j2 - j1 + 1)
        if total & 1:  # 总的格子数是奇数
            if (i1 + j1) & 1:  # 奇数说明左下角为黑色
                return total // 2 + 1, total // 2  # 返回黑色格和白色格子数量
            else:
                return total // 2, total // 2 + 1
        else:
            return total // 2, total // 2

    input_data = [int(x) for y in line.split('\n') for x in y.strip().split()]
    T = input_data.pop(0)
    res = ""
    for times in range(T):
        tmp_matrix = input_data[10 * times:10 * (times + 1)]  # n,m,加上八个坐标值，一共10个元素
        n, m = tmp_matrix[:2]
        x0, y0, x1, y1 = tmp_matrix[2:6]
        x2, y2, x3, y3 = tmp_matrix[6:]
        x4, y4, x5, y5 = max(x0, x2), max(y0, y2), min(x1, x3), min(y1, y3)
        t1 = square_num(1, 1, m, n)[1]
        t2 = square_num(x0, y0, x1, y1)[0]
        t3 = square_num(x2, y2, x3, y3)[1]
        t4 = square_num(x4, y4, x5, y5)[0] if x5 >= x4 and y5 >= y4 else 0
        white_num = t1 - t3 + (t2 - t4)
        black_num = n * m - white_num
        res += str(white_num) + " " + str(black_num) + "\n"
    return res


test1 = "3\n1 3\n1 1 1 3\n1 1 1 3\n3 3\n1 1 2 3\n2 1 3 3\n3 4\n2 1 2 4\n1 2 3 3"
print(solution(test1))
# output:
# 0 3
# 3 6
# 4 8
test2 = "5\n2 2\n1 1 2 2\n1 1 2 2\n3 4\n2 2 3 2\n3 1 4 3\n1 5\n1 1 5 1\n3 1 5 1\n4 4\n1 1 4 2\n1 3 4 4\n3 4\n1 2 4 2\n1 3 4 4\n3 4\n1 2 4 2\n2 1 3 3"
print(solution(test2))
# output:
# 0 4
# 3 9
# 2 3
# 8 8
# 4 8


# 总的格子数量是不变的，就是n*m，除了白色就是黑色，求得黑色方格就能知道白色方格，反之亦然。而黑白的地位是等价的，不妨求白格数量。
# 设所有矩阵从1开始计数，分析最初的矩阵，可以发现两个涂色规律：
# 1. 设某个格子的坐标为(i,j)，则i+j是偶数的话，该位置是白色，i+j是奇数的话，该位置是黑色。可以画斜率为1的直线，很容易看出。
# 2. 不妨设一个矩阵的左下角格子是白色，若矩阵的格子总数为偶数，那么该矩阵内黑白格子数相同。
#                                若矩阵的格子总数为奇数，那么该矩阵内白色格子比黑色格子多一个。
#    由于黑白地位等价，以上命题黑白可以互换，也是成立的。
# 所以根据以上两个观察，可以得到每次操作后黑白格子的数量。

# 设最初的黑白矩阵为A,被涂白的矩阵为B,被涂黑的矩阵为C。重点是B和C的交叉区域，即两者重叠的地方，不妨设为D。
# A,B,C区域已给出，而B与C重叠的区域D则为：左下角为(max(x0,x2), max(y0,y2)), 右上角为(min(x1,x3), min(y1,y3))。
# 要求白色格子的数量，就先求出A的白色格子数量t1，再求出B区域原来的黑色格子数量t2，再求出C区域原来的白色格子数量t3，再求出D区域原来的黑色格子t4。
# 那么最终白色方块的数量就是t1- t3 + (t2-t4)，即总的白格数量减去涂黑操作影响的白格子，再加上涂白操作里面受到影响的黑格子数量(重叠区域的黑格要减去)。
