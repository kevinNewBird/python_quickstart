import pytest

from paramObj import ParamObj


def pytest_addoption(parser):
    parser.addoption(
        "--username",
        help="runner username"
    )


# 测试的配置文件
# 钩子函数
@pytest.fixture
def test_url():
    return 'http://www.baidu.com'


def load_data():
    obj1 = ParamObj()
    obj1.host = '1.1'
    obj1.task_json = {"a": "1"}

    obj2 = ParamObj()
    obj2.host = '2.1'
    obj2.task_json = {"b": "2"}

    return [obj1, obj2]


def pytest_generate_tests(metafunc: pytest.Metafunc):
    if "testObj0" in metafunc.fixturenames:
        # https://blog.csdn.net/paperplaneY/article/details/146120474
        # metafunc.parametrize("username", metafunc.config.getoption("username"))
        metafunc.parametrize("testObj0", load_data())
    # 测试用例形参名
    if "testObj" in metafunc.fixturenames and "username" in metafunc.fixturenames:
        # https://blog.csdn.net/paperplaneY/article/details/146120474
        # metafunc.parametrize("username", metafunc.config.getoption("username"))
        # 多个参数，argnames为N个参数， argvalues就必须是N个元组的列表
        # https://docs.pytest.org/en/stable/reference/reference.html#pytest.Metafunc.parametrize
        metafunc.parametrize("testObj,username", [tuple([load_data()[0],metafunc.config.getoption("username")])
            ,tuple([load_data()[0],metafunc.config.getoption("username")])])
