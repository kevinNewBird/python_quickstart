import pymysql
import numpy as np
import pandas as pd
from pandas import DataFrame

def get_conn():
    return pymysql.connect(host="192.168.231.150", port=3306, user="root", password="root@123", db="testdb")

def execute_query_sql_by_origin(conn, sql, size = None):
    """
    使用原生的方式执行sql查询
    :param conn:
    :param sql:
    :return:
    """
    size = None if size and size < 0 else size
    # 2.创建光标（表示对mysql要做什么操作，类似java中的statement）
    stmt = conn.cursor()
    # 3.执行查询(返回结果为数据的行数)
    lines = stmt.execute("select * from tb1_demo;")
    return lines, (stmt.fetchall() if not size else stmt.fetchmany(size))

def execute_query_sql_by_pandas(conn, sql, size = None):
    """
        使用pandas的方式执行sql查询
        :param conn:
        :param sql:
        :return:
        """
    size = None if size and size < 0 else size
    df = pd.read_sql(sql, conn)
    # 多少行多少列： (4, 2)
    # print("多少行多少列：", df.shape)
    return df.shape[0], (df.all() if not size else df.head(size))

def execute_create_sql_by_origin(conn, sqls):
    """
        使用原生的方式执行sql查询
        :param conn:
        :param sql:
        :return:
        """
    if not sqls:
        return
    # 2.创建光标（表示对mysql要做什么操作，类似java中的statement）
    stmt = conn.cursor()
    conn.autocommit(False)
    for sql in sqls:
        try:
            stmt.execute(sql)
            conn.commit()
        except Exception as ex:
            print("执行{}失败\n".format(sql), ex)
            conn.rollback()

# 1.连接mysql
conn = get_conn()
sql = "select * from tb1_demo;"

# 2.1.执行原生的sql查询
# data = execute_sql_by_origin(conn, sql, -1)
# 2.2.使用pandas执行sql查询
data = execute_query_sql_by_pandas(conn, sql, 2)
print("行数：",data[0], "\n数据：\n",data[1])

# 2.3.创建数据库和表
sqls = ("create database if not exists testdb;", "use testdb;", "create table if not exists tb1_demo2(id int primary key auto_increment, name varchar(20));")
execute_create_sql_by_origin(conn, sqls)

# 2.4.插入数据
sqls = ("insert into tb1_demo2(name) values('a');",)
execute_create_sql_by_origin(conn, sqls)
# 3.关闭连接
conn.close()