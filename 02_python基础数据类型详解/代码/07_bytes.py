# bytes
s = "张三"
bs1 = s.encode("gbk")
bs2 = s.encode("utf-8")
print(bs1)  # b'\xd5\xc5\xc8\xfd'
print(bs2)  # b'\xe5\xbc\xa0\xe4\xb8\x89'

# 将一个gbk字节转换为utf-8字节
bs = b'\xd5\xc5\xc8\xfd'
## 先变成文字符号（字符串）
s2 = bs.decode("gbk")  # 解码
print(s2)
bs22 = s2.encode("utf-8")
print(bs22)
