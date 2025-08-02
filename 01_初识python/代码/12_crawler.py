"""
爬虫代码。核心逻辑：
1.get_page
2.get_links
3.get_content
"""

import os
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Cookie": "BAIDUID=DC291A6F6F636A8C4F7AE03CC14EDA76:FG=1; PSTM=1744206932; BIDUPSID=652968AD61280136349DB0D4CBBD0541; BD_UPN=123253; MAWEBCUID=web_cClIAOzDvENqFGFgGarUGmndYEPdsuFZtGsgnkGJvlpKYblGTb; H_WISE_SIDS_BFESS=110085_644369_644900_645434_645170_648728_648743_648982_648960_649347_649357_649339_649595_649910_649231; MCITY=-%3A; BDUSS=djSWVDaEJCcXVaWHNNdlRGUVJvUjhCVnRoTDBEb2xTdGdremktMENSdm1GSmRvSVFBQUFBJCQAAAAAAAAAAAEAAABX8jkdenN1dGFyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOaHb2jmh29oNj; BDUSS_BFESS=djSWVDaEJCcXVaWHNNdlRGUVJvUjhCVnRoTDBEb2xTdGdremktMENSdm1GSmRvSVFBQUFBJCQAAAAAAAAAAAEAAABX8jkdenN1dGFyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOaHb2jmh29oNj; BDSFRCVID=21COJeC62iHrvXosiMsHT995egbAts7TH6aoxMCnb7EbJWy4S1qZEG0PiU8g0KuhrPyUogKKXgOTHw0F_2uxOjjg8UtVJeC6EG0Ptf8g0x5; H_BDCLCKID_SF=JJCDoI-5tD-3DbbvhPnoq4tehHRyhxc9WDTm_D_XHC3pMPQRMjKa2l3-eHo-Kbb2aj6I-pPKKR7_SCnoQqjZQptJbhQiL-bv3mkjbPoDfn02OP5dbU6oW44syPRvKMRnWTvdKfA-b4ncjRcTehoM3xI8LNj405OTbIFO0KJyJCF-hDDxj5tKj5PjbMny2-4XKKOLVb7XWl7keq8CD6uVjUQW5lb0JjoEQnK8_R5jbbO_qfj2y5jHhPCZe-R4LqcxLKbbQlv65MnpsIJMK4DWbT8U5f7MBtRzaKviaMnjBMb1fU7DBT5h2M4qMxtOLR3pWDTm_q5TtUJMeCnTDbAhe653jG8OqT0Df57y0t-82bjtHJuGeKTjhPrMDGQmWMT-0bFHBln-bfnoqnTEKU7xejc0bfJa3R3eJan7_JjOMp6TDR_6Qt5k3nc30NQDXfQxtNR0-Cnjtpvhj-oM2qoobUPUWMJ9LUvftgcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkjXIKLK-oj-DLlDTA-3j; BDSFRCVID_BFESS=21COJeC62iHrvXosiMsHT995egbAts7TH6aoxMCnb7EbJWy4S1qZEG0PiU8g0KuhrPyUogKKXgOTHw0F_2uxOjjg8UtVJeC6EG0Ptf8g0x5; H_BDCLCKID_SF_BFESS=JJCDoI-5tD-3DbbvhPnoq4tehHRyhxc9WDTm_D_XHC3pMPQRMjKa2l3-eHo-Kbb2aj6I-pPKKR7_SCnoQqjZQptJbhQiL-bv3mkjbPoDfn02OP5dbU6oW44syPRvKMRnWTvdKfA-b4ncjRcTehoM3xI8LNj405OTbIFO0KJyJCF-hDDxj5tKj5PjbMny2-4XKKOLVb7XWl7keq8CD6uVjUQW5lb0JjoEQnK8_R5jbbO_qfj2y5jHhPCZe-R4LqcxLKbbQlv65MnpsIJMK4DWbT8U5f7MBtRzaKviaMnjBMb1fU7DBT5h2M4qMxtOLR3pWDTm_q5TtUJMeCnTDbAhe653jG8OqT0Df57y0t-82bjtHJuGeKTjhPrMDGQmWMT-0bFHBln-bfnoqnTEKU7xejc0bfJa3R3eJan7_JjOMp6TDR_6Qt5k3nc30NQDXfQxtNR0-Cnjtpvhj-oM2qoobUPUWMJ9LUvftgcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkjXIKLK-oj-DLlDTA-3j; BAIDUID_BFESS=DC291A6F6F636A8C4F7AE03CC14EDA76:FG=1; delPer=0; BD_CK_SAM=1; ZFY=bafQUU8Y1rfv:AiWnwsk:A9YPQrbRRpPfIytcZOO6XH5U:C; H_PS_PSSID=62325_63143_63325_63881_63948_64008_64125_64168_64174_64183_64210_64232_64248_64245_64252_64259_64261_64295_64270_64317; BA_HECTOR=2k2g0h8hak8h8h808185010l0000ag1k8lf6024; BDRCVFR[S4-dAuiWMmn]=I67x6TjHwwYf0; H_WISE_SIDS=62325_63143_63325_63881_63948_64008_64125_64168_64174_64183_64210_64232_64248_64245_64252_64259_64261_64295_64270_64317; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ab_sr=1.0.1_M2NlOWJlZWY3ZGE2MDQ2ZDg2NmZjOGU5ZjNjYzAwNmM3MTA3NDEwYzVjZGQzMGVkMzZkYWI5NDFiNTFhMTEwOGUzNTk1ZjM4YjI4ZjY3ZGQ2ODQyODdmOWZjNGY5N2VkYmRlYjA0OWViNzliZWIwMThmNmNjMzczMGEwMWQ3NDRiNWIxNDJlMGI1ZjE1YTljNDNlMGFmNzFjYzNhYWI5Ng==; PSINO=7; H_PS_645EC=1535%2FIdgljQmh%2F%2Ff0LHw7%2BY9xYT9A9ReQksMZke1LUteoITlCUK6IIBCjMRQTioBQXf3; BDSVRTM=408; baikeVisitId=c8bbc35e-f186-4457-9ddb-5ea6265b01dd; COOKIE_SESSION=148901_2_7_9_3_16_1_0_7_7_1_11_715_0_0_0_1753772153_1753771416_1753927263%7C9%232499206_28_1753771413%7C7"
}


def search_main_page(url: str = "http://www.baidu.com/s?wd=", keyword: str = "王者荣耀"):
    search_url = url + keyword
    resp = requests.get(search_url, headers=headers)
    return resp.text


def get_page(seed: str):
    try:
        resp = requests.get(seed)
        return resp.text
    except Exception as ex:
        # log
        print("request url occur error!\n", "url:", seed, "\nexception:", ex)
        return None


def get_all_links(page_content: str):
    soup = BeautifulSoup(page_content, "lxml")
    all_links = [item['href'] for item in soup.find_all("a") if 'href' in item.attrs]

    if all_links:
        all_links = [link.strip("/") for link in all_links
                     if (link.startswith("http") or link.startswith("//"))
                     and not link.startswith("http://www.cyberpolice.cn") and not link.startswith("https://www.kalebooster.com")
                     and not link.startswith("https://twitter.com") and not link.startswith("https://server.m.pp.cn")
                     and not link.startswith("https://server.m.pp.cn") and not link.startswith("https://www.wandoujia.com")
                     and not link.startswith("https://assistant.9game.cn") and not link.startswith("https://www.9game.cn")
                     and not link.startswith("http://www.12377.cn") and not link.startswith("https://feedback.uc.cn")
                     and not link.startswith("http://pc.duowan.com") and ".163.com" not in link]

    for link in all_links:
        parsed_url = urlparse(link)
        if parsed_url.path:
            file_path, ext_name = os.path.splitext(parsed_url.path)
            if ext_name in ('.mp4', '.avi', '.asf'
                            , '.mov', '.flv', '.pdf'
                            , '.mpg', '.mpeg', '.wmv'
                            , '.exe', '.rar', '.zip', '.apk'):
                print("skip file download: ", link)
                all_links.remove(link)
    return all_links


def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)


def crawl_web(seed):
    tocrawl = seed
    crawled = []
    while tocrawl:
        page_url = tocrawl.pop()
        print("starting crawling:", page_url)
        if page_url not in crawled:
            page_content = get_page(page_url)
            if page_content:
                all_links_onpage = get_all_links(page_content)
                if all_links_onpage:
                    union(tocrawl, all_links_onpage)
            crawled.append(page_url)
    return crawled


soup = BeautifulSoup(search_main_page(), "lxml")
all_results = soup.find_all("div", attrs={"class": ["result"]})
# print(all_results)
all_seeds = [item['href'] for result in all_results for item in result.find_all("a") if
             "href" in item.attrs and "data-click" in item.attrs]
print("主页面种子列表：", all_seeds)

crawling_seeds = all_seeds
crawl_web(crawling_seeds)
