#源地址：https://algo.itcharge.cn/04_string/04_04_string_kmp/

"""
总结
KMP 算法通过预处理模式串的前缀信息，实现文本串指针不回退的高效匹配，是经典的线性时间字符串查找算法。

优点：
匹配阶段线性时间，文本指针不回退，效率稳定。
仅依赖模式串的前缀表，额外空间开销小（O(m)）。
缺点：
实现与理解相对复杂，调试成本高于朴素算法。
仅适用于精确匹配；包含通配符、编辑距离等需求需用其他算法（如 Aho–Corasick、DP、后缀结构等）。
"""


#代码实现
# 生成 next 数组
# next[j] 表示子串 p[0: j+1] 的最长相等前后缀的长度
def generateNext(p: str):
    m = len(p)
    next = [0 for _ in range(m)]  # 初始化 next 数组，全部为 0

    left = 0  # left 表示当前已知的最长相等前后缀的长度
    for right in range(1, m):  # right 表示当前考察的字符下标
        # 如果前后缀不相等，尝试回退 left 到更短的前后缀
        while left > 0 and p[left] != p[right]:
            left = next[left - 1]  # 回退到上一个最长相等前后缀
        # 如果前后缀相等，最长相等前后缀长度加一
        if p[left] == p[right]:
            left += 1
        next[right] = left  # 记录当前最长相等前后缀长度
    return next

# KMP 匹配算法，T 为文本串，p 为模式串
def kmp(T: str, p: str) -> int:
    """
    返回模式串 p 在文本串 T 中首次出现的位置（下标），如果不存在则返回 -1
    """
    n, m = len(T), len(p)
    if m == 0:
        return 0  # 空模式串视为匹配在开头

    next = generateNext(p)  # 生成 next 数组

    j = 0  # j 为模式串当前匹配到的位置
    for i in range(n):  # i 为文本串当前匹配到的位置
        # 如果当前字符不匹配，且 j > 0，则回退 j 到 next[j-1]
        while j > 0 and T[i] != p[j]:
            j = next[j - 1]
        # 如果当前字符匹配，j 向右移动
        if T[i] == p[j]:
            j += 1
        # 如果模式串全部匹配，返回匹配起始下标
        if j == m:
            return i - m + 1
    return -1  # 未找到匹配，返回 -1

# 测试用例
print(kmp("abbcfdddbddcaddebc", "ABCABCD"))  # 不存在，返回 -1
print(kmp("abbcfdddbddcaddebc", "bcf"))      # 返回 2
print(kmp("aaaaa", "bba"))                   # 不存在，返回 -1
print(kmp("mississippi", "issi"))            # 返回 1
print(kmp("ababbbbaaabbbaaa", "bbbb"))       # 返回 3