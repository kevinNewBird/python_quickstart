# 待测试的功能
def add(x: int, y: int):
    return x + y


# 1.测试是否相等
def test_equal():
    assert add(4, 6) == 10


# 2.测试是否不相等
def test_not_equal():
    assert add(4, 6) != 10


# 3.测试大于等于
def test_greater_equal():
    assert add(4, 6) >= 10


# 4.测试小于等于
def test_less_equal():
    assert add(4, 6) <= 11


# 5.测试包含
def test_in():
    assert 'h' in 'hello'


# 6.测试不包含
def test_not_in():
    assert 'h' not in 'hello'


# 7.测试是否true
def test_true():
    assert bool(2) is True


# 8.测试是否false
def test_false():
    assert bool(2) is False


import pytest

if __name__ == '__main__':
    cases = ['02_test_assert.py']
    pytest.main(['-x', *cases])
