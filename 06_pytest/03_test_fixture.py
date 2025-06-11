# 待测试的功能
def add(x: int, y: int):
    return x + y


# ----------fixture-----------
# 即测试用例执行的前置或后置执行操作

# 1.1.所有测试用例执行之前执行
def setup_module(module):
    print('setup module================')


# 1.2.所有测试用例执行之后执行
def teardown_module(module):
    print('----------------teardown_module')


# 2.1.所有测试用例执行之前执行(只会执行一次)
def setup_function(module):
    print('setup function================')


# 2.2.所有测试用例执行之后执行(只会执行一次)
def teardown_function(module):
    print('----------------teardown_function')


# ------------测试用例---------------
def test_result1():
    assert add(4, 5) == 9


def test_result2():
    assert add(4, 7) > 12


# 使用代码调用pytest
# 1.首先引入pytest
# 2.最后调用pytest
import pytest

if __name__ == '__main__':
    pytest.main(['-x', *['03_test_fixture.py']])
