# 待测试的功能
def add(x: int, y: int):
    return x + y


# ----------fixture-----------
# 使用测试类
class TestAdd:

    @classmethod
    def setup_class(cls):
        print('=============setup class============')

    @classmethod
    def teardown_class(cls):
        print('-------------teardown class---------------')

    def setup_method(cls):
        print('=============setup method============')

    @classmethod
    def teardown_method(cls):
        print('-------------teardown method---------------')

    # ------------测试用例---------------
    def test_result1(self):
        assert add(4, 5) == 9

    def test_result2(self):
        assert add(4, 7) > 12


# 使用代码调用pytest
# 1.首先引入pytest
# 2.最后调用pytest
import pytest

if __name__ == '__main__':
    pytest.main(['-x', '04_test_fixture.py'])