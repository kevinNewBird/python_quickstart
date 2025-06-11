# 待测试的功能
def add(x: int, y: int):
    return x + y


# 测试用例
# 使用pytest的规则：py文件必须以test开头且测试用例也必须以test开头
# 在命令行，使用./.venv/bin/06_pytest 06_pytest/01_test_sample.py 或者 直接使用./.venv/bin/06_pytest(会报找不到测试文件，原因见上，改文件名为test_Xxx即可)
def test_result():
    assert add(4, 5) == 9


# 使用代码调用pytest
# 1.首先引入pytest
# 2.最后调用pytest
import pytest

if __name__ == '__main__':
    pytest.main()
