# Python Docstring 规范与用法指南
Docstring 是 Python 中用于解释代码功能的特殊注释，通过三重引号（""" 或 '''）定义，可被工具提取生成文档

### 1.核心功能
- a.代码文档化‌
-- 描述模块、类、函数的用途、参数和返回值
-- 支持 IDE 自动提示和帮助查询（如 help(func)）
- b.‌自动化工具支持‌
-- 被 Sphinx、pdoc 等工具解析生成 API 文档
-- 嵌入 doctest 测试用例（示例代码+预期输出）
### 2.基本使用

```python
def add(a, b):
    """计算两数之和。
    
    Args:
        a (int): 第一个加数
        b (int): 第二个加数
    
    Returns:
        int: 两数之和
    
    Example:
        >>> add(2, 3)
        5
    """
    return a + b

# 通过 func.__doc__ 可访问该字符串
print(add.__doc__)
```