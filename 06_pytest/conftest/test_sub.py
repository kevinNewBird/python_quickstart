# 测试用例
import pytest
import conftest


# test_url就是conftest.py里的函数，输出它就是输出它的返回值
def test_baidu(test_url):
    print(test_url)


if __name__ == '__main__':
    # 必须要指定目录
    pytest.main(['-s', '-v', './'])
