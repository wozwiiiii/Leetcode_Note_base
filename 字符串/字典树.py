#原教程地址：https://algo.itcharge.cn/04_string/04_08_trie/

"""
总结
字典树（Trie）是一种高效存储和查找字符串集合的树形数据结构，通过利用字符串的公共前缀来减少重复比较，实现快速的前缀匹配和字符串检索。

优点：
查找效率高：查找单词和前缀的时间复杂度均为 O(n)，其中n 为字符串长度，比暴力匹配快很多
前缀匹配优秀：能够快速判断一个字符串是否为另一个字符串的前缀，这在搜索引擎自动补全等场景中非常有用
空间共享：具有相同前缀的单词共享路径，相比单独存储每个单词，能节省大量空间
支持动态操作：可以动态插入、删除字符串，适合需要频繁更新的字符串集合

缺点：
空间消耗较大：每个节点都需要存储子节点信息，对于稀疏的字符串集合，空间利用率不高
实现复杂度：相比简单的哈希表或数组，字典树的实现和维护更加复杂
字符集限制：使用数组实现时，字符集大小会影响空间复杂度，大字符集会显著增加内存消耗
缓存不友好：树形结构在内存中的分布可能不够连续，对 CPU 缓存不够友好
"""


#代码实现


class Node:  # 字符节点（Trie 树的节点）
    def __init__(self):
        self.children = dict()  # 子节点字典，key 为字符，value 为 Node 对象
        self.isEnd = False      # 是否为单词结尾标记


class Trie:  # 字典树（Trie）

    def __init__(self):
        """
        初始化字典树，创建一个空的根节点（根节点不保存字符）
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        向字典树中插入一个单词

        参数:
            word (str): 要插入的单词
        """
        cur = self.root  # 从根节点开始
        for ch in word:  # 遍历单词中的每个字符
            if ch not in cur.children:  # 如果当前节点没有ch这个子节点
                cur.children[ch] = Node()  # 新建一个子节点
            cur = cur.children[ch]  # 移动到子节点，继续处理下一个字符
        cur.isEnd = True  # 单词插入完成，标记结尾

    def search(self, word: str) -> bool:
        """
        查找字典树中是否存在一个完整单词

        参数:
            word (str): 要查找的单词

        返回:
            bool: 存在返回True，否则返回False
        """
        cur = self.root  # 从根节点开始
        for ch in word:  # 遍历单词中的每个字符
            if ch not in cur.children:  # 如果没有对应的子节点
                return False  # 单词不存在
            cur = cur.children[ch]  # 移动到子节点
        return cur.isEnd  # 判断是否为单词结尾

    def startsWith(self, prefix: str) -> bool:
        """
        查找字典树中是否存在某个前缀

        参数:
            prefix (str): 要查找的前缀

        返回:
            bool: 存在返回True，否则返回False
        """
        cur = self.root  # 从根节点开始
        for ch in prefix:  # 遍历前缀中的每个字符
            if ch not in cur.children:  # 如果没有对应的子节点
                return False  # 前缀不存在
            cur = cur.children[ch]  # 移动到子节点
        return True  # 前缀存在

