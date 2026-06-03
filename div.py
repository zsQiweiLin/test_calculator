def divide(a, b):
    """
    实现两个数的除法运算
    :param a: 被除数
    :param b: 除数
    :return: 计算结果 / 除零错误提示
    """
    # 处理除数为0的异常（数学禁忌，必须加）
    if b == 0:
        return "错误：除数不能为0"
    return a / b


# 新增一行作为修改标识