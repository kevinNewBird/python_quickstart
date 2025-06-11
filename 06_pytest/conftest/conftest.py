import pytest


# 测试的配置文件
# 钩子函数
@pytest.fixture()
def test_url():
    return 'http://www.baidu.com'
