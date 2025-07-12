import requests
from lxml import etree

keyword = input('请输入想要搜索的物品：')
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://m.1688.com/search.html",
    "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}
url = "https://m.1688.com/offer_search/-6D7033.html"
params = {
    "keywords": keyword
}
response = requests.get(url, headers=headers, params=params)
html = etree.HTML(response.text)

first_xpath = html.xpath('//div[@id="list-main"]/div')

for each_xpath in first_xpath:
    try:
        name = ''.join(each_xpath.xpath('.//div[@class="item-info_title"]//text()')).strip()
        pic = each_xpath.xpath('.//div[@class="item-image"]//img/@data-src')[0]  # 此处不用‘’.join主要就是去除那几条错误数据
        price = ''.join(each_xpath.xpath('.//div[@class="item-info_count"]/div[@class="count_price"]/text()')).strip()
        print([name, pic, price])
    except IndexError as e:
        continue
