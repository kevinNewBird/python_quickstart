# coding:utf-8
import os
import time

import click
# 简单的测试
import pytest


def init_dir(now_time):
    os.mkdir(os.getcwd() + '/test_report/' + now_time)


@click.command()
def run():
    print('执行完成，生成测试结果')
    now_time = time.strftime('%Y_%m-%d_%H_%M_%S')

    # 创建目录
    init_dir(now_time)

    # 构建html测试报告的路径
    html_report = os.getcwd() + '/test_report/' + now_time + '/result.html'

    # 编写动行
    pytest.main(['-s', '-v', './test_dir', '--html=' + html_report])


if __name__ == '__main__':
    # pytest.main(['-v','./test_dir'])'
    run()
