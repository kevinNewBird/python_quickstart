# 0.前置知识
## 0.1.字符集和编码

| 编码格式 | 字节大小                                                                    | 备注                   |
| -------- |-------------------------------------------------------------------------| ---------------------- |
| ascii    | 8bit , 1byte                                                            |                        |
| gbk      | 16bit, 2byte                                                            | windows默认            |
| unicode  | 32bit, 4byte                                                            | 只是一个标准（没法用） |
| utf-8    | 最短的位长8:</br>- 英文：8bit ， 1byte</br>- 欧洲：16bit，2byte</br>- 中文：24bit，3byte | mac默认                |
| utf-16   | 最短的位长16                                                                 |                        |

注意事项：gbk是基于ascii标准做到扩展，utf-8和utf-16是基于unicode标准做的扩展。所以gbk和utf8/utf16之间无法直接转换。
# 1.bytes
## 1.1.定义
python中的bytes类型叫做“字节串”，与“字符串”类型类似，“字节串”是把多个“字节”串在一起。
## 1.2.常用操作
encode：编码。</br>
decode：解码。
```python
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
bs22 = s2.encode("utf-8")
print(bs22)
```
