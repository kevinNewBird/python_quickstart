import requests
from requests import cookies

# adv: 认证授权。即对于登录系统的爬虫如何模拟浏览器效果，达到数据爬取的目的。
# 本质上， 认证和授权通过cookie或者token两种方式。所以请求登录系统认证后，获取到相关的授权信息后，下次请求带着授权信息就可以访问网站真实数据

# 模拟登录的情况，设置cookie
jar = requests.cookies.RequestsCookieJar()
jar.set("__bid_n","197e808f0059984989c963",domain=".baidu.com", path="/")
jar.set("BA_HECTOR","a0818g2l04248l81a12k25a1a504001k966m624",domain=".baidu.com", path="/")
jar.set("BAIDUID","DC291A6F6F636A8C4F7AE03CC14EDA76:FG=1", domain=".baidu.com", path="/")
jar.set("BAIDUID_BFESS","DC291A6F6F636A8C4F7AE03CC14EDA76:FG=1", domain=".baidu.com", path="/")
jar.set("BCLID", "9836183298399657015", domain=".baidu.com", path="/")
jar.set("BCLID_BFESS","9836183298399657015", domain=".baidu.com", path="/")
jar.set("BD_CK_SAM","1", domain="www.baidu.com", path="/")
jar.set("BD_HOME","1", domain="www.baidu.com", path="/")
jar.set("BD_UPN","123253", domain="www.baidu.com", path="/")
jar.set("BDORZ","B490B5EBF6F3CD402E515D22BCDA1598", domain=".baidu.com", path="/")
jar.set("BDSFRCVID","Gb8OJeC627DckGJsug8oT99MimKv7fTTH6aouqoFUzozGh-kcAstEG0PtU8g0Ku-eGcEogKKXgOTHw0F_2uxOjjg8UtVJeC6EG0Ptf8g0M5", domain=".baidu.com", path="/")
jar.set("BDSFRCVID_BFESS","Gb8OJeC627DckGJsug8oT99MimKv7fTTH6aouqoFUzozGh-kcAstEG0PtU8g0Ku-eGcEogKKXgOTHw0F_2uxOjjg8UtVJeC6EG0Ptf8g0M5", domain=".baidu.com", path="/")
jar.set("BDUSS","ZsdFNtUmpkeWFvfkFIWDdnSTRoS1lZQ2E3c1JEMjJyWVo1elNEclkwcGl2N3BvSVFBQUFBJCQAAAAAAAAAAAEAAABX8jkdenN1dGFyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGIyk2hiMpNoS3", domain=".baidu.com", path="/")
jar.set("BDUSS_BFESS","ZsdFNtUmpkeWFvfkFIWDdnSTRoS1lZQ2E3c1JEMjJyWVo1elNEclkwcGl2N3BvSVFBQUFBJCQAAAAAAAAAAAEAAABX8jkdenN1dGFyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGIyk2hiMpNoS3", domain=".baidu.com", path="/")
jar.set("BIDUPSID","652968AD61280136349DB0D4CBBD0541", domain=".baidu.com", path="/")
jar.set("COOKIE_SESSION","22670_1_5_9_3_9_1_0_5_9_252_0_5455_0_0_2_1754447714_1754475802_1754475800%7C9%23704387_36_1754475800%7C8", domain="www.baidu.com", path="/")
jar.set("H_BDCLCKID_SF", "tJItVIKKJIvbfP0k-J32h-QH-UnLetJXf2vaVp7F5l8-hC3e-PRnyRt0bN7yLTF8BC5La-L55fbxOKQphnoahUKA2xnE0-kL2K7CQ-bN3KJmfMK9bT3v5Du8QUb42-biWabM2MbdbKJP_IoG2Mn8M4bb3qOpBtQmJeTxoUJ25DnJhhCGe4bK-TrBDNAqJUK", domain=".baidu.com", path="/")
jar.set("H_BDCLCKID_SF_BFESS", "tJItVIKKJIvbfP0k-J32h-QH-UnLetJXf2vaVp7F5l8-hC3e-PRnyRt0bN7yLTF8BC5La-L55fbxOKQphnoahUKA2xnE0-kL2K7CQ-bN3KJmfMK9bT3v5Du8QUb42-biWabM2MbdbKJP_IoG2Mn8M4bb3qOpBtQmJeTxoUJ25DnJhhCGe4bK-TrBDNAqJUK", domain=".baidu.com", path="/")
jar.set("H_PS_PSSID","62325_63143_63325_63881_63948_64008_64125_64168_64174_64183_64210_64248_64245_64252_64259_64261_64295_64270_64317_64342_64359_64366_64362_64363_64386", domain=".baidu.com", path="/")
jar.set("H_WISE_SIDS","62325_63143_63325_63881_63948_64008_64125_64168_64174_64183_64210_64248_64245_64252_64259_64261_64295_64270_64317_64342_64359_64366_64362_64363_64386", domain=".baidu.com", path="/")
jar.set("H_WISE_SIDS_BFESS","62325_63143_63325_63881_63948_64008_64125_64168_64174_64183_64210_64248_64245_64252_64259_64261_64295_64270_64317_64342_64359_64366_64362_64363_64386", domain=".baidu.com", path="/")
jar.set("HOSUPPORT","1", domain=".passport.baidu.com", path="/")
jar.set("MAWEBCUID","web_cClIAOzDvENqFGFgGarUGmndYEPdsuFZtGsgnkGJvlpKYblGTb", domain=".baidu.com", path="/")
jar.set("MCITY","-%3A", domain=".baidu.com", path="/")
jar.set("PSINO","7", domain=".baidu.com", path="/")
jar.set("PSTM","1744206932", domain=".baidu.com", path="/")
jar.set("PTOKEN","7f3ab11397e64b230e9cd089cb90e66e", domain=".passport.baidu.com", path="/")
jar.set("PTOKEN_BFESS","7f3ab11397e64b230e9cd089cb90e66e", domain=".passport.baidu.com", path="/")
jar.set("STOKEN","be1f06d18a687536a4e695ea3cefebb80ef68470b7657cffd101f1aa98696487", domain=".passport.baidu.com", path="/")
jar.set("STOKEN_BFESS","be1f06d18a687536a4e695ea3cefebb80ef68470b7657cffd101f1aa98696487", domain=".passport.baidu.com", path="/")
jar.set("SAVEUSERID","10db9e5a1ddf3bd93f29", domain=".passport.baidu.com", path="/")
jar.set("SAVEUSERID_BFESS","10db9e5a1ddf3bd93f29", domain=".passport.baidu.com", path="/")
jar.set("UBI","fi_PncwhpxZ%7ETaJc7A2iB%7E3wSKgTEfTszWhz1sx1m7dPb8E1G3LWYNTQR9fFE8MOY6VmvkOzfyaHxGDGclt", domain=".passport.baidu.com", path="/")
jar.set("UBI_BFESS","fi_PncwhpxZ%7ETaJc7A2iB%7E3wSKgTEfTszWhz1sx1m7dPb8E1G3LWYNTQR9fFE8MOY6VmvkOzfyaHxGDGclt", domain=".passport.baidu.com", path="/")
jar.set("USERNAMETYPE","1", domain=".passport.baidu.com", path="/")
jar.set("USERNAMETYPE_BFESS","1", domain=".passport.baidu.com", path="/")
jar.set("XFCS","28AC561A354F527BAD9359462941882826120C918B34FD345F6AEAB8F05C991F", domain="www.baidu.com", path="/")
jar.set("XFI","838c4ac0-72b2-11f0-abe8-1b8e9056eb35", domain="www.baidu.com", path="/")
jar.set("XFT","YPkOIEoDIr9oF+W0REKJgG0rs3aeOU2jW01Tf80TG/E=", domain="www.baidu.com", path="/")
jar.set("ZFY","bafQUU8Y1rfv:AiWnwsk:A9YPQrbRRpPfIytcZOO6XH5U:C", domain=".baidu.com", path="/")


# 请求
url = "https://www.baidu.com/my/index"
resp = requests.get(url, cookies=jar)
print(resp.text)
