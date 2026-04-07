#https://algo.itcharge.cn/07_algorithm/07_04_backtracking_algorithm/






#代码模板
"""
res = []    # 存放所有符合条件结果的集合
path = []   # 存放当前递归路径下的结果

def backtracking(nums):
    '''
    回溯算法通用模板
    :param nums: 可选元素列表
    '''
    # 递归终止条件：根据具体问题设定（如 path 满足特定条件）
    if 满足结束条件:  # 例如：len(path) == len(nums)
        res.append(path[:])  # 注意要拷贝一份 path，避免后续修改影响结果
        return

    # 遍历所有可选的元素
    for i in range(len(nums)):
        # 可选：根据具体问题添加剪枝条件，如元素不能重复选取
        # if nums[i] in path:
        #     continue

        path.append(nums[i])      # 做选择，将当前元素加入 path
        backtracking(nums)        # 递归，继续选择下一个元素
        path.pop()                # 撤销选择，回退到上一步状态

# 调用回溯函数，开始搜索
backtracking(nums)
"""