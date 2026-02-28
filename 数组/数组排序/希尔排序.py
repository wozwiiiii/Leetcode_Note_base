#源地址：https://algo.itcharge.cn/01_array/01_06_array_shell_sort/

"""
适用场景：
中等规模数据（50≤n≤1000）
对插入排序的改进需求
对稳定性要求不高的场景

总结
希尔排序是插入排序的改进版本，通过分组排序减少数据移动次数，提高排序效率。

优点：比插入排序更快，空间复杂度低，适合中等规模数据
缺点：时间复杂度不稳定，不稳定排序，间隔序列选择影响性能
"""

#代码实现
class Solution:
    def shellSort(self, nums: [int]) -> [int]:
        size = len(nums)
        gap = size // 2  # 初始间隔设为数组长度的一半

        # 不断缩小gap，直到gap为0
        while gap > 0:
            # 从gap位置开始，对每个元素进行组内插入排序
            for i in range(gap, size):
                temp = nums[i]  # 记录当前待插入的元素
                j = i
                # 在组内进行插入排序，将比 temp 大的元素向后移动
                while j >= gap and nums[j - gap] > temp:
                    nums[j] = nums[j - gap]  # 元素后移
                    j -= gap    # 向前跳 gap 步
                nums[j] = temp  # 插入到正确位置
            # 缩小 gap，通常取 gap 的一半
            gap //= 2

        return nums  # 返回排序后的数组

    def sortArray(self, nums: [int]) -> [int]:
        """排序接口，调用shellSort方法"""
        return self.shellSort(nums)