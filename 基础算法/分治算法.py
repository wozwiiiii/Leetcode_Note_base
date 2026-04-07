#https://algo.itcharge.cn/07_algorithm/07_03_divide_and_conquer_algorithm/




#代码模板
"""
def divide_and_conquer(problem_n):
    '''
    分治算法通用模板
    :param problem_n: 问题规模
    :return: 原问题的解
    '''
    # 1. 递归终止条件：当问题规模足够小时，直接解决
    if problem_n < d:  # d 为可直接求解的最小规模
        return solve(problem_n)  # 直接求解（注意：原代码有拼写错误，应为 solve）

    # 2. 分解：将原问题分解为 k 个子问题
    problems_k = divide(problem_n)  # divide 函数返回 k 个子问题的列表

    # 3. 递归求解每个子问题
    res = []
    for sub_problem in problems_k:
        sub_res = divide_and_conquer(sub_problem)  # 递归求解子问题
        res.append(sub_res)  # 收集每个子问题的解

    # 4. 合并：将 k 个子问题的解合并为原问题的解
    ans = merge(res)
    return ans  # 返回原问题的解
"""