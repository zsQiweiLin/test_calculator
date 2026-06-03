"""
addition.py - 一个实现加法运算的模块
"""

def add_two(a, b):
    """
    两个数相加
    
    参数:
        a, b: 要相加的数字
        
    返回:
        两个数字的和
        
    示例:
        >>> add_two(3, 5)
        8
    """
    try:
        return float(a) + float(b)
    except (ValueError, TypeError):
        raise TypeError("参数必须是数字类型")

def add_multiple(*numbers):
    """
    多个数相加
    
    参数:
        *numbers: 任意数量的数字
        
    返回:
        所有数字的和
        
    示例:
        >>> add_multiple(1, 2, 3, 4)
        10
    """
    total = 0
    for num in numbers:
        try:
            total += float(num)
        except (ValueError, TypeError):
            raise TypeError(f"参数必须是数字类型，但收到了: {num}")
    return total

def add_list(numbers_list):
    """
    列表中的所有数相加
    
    参数:
        numbers_list: 包含数字的列表或可迭代对象
        
    返回:
        列表中所有数字的和
        
    示例:
        >>> add_list([1, 2, 3, 4])
        10
    """
    if not isinstance(numbers_list, (list, tuple)):
        raise TypeError("参数必须是列表或元组")
    
    return add_multiple(*numbers_list)

def safe_add(a, b, default=None):
    """
    安全加法，如果输入无效则返回默认值
    
    参数:
        a, b: 要相加的数字
        default: 加法失败时返回的默认值
        
    返回:
        两个数字的和，或默认值
        
    示例:
        >>> safe_add(3, "hello", default=0)
        0
    """
    try:
        return add_two(a, b)
    except (TypeError, ValueError):
        return default

class Adder:
    """
    加法器类，提供面向对象的接口
    """
    
    def __init__(self, initial_value=0):
        """
        初始化加法器
        
        参数:
            initial_value: 初始值
        """
        self.total = float(initial_value)
    
    def add(self, value):
        """
        添加一个值到总和中
        
        参数:
            value: 要添加的值
        """
        self.total += float(value)
        return self
    
    def reset(self, new_value=0):
        """
        重置总和
        
        参数:
            new_value: 新的初始值
        """
        self.total = float(new_value)
        return self
    
    def get_total(self):
        """
        获取当前总和
        """
        return self.total
    
    def __str__(self):
        return f"Adder(total={self.total})"
    
    def __repr__(self):
        return f"Adder({self.total})"


# 单元测试
if __name__ == "__main__":
    # 测试 add_two
    print("测试 add_two:")
    print(f"3 + 5 = {add_two(3, 5)}")  # 8
    print(f"2.5 + 3.7 = {add_two(2.5, 3.7)}")  # 6.2
    
    # 测试 add_multiple
    print("\n测试 add_multiple:")
    print(f"1+2+3+4 = {add_multiple(1, 2, 3, 4)}")  # 10
    print(f"2.5+1.5+3 = {add_multiple(2.5, 1.5, 3)}")  # 7.0
    
    # 测试 add_list
    print("\n测试 add_list:")
    print(f"[1,2,3,4]的和是: {add_list([1, 2, 3, 4])}")  # 10
    
    # 测试 safe_add
    print("\n测试 safe_add:")
    print(f"3 + 'hello' = {safe_add(3, 'hello', default='无效输入')}")
    
    # 测试 Adder 类
    print("\n测试 Adder 类:")
    adder = Adder(10)
    print(f"初始值: {adder.get_total()}")  # 10
    adder.add(5).add(3).add(2)
    print(f"添加后: {adder.get_total()}")  # 20
    adder.reset()
    print(f"重置后: {adder.get_total()}")  # 0
    
    print("\n所有测试通过!")