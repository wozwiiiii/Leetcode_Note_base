#原教程地址：https://algo.itcharge.cn/04_string/04_06_string_horspool/

"""
总结
Horspool 算法是一种基于坏字符规则的高效字符串匹配算法，通过预处理模式串构建坏字符表，实现快速跳跃以提升匹配效率，适用于大多数实际场景。

优点：
实现简单，代码量少，易于理解。
平均性能优良，适合大多数实际应用场景。
只需构建坏字符表，预处理开销小。
缺点：
最坏情况下时间复杂度较高，可能退化为 O(n×m)。
只利用坏字符规则，跳跃能力不如 BM 算法。
不适合极端重复或特殊构造的模式串。
"""


#代码实现


# 生成后移位数表
# bc_table[bad_char] 表示遇到坏字符时可以向右移动的距离
def generateBadCharTable_1(p: str):
    """
    构建 Horspool 算法的后移位数表。
    输入:
        p: 模式串
    输出:
        bc_table: 字典，key 为字符，value 为遇到该字符时可向右移动的距离
    """
    m = len(p)
    bc_table = dict()
    # 只处理模式串的前 m - 1 个字符（最后一个字符不需要处理）
    for i in range(m - 1):  # i 从 0 到 m - 2
        # 对于每个字符 p[i]，记录其对应的移动距离
        # 移动距离 = 模式串长度 - 1 - 当前字符下标
        bc_table[p[i]] = m - 1 - i
        # 如果字符重复出现，保留最右侧（下标最大）的距离
    return bc_table



# Horspool 算法实现，T 为文本串，p 为模式串
def horspool(T: str, p: str) -> int:
    """
    Horspool 字符串匹配算法。
    返回模式串 p 在文本串 T 中首次出现的位置，如果无则返回 -1。
    """
    n, m = len(T), len(p)
    if m == 0:
        return 0 if n == 0 else -1  # 约定：空模式串匹配空文本串返回 0，否则返回 -1
    if n < m:
        return -1                   # 模式串比文本串长，必不匹配

    bc_table = generateBadCharTable(p)  # 生成后移位数表

    i = 0
    while i <= n - m:
        j = m - 1
        # 从模式串末尾向前逐位比较
        while j >= 0 and T[i + j] == p[j]:
            j -= 1
        if j < 0:
            return i  # 匹配成功，返回起始下标
        # 取文本串当前窗口最右字符，查表决定滑动距离
        shift_char = T[i + m - 1]
        shift = bc_table.get(shift_char, m)  # 如果未出现则右移 m 位
        i += shift
    return -1  # 匹配失败，未找到

# 生成 Horspool 算法的后移位数表
# bc_table[bad_char] 表示遇到坏字符 bad_char 时可以向右移动的距离
def generateBadCharTable(p: str):
    """
    构建 Horspool 算法的后移位数表。
    输入:
        p: 模式串
    输出:
        bc_table: 字典，key 为字符，value 为遇到该字符时可向右移动的距离
    """
    m = len(p)
    bc_table = dict()
    # 只处理模式串的前 m - 1 个字符（最后一个字符不处理）
    for i in range(m - 1):  # i 从 0 到 m - 2
        # 对于每个字符 p[i]，记录其对应的移动距离
        # 移动距离 = 模式串长度 - 1 - 当前字符下标
        bc_table[p[i]] = m - 1 - i
        # 如果字符重复出现，保留最右侧（下标最大）的距离
    return bc_table

# 测试用例
print(horspool("abbcfdddbddcaddebc", "aaaaa"))  # -1，未匹配
print(horspool("abbcfdddbddcaddebc", "bcf"))    # 2，匹配成功