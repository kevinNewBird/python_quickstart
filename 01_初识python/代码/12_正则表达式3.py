from bs4 import BeautifulSoup as bs

html_content = """<!DOCTYPE html>
<html>
<head>
    <title>我的第一个网页</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f0f0f0;
        }
        h1 {
            color: #333;
        }
        p {
            color: #666;
        }
    </style>
</head>
<body>
    <h1>欢迎来到我的网站</h1>
    <p class="boldest" value="place">这是一个简单的HTML网页示例。</p>
    <p>今天是2025年7月21日</p>
    <form class="content_details">
        <div><a href="www.baidu.com">11</div>
        <div><a href="www.baidu2.com">22</div>
    </form>
    <form class="content_details">
        <div><a href="www.google.com">11</div>
        <div><a href="www.google2.com">22</div>
    </form>
</body>
</html>"""

# 需要确保安装bs4插件：https://beautifulsoup.readthedocs.io/zh-cn/v4.4.0/#id13
# 文档：https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/
# 还原网页页面为浏览器识别的，也就是dom树
soup = bs(html_content, "html.parser")
print("解析内容,优化后：", soup.prettify())

print("解析内容，文本：", soup.text)

# 查找解析dom树所有的h1标签
h1_tags = soup.find_all("h1")
print("查找dom树里所有的标签：", h1_tags)
form_letters = soup.find_all("form", class_="content_details")
print("表单，clas s= content_details的提取结果类型:", type(form_letters))
print("表单，clas s= content_details的提取结果:", form_letters)
for element in form_letters:
    print("遍历表单： ", element.div.a.get_text(), element.div.a["href"])

# 获取单个标签,如果存在多个，按顺序获取第一个
p_tag = soup.p  # <p class="boldest" value="place">这是一个简单的HTML网页示例。</p>
print("标签对象：", p_tag)
# 获取标签的名字
p_tag_name = p_tag.name  # p
print("标签名字：", p_tag_name)
# 获取标签的单个或多个属性
p_attrs = p_tag.attrs  # {'class': ['boldest'], 'value': 'place'}
print("p标签的属性：", p_attrs)
print("p标签的class属性值：", p_tag['class'])  # ['boldest']
print("p标签的value属性值：", p_tag['value'])  # place

print(type(soup.body.contents))
print(soup.body.contents)
print(type(soup.body.contents[0]))
print(type(soup.body.contents[1]))
