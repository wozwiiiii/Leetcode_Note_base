#原教程地址：https://algo.itcharge.cn/04_string/04_05_string_boyer_moore/

"""
总结
Boyer-Moore（BM）算法通过「坏字符规则」和「好后缀规则」两种启发式策略，实现模式串的高效跳跃移动，是实际应用中性能最优的单模式串匹配算法之一。

优点：
实际性能优异：在大多数实际应用中，BM 算法通常比 KMP 算法快 3~5 倍
跳跃能力强：通过坏字符和好后缀规则，能够跳过大量不可能匹配的位置
从右到左比较：充分利用模式串信息，减少不必要的字符比较
启发式策略：两种规则互补，最大化跳跃距离
缺点：
实现复杂：特别是好后缀规则的预处理部分，理解和实现难度较高
最坏情况退化：在特定输入下可能退化到 O(m×n) 复杂度
空间开销：需要存储坏字符表和好后缀表，空间复杂度为 O(m+σ)
预处理开销：需要预先构建两个辅助表，不适合单次匹配场景
"""


#代码复现

# 生成坏字符位置表
# bc_table[bad_char] 表示坏字符 bad_char 在模式串中最后一次出现的位置
def generateBadCharTable_1(p: str):
    """
    构建坏字符位置表。
    输入:
        p: 模式串
    输出:
        bc_table: 字典，key 为字符，value 为该字符在模式串中最后一次出现的下标
    """
    bc_table = dict()  # 初始化坏字符表

    # 遍历模式串，将每个字符及其下标记录到表中
    for i, ch in enumerate(p):
        bc_table[ch] = i  # 如果字符多次出现，保留最后一次出现的位置

    # 返回坏字符表
    return bc_table


#生成好后缀规则后移位数表
# 生成 suffix 数组
# suffix[i] 表示以 i 结尾的子串（p[0:i+1]）与模式串后缀的最大匹配长度
def generateSuffixArray_1(p: str):
    """
    构建 suffix 数组。
    输入:
        p: 模式串
    输出:
        suffix: 列表，suffix[i] 表示以 i 结尾的子串与模式串后缀的最大匹配长度
    """
    m = len(p)
    suffix = [0 for _ in range(m)]  # 初始化为 0，表示尚未匹配
    suffix[m - 1] = m               # 最后一个字符的后缀必然和自身完全匹配，长度为 m

    # 从倒数第二个字符开始向前遍历
    for i in range(m - 2, -1, -1):
        j = i                       # j 指向当前子串的起始位置
        # 比较 p[j] 与 p[m-1-(i-j)]，即从后缀和子串末尾同时向前比较
        while j >= 0 and p[j] == p[m - 1 - (i - j)]:
            j -= 1
        # 以 i 结尾的子串与模式串后缀的最大匹配长度为 i - j
        suffix[i] = i - j

    return suffix


# 生成好后缀规则后移位数表
# gs_list[j] 表示在模式串下标 j 处遇到坏字符时，根据好后缀规则可以向右移动的距离
def generateGoodSuffixList_1(p: str):
    """
    构建好后缀规则的后移位数表 gs_list。
    输入:
        p: 模式串
    输出:
        gs_list: 列表，gs_list[j] 表示在 j 处遇到坏字符时可向右移动的距离
    """
    m = len(p)
    gs_list = [m for _ in range(m)]  # 情况3：默认全部初始化为 m，表示完全不匹配时的最大移动
    suffix = generateSuffixArray(p)  # 生成后缀数组

    # 处理情况 2：寻找最长的前缀与好后缀的后缀相等
    # j 表示好后缀前的坏字符位置
    j = 0
    # 从后往前遍历，i 表示前缀的结尾下标
    for i in range(m - 1, -1, -1):
        # 如果 suffix[i] == i + 1，说明 p[0: i+1] == p[m-1-i: m]，即前缀和后缀相等
        if suffix[i] == i + 1:
            # 对于所有 j < m-1-i 的位置，如果还未被更新，则设置为 m-1-i
            while j < m - 1 - i:
                if gs_list[j] == m:
                    gs_list[j] = m - 1 - i  # 更新移动距离
                j += 1

    # 处理情况 1：模式串中存在与好后缀完全相同的子串
    # i 表示好后缀的右端点
    for i in range(m - 1):
        # m-1-suffix[i] 是好后缀的左端点
        # m-1-i 是可移动的距离
        gs_list[m - 1 - suffix[i]] = m - 1 - i  # 更新在好后缀左端点遇到坏字符时的移动距离

    return gs_list



# Boyer-Moore 字符串匹配算法实现
def boyerMoore(T: str, p: str) -> int:
    """
    Boyer-Moore 算法主函数，返回模式串 p 在文本串 T 中首次出现的位置，如果无则返回 -1。
    """
    n, m = len(T), len(p)
    if m == 0:
        return 0 if n == 0 else -1  # 约定空模式串匹配空文本串返回 0，否则 -1
    if n < m:
        return -1

    bc_table = generateBadCharTable(p)      # 生成坏字符表
    gs_list = generateGoodSuffixList(p)     # 生成好后缀表

    i = 0
    while i <= n - m:
        j = m - 1
        # 从模式串末尾向前比较
        while j >= 0 and T[i + j] == p[j]:
            j -= 1
        if j < 0:
            return i  # 匹配成功，返回起始下标
        # 坏字符规则：j - bc_table.get(T[i + j], -1)
        bad_move = j - bc_table.get(T[i + j], -1)
        # 好后缀规则：gs_list[j]
        good_move = gs_list[j]
        # 取两者最大值进行滑动
        i += max(bad_move, good_move)
    return -1

def generateBadCharTable(p: str):
    """
    生成坏字符表：记录每个字符在模式串中最后一次出现的位置。
    """
    bc_table = dict()
    for i, ch in enumerate(p):
        bc_table[ch] = i  # 只保留最后一次出现的位置
    return bc_table

def generateGoodSuffixList(p: str):
    """
    生成好后缀规则的后移位数表 gs_list。
    gs_list[j] 表示在模式串下标 j 处遇到坏字符时，根据好后缀规则可以向右移动的距离。
    """
    m = len(p)
    gs_list = [m for _ in range(m)]  # 默认全部为情况 3：最大移动 m
    suffix = generateSuffixArray(p)  # 生成后缀数组

    # 处理情况 2：寻找最长的前缀与好后缀的后缀相等
    j = 0
    for i in range(m - 1, -1, -1):
        if suffix[i] == i + 1:
            while j < m - 1 - i:
                if gs_list[j] == m:
                    gs_list[j] = m - 1 - i    # 更新移动距离
                j += 1

    # 处理情况 1：模式串中存在与好后缀完全相同的子串
    for i in range(m - 1):
        # m-1-suffix[i] 是好后缀的左端点
        gs_list[m - 1 - suffix[i]] = m - 1 - i

    return gs_list

def generateSuffixArray(p: str):
    """
    生成后缀数组 suffix。
    suffix[i] 表示以 i 结尾的子串与模式串后缀的最大匹配长度。
    """
    m = len(p)
    suffix = [m for _ in range(m)]  # 初始化为 0，表示尚未匹配
    suffix[m - 1] = m  # 最后一个字符的后缀长度为 m
    for i in range(m - 2, -1, -1):
        j = i
        # 从 i 向前与模式串后缀比较
        while j >= 0 and p[j] == p[m - 1 - i + j]:
            j -= 1
        suffix[i] = i - j
    return suffix

# 测试用例
print(boyerMoore("abbcfdddbddcaddebc", "aaaaa"))  # -1
print(boyerMoore("", ""))                         # 0
print(boyerMoore("HERE IS A SIMPLE EXAMPLE", "EXAMPLE"))  # 17
print(boyerMoore("abcabcabcabc", "abcabc"))       # 0