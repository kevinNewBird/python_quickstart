import math

import pytest


# pytest的参数化
# 2的三次方等于8,所以是需要三个参数，即a,b,c. 其中c是结果
# 列表中的数据极为测试的参数值
@pytest.mark.parametrize(
    'a,b,c', [(2, 2, 4), (2, 3, 8), (2, 4, 17)]
)
def test_pow(a, b, c):
    assert math.pow(a, b) == c


if __name__ == '__main__':
    # （离线）生成xml测试报告到指定路径下文件里
    pytest.main(['-v', '06_test_report.py', '--junit-xml', '../report/log.xml'])
    # （在线）生成在线的测试报告
    # pytest.main(['-v', '06_test_report.py', '--pastebin', 'all'])
