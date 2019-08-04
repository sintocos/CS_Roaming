# 题目大意是输入一个工资，然后输出对应的应缴税款

import sys
T = int(sys.stdin.readline().strip())
rate = [0.03, 0.10, 0.20, 0.25, 0.30, 0.35, 0.45]
points = [3000, 12000, 25000, 35000, 55000, 80000]
interval = [3000, 9000, 13000, 10000, 20000, 25000]
tax = []
for i in range(6):
    tax.append(interval[i] * rate[i])


for _ in range(T):
    remain = int(input().strip()) - 5000
    if remain <= 0:
        output = 0
    elif remain <= points[0]:
        output = remain * rate[0]
    elif remain <= points[1]:
        output = (remain - points[0]) * rate[1] + sum(tax[:1])
    elif remain <= points[2]:
        output = (remain - points[1]) * rate[2] + sum(tax[:2])
    elif remain <= points[3]:
        output = (remain - points[2]) * rate[3] + sum(tax[:3])
    elif remain <= points[4]:
        output = (remain - points[3]) * rate[4] + sum(tax[:4])
    elif remain <= points[5]:
        output = (remain - points[4]) * rate[5] + sum(tax[:5])
    else:
        output = (remain - points[5]) * rate[6] + sum(tax[:6])
    print(round(output))
