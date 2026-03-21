#原教程地址：https://algo.itcharge.cn/04_string/04_03_string_rabin_karp/

"""
Rabin-Karp（RK）算法通过将模式串和文本子串转化为哈希值，利用「滚动哈希」快速筛查匹配位置，大幅减少无效字符比较。
其平均时间复杂度远优于朴素算法，适合大文本和多模式串场景，但哈希冲突时需回退逐字符比对，最坏情况下复杂度与朴素法相同。
合理选择哈希参数可有效降低冲突概率，是一种高效且易于扩展的字符串匹配算法。

与 BF 相比，RK通过哈希筛选把大多数不匹配位置在O(1) 内排除；但哈希冲突会触发逐字符校验，致使最坏复杂度退化

优点：
滚动哈希使子串哈希更新为 O(1)，平均性能优于 BF；
易于扩展到多模式串场景（统一维护多哈希）。
缺点：
存在哈希冲突，最坏复杂度可退化至O(nm)；
需合理选择基数d 与大质数模 q，以降低冲突概率。
"""


#代码复现
# T: 文本串，p: 模式串，d: 字符集大小（基数），q: 模数（质数）
def rabinKarp(T: str, p: str, d: int, q: int) -> int:
    n, m = len(T), len(p)
    if m == 0:
        return 0
    if n < m:
        return -1

    hash_p, hash_t = 0, 0

    # 计算 H(p) 与首个子串的哈希
    for i in range(m):
        hash_p = (hash_p * d + ord(p[i])) % q
        hash_t = (hash_t * d + ord(T[i])) % q

    # 使用 pow 的三参形式避免中间溢出
    power = pow(d, m - 1, q)  # d^(m-1) % q，用于移除最高位字符

    for i in range(n - m + 1):
        if hash_p == hash_t:
            # 避免冲突：逐字符核验
            match = True
            for j in range(m):
                if T[i + j] != p[j]:
                    match = False
                    break
            if match:
                return i
        if i < n - m:
            # 滚动更新到下一个子串
            hash_t = (hash_t - power * ord(T[i])) % q  # 去掉最高位字符
            hash_t = (hash_t * d + ord(T[i + m])) % q  # 加入新字符

    return -1
