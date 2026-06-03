from functools import reduce
import operator

def product(iterable, start=1):
    """
    计算可迭代对象中所有元素的乘积。
    
    参数:
        iterable: 包含数字的可迭代对象
        start: 初始值（默认为1，相当于乘法单位元）
    
    返回:
        所有元素的乘积
    
    示例:
        >>> product([2, 3, 4])
        24
        >>> product([1, 2, 3], start=10)
        60
        >>> product([])  # 空序列返回 start 值
        1
    """
    try:
        return reduce(operator.mul, iterable, start)
    except TypeError:
        raise TypeError("所有元素必须是数字类型")
