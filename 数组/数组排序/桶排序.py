#源地址：https://algo.itcharge.cn/01_array/01_11_array_bucket_sort/

"""
适用场景：
数据分布均匀
外部排序
数据范围已知且有限

总结
桶排序是一种分布式排序算法，通过将数据分散到多个桶中，对每个桶单独排序后合并实现排序。

优点：数据分布均匀时效率高，适合外部排序，可并行处理
缺点：需要额外空间，数据分布不均匀时效率下降，对数据范围有要求
"""




#代码实现
class Solution:
    def insertionSort(self, nums: [int]) -> [int]:
        # 遍历无序区间
        for i in range(1, len(nums)):
            temp = nums[i]
            j = i
            # 从右至左遍历有序区间
            while j > 0 and nums[j - 1] > temp:
                # 将有序区间中插入位置右侧的元素依次右移一位
                nums[j] = nums[j - 1]
                j -= 1
            # 将该元素插入到适当位置
            nums[j] = temp
        return nums

    def bucketSort(self, nums: [int], bucket_size=5) -> [int]:
        # 计算数据范围
        nums_min, nums_max = min(nums), max(nums)
        bucket_count = (nums_max - nums_min) // bucket_size + 1
        # 定义桶数组 buckets
        buckets = [[] for _ in range(bucket_count)]

        # 遍历待排序数组元素，将每个元素根据大小分配到对应的桶中
        for num in nums:
            buckets[(num - nums_min) // bucket_size].append(num)

        # 排序并合并
        res = []
        for bucket in buckets:
            self.insertionSort(bucket)
            res.extend(bucket)
        
        # 返回结果数组
        return res

    def sortArray(self, nums: [int]) -> [int]:
        return self.bucketSort(nums)
    

"""
练习题
描述：给定一个整数数组nums，以及两个整数k、t。

要求：判断数组中是否存在两个不同下标的i和j，
其对应元素满足abs(nums[i]−nums[j])≤t，同时满足abs(i−j)≤k。
如果满足条件则返回 True，不满足条件返回 False。

说明：
0≤nums.length≤2×10^4 
-2^31≤nums[i]≤2^31 − 1
0≤k≤10^4
0≤t≤2^31 − 1。
"""    