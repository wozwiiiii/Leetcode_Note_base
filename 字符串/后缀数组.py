#原教程地址：https://algo.itcharge.cn/04_string/04_10_suffix_array/


"""
后缀数组构建方法：
朴素排序：直接生成所有后缀并排序，时间复杂度 O(n^2*logn)，适合短串。

倍增排序：基数排序思想，时间复杂度O(nlogn)

DC3/Skew算法：线性时间 O(n) 构建，适合大数据量。


LCP 数组(时间复杂度：O(n))常用于：
  快速查找最长重复子串
  计算不同子串个数
  字符串压缩等
"""



#代码复现


# 朴素法构建后缀数组
S = "banana"
suffixes = [(S[i:], i) for i in range(len(S))]
suffixes.sort()
SA = [idx for (suf, idx) in suffixes]
print(SA)  # 输出: [5, 3, 1, 0, 4, 2]



def build_suffix_array(s):
    n = len(s)
    k = 1
    rank = [ord(c) for c in s]
    tmp = [0] * n
    sa = list(range(n))
    while True:
        sa.sort(key=lambda x: (rank[x], rank[x + k] if x + k < n else -1))
        tmp[sa[0]] = 0
        for i in range(1, n):
            tmp[sa[i]] = tmp[sa[i-1]] + \
                ((rank[sa[i]] != rank[sa[i-1]]) or
                 (rank[sa[i]+k] if sa[i]+k < n else -1) != (rank[sa[i-1]+k] if sa[i-1]+k < n else -1))
        rank = tmp[:]
        if rank[sa[-1]] == n-1:
            break
        k <<= 1
    return sa

# 示例
S = "banana"
print(build_suffix_array(S))  # 输出: [5, 3, 1, 0, 4, 2]


#LCP（最长公共前缀）数组构建
def build_lcp(s, sa):
    n = len(s)
    rank = [0] * n
    for i in range(n):
        rank[sa[i]] = i
    h = 0
    lcp = [0] * n
    for i in range(n):
        if rank[i] == 0:
            lcp[0] = 0
        else:
            j = sa[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1
    return lcp

# 示例
S = "banana"
SA = build_suffix_array(S)
LCP = build_lcp(S, SA)
print(LCP)  # 输出: [0, 1, 3, 0, 0, 2]