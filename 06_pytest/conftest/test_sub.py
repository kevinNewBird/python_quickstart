# 测试用例
import threading

import pytest
import time
from log import logger
from paramObj import ParamObj


# test_url就是conftest.py里的函数，输出它就是输出它的返回值
def test_baidu(test_url):
    print(test_url)


# 每个参数便利的传入去执行
def test_param_transfer(testObj0: ParamObj):
    print(f"Executing param1:{testObj0.host}")
    logger.info(f"[xxx]Executing file:{testObj0.host}")
    time.sleep(1)

def test_params_transfer(testObj: ParamObj, username: str):
    print(f"Executing param1:{testObj.host},param2:{username}")
    logger.info(f"[yyy]Executing file:{testObj.host}")
    time.sleep(1)


if __name__ == '__main__':
    # 必须要指定目录
    # 需要安装pytest-parallel, 实际不可用，原因未知（--workers和tests-per-worker=2）
    # pytest.main(['-s', 'test_sub.py','--username=kevin', '--workers=2', '--tests-per-worker=2'])
    # 需要安装pytest-xdist（-n参数）
    pytest.main(['-s', 'test_sub.py','--username=kevin','-n','4'])
    # pytest.main(['-s', 'test_sub.py'])
    # pytest.main(['-s', '-v', './'])
