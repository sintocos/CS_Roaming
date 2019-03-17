# 快速幂算法   快速幂取模
# 计算 (a^b)%c

# 传统算法是先计算出a^b，再取余，的复杂度是O(b),且当a或b很大时，可能会发生溢出
# 基于(a^b)%c ==(a%c)^b %c的算法，这个很容易证明，不妨设a=k*c+e，则代入式子左边有(k*c+e)^b %c = e^b %c = (a%c)^b%c
# 继续改进：
#     有两个等式可以依赖：当b是偶数时，(a^b)%c = ((a^2)^(b/2))%c
#                     当b是奇数时，(a^b)%c = ((a^2)^(b/2)*a)%c
#     从而：当b是偶数时，(a^b)%c = ((a^2)^(b/2))%c = (((a^2)%c)^(b/2))%c
#          当b是奇数时，(a^b)%c = ((a^2)^(b/2)*a)%c = [((a^2)%c)^(b/2) %c * (a%c)]%c
#      这样的话不仅不会溢出，而且算法的时间复杂度也降到了log2(b)

def power_mod(a, b, c):
    if b == 1:
        return a % c
    else:
        if b % 2 == 0:
            return power_mod(a * a % c, b // 2, c)
        else:
            return power_mod(a * a % c, b // 2, c) * (a % c) % c


print(power_mod(2,6,5))


# 矩阵快速幂
# 1.入门https://www.jianshu.com/p/1c3f88f63dec
# 2.进阶https://www.jianshu.com/p/25eba927d9da
# 3.实战https://www.jianshu.com/p/a6d3284244c7