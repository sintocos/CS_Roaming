# 输入为n,m两个正整数，要求构造由n个A和m个B组成的字符串，且该字符串里面不会包含连续三个字符相同的子字符串，即不存在"AAA"或者"BBB"这样的子字符串。
# 输出任意一个满足条件的字符串即可。


def generate_string(n, m):
    res = ""
    if n > m:
        res += "AAB" * (n - m) + "AB" * (2 * m - n)
    else:
        res += "BBA" * (m - n) + "BA" * (2 * n - m)
    return res

