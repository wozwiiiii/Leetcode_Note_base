#原网址：https://algo.itcharge.cn/01_array/01_08_array_quick_sort/
"""
适用场景：
大规模数据排序（n≥1000）
对平均性能要求高的场景
数据分布相对均匀的情况

优化策略：
随机选择基准值，避免最坏情况
三数取中法选择基准值
小数组使用插入排序
处理重复元素时使用三路快排

总结
快速排序是一种高效的排序算法，采用分治策略，通过分区操作将数组分成两部分，然后递归排序。

优点：
平均情况下效率高，时间复杂度为O(nlogn)
原地排序，空间复杂度低
缓存友好，局部性良好
实际应用中常数因子较小
缺点：
不稳定排序
最坏情况下性能较差，时间复杂度为O(n^2)
对于小数组，其他算法可能更快
递归调用可能导致栈溢出

快速排序是许多编程语言内置排序函数的实现基础，在实际应用中非常广泛。
通过合理的优化策略，可以显著提高其性能和稳定性。
"""


#代码实现
import random

class Solution:
    def randomPartition(self, nums: [int], low: int, high: int) -> int:
        # 随机选择基准值，避免最坏情况
        i = random.randint(low, high)
        # 将基准数与最低位互换
        nums[i], nums[low] = nums[low], nums[i]
        # 随机将基准数移到首位，后续进行分区操作
        return self.partition(nums, low, high)
    
    # 哨兵划分法（Hoare 法）：以 nums[low] 作为基准值
    # 左右指针分别从区间两端向中间收缩
    # 使比基准值小的元素都移动到基准值左侧
    # 使比基准值大的元素都移动到基准值右侧
    # 循环后将基准值放入最终的位置，并返回该位置索引
    def partition(self, nums: [int], low: int, high: int) -> int:
        pivot = nums[low]  # 选取基准值（当前区间第一个元素）
        i, j = low, high
        
        while i < j:
            # 从右向左找小于基准值的元素
            while i < j and nums[j] >= pivot:
                j -= 1
            # 从左向右找大于基准值的元素
            while i < j and nums[i] <= pivot:
                i += 1
            # 交换元素
            nums[i], nums[j] = nums[j], nums[i]
        
        # 将基准值放到正确位置
        nums[i], nums[low] = nums[low], nums[i]
        # 返回基准数的索引
        return i

    def quickSort(self, nums: [int], low: int, high: int) -> [int]:
        if low < high:
            # 分区并获取基准值位置
            pivot_i = self.randomPartition(nums, low, high)
            # 递归排序左右子数组
            self.quickSort(nums, low, pivot_i - 1)
            self.quickSort(nums, pivot_i + 1, high)
        return nums

    def sortArray(self, nums: [int]) -> [int]:
        return self.quickSort(nums, 0, len(nums) - 1)





"""
练习题
描述：给定一个大小为n的数组nums。

要求：返回其中的多数元素。

说明：
多数元素：指在数组中出现次数大于(n/2)的元素。
假设数组是非空的，并且给定的数组总是存在多数元素。
n==nums.length。
1≤n≤5×10^4 
−10^9≤nums[i]≤10^9。
"""