#原教程地址：https://algo.itcharge.cn/04_string/04_07_string_sunday/

"""
总结
Sunday 算法是一种高效的字符串匹配算法，通过利用窗口末尾字符的后移位数表，实现大步跳跃式匹配，提升了实际查找效率，适用于大多数文本搜索场景。

优点：
实现简单，易于理解和编码。
平均性能优良，实际应用中匹配效率高。
只需构建一次后移位数表，预处理开销小。
跳跃能力强，适合大多数实际文本搜索场景。
缺点：
最坏情况下时间复杂度较高，可能退化为 O(n×m)。
只利用窗口末尾字符的信息，未充分利用更多启发式规则（如 BM 算法的好后缀规则）。
对极端重复或特殊构造的模式串不够友好，跳跃能力有限。
"""

#代码实现


# 生成 Sunday 算法的后移位数表
# bc_table[bad_char] 表示遇到坏字符 bad_char 时，模式串可以向右移动的距离
def generateBadCharTable_1(p: str):
    """
    构建 Sunday 算法的后移位数表。
    输入:
        p: 模式串
    输出:
        bc_table: 字典，key 为字符，value 为遇到该字符时可向右移动的距离
    """
    m = len(p)
    bc_table = dict()
    # 遍历模式串的每一个字符（包括最后一个字符）
    for i in range(m):
        # 对于每个字符 p[i]，记录其对应的移动距离
        # 移动距离 = 模式串长度 - 当前字符下标
        bc_table[p[i]] = m - i
        # 如果字符重复出现，保留最右侧（下标最大）的距离
    return bc_table



# Sunday 算法实现，T 为文本串，p 为模式串
def sunday(T: str, p: str) -> int:
    """
    Sunday 算法主函数，返回模式串 p 在文本串 T 中首次出现的位置，如果未匹配则返回 -1。
    参数:
        T: 文本串
        p: 模式串
    返回:
        int: 第一个匹配位置的下标，未匹配返回 -1
    """
    n, m = len(T), len(p)
    if m == 0:
        return 0  # 空模式串视为匹配在开头

    bc_table = generateBadCharTable(p)  # 生成后移位数表

    i = 0  # i 表示当前窗口在文本串中的起始下标
    while i <= n - m:
        # 逐字符比较当前窗口是否与模式串完全匹配
        j = 0
        while j < m and T[i + j] == p[j]:
            j += 1
        if j == m:
            return i  # 匹配成功，返回起始下标
        # 检查窗口末尾的下一个字符，决定滑动距离
        if i + m >= n:
            return -1  # 已到文本串末尾，未匹配
        next_char = T[i + m]  # 当前窗口末尾的下一个字符
        # 如果 next_char 在后移位数表中，滑动对应距离，否则滑动 m+1
        shift = bc_table.get(next_char, m + 1)
        i += shift
    return -1  # 未找到匹配

# 生成 Sunday 算法的后移位数表
# bc_table[bad_char] 表示遇到坏字符 bad_char 时，模式串可以向右移动的距离
def generateBadCharTable(p: str):
    """
    构建 Sunday 算法的后移位数表。
    参数:
        p: 模式串
    返回:
        dict: 字典，key 为字符，value 为遇到该字符时可向右移动的距离
    """
    m = len(p)
    bc_table = dict()
    # 遍历模式串每个字符（包括最后一个字符）
    for i in range(m):
        # 记录每个字符在模式串中最右侧出现时可向右移动的距离
        bc_table[p[i]] = m - i
    return bc_table

# 测试用例
print(sunday("abbcfdddbddcaddebc", "aaaaa"))  # 输出: -1，未匹配
print(sunday("abbcfdddbddcaddebc", "bcf"))    # 输出: 2，匹配成功