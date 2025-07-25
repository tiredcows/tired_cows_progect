import requests
from lxml import etree
import json

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
}
url = "https://www.dianping.com/shop/Gajv7d7tSl1XxTyD"
params = {
    "": ""
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

html = etree.HTML(response.text)
pic_list = [i.replace('"', '') for i in html.xpath('//div[@class="picsWrap wx-view"]/div/div[@class="recommendWrap wx-view"]/@data-url')[5:8]]
num = 0
for pic in pic_list:
    num += 1
    with open(f'MP4/{num}.png', 'wb') as f:
        f.write(requests.get(pic, headers=headers, cookies=cookies, params=params).content)



headers1 = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Origin": "https://www.dianping.com",
    "Pragma": "no-cache",
    "Referer": "https://www.dianping.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "channel": "H5",
    "channelversion": "undefined",
    "minaname": "dianping-wxapp",
    "minaversion": "11.0.0",
    "mtgsig": "{\"a1\":\"1.2\",\"a2\":1745740306946,\"a3\":\"5xwx54z1u5u5582609328476zv6856y380324vu8x779795852x3216w\",\"a5\":\"iG6qpdVRwxQK+pr7AVxD67zcw52ss6RWO0K4bmr/LEV81cFWuUejwEVMD+QxUud/AW==\",\"a6\":\"h1.89IlK3qQNmaU1kbro6HK2F3Z+WcnHYXUwqMGmbeQl2Z3X1OGFbmAbxhZSDHSqUtPOHS61e+w2w9oyltP7JILbdPICGZtIOVdYewuO5O4tRyCFCleG8yVEsznUvwVoFY+YcHNVntehkIbHI/nvjryUPq50E2W5H9ntN5aU30B9CuOyR5TQIhPYTk32xD2P/jUWi+w24Et+QO4NvlHvs2+fcBL3wtAUZ/wdv1e8jaEwJ0HztA0RGdefEyQE9mFcewNULNu6DCGkW7GlAn0yDcWUFmKLdvRzfeVsxuK3NrFFqNjDh97qpQYvY95xw1sdrtYZITuOw60F1+3f0OmwhWl6ilMmx+gUKsgj1oWbvik+WG6DSgke4qJV6EzVOX11IEIPSmZFpLpBWUzQwhwvQKSBnw==\",\"a8\":\"37072168337338703961a17e93a60aef\",\"a9\":\"3.1.0,7,245\",\"a10\":\"e8\",\"x0\":4,\"d1\":\"7060110f6370dbcdec23cb071310caca\"}",
    "platform": "undefined",
    "platformversion": "undefined",
    "sdkversion": "undefined",
    "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "token": "null",
    "wechatversion": "undefined"
}
cookies = {
}
url = "https://m.dianping.com/ugc/review/shop/shopreview"
params = {
    "pageSize": "3",
    "mtsiReferrer": "https://www.dianping.com/shop/Gajv7d7tSl1XxTyD??shopUuid=Gajv7d7tSl1XxTyD&online=1&shopuuid=Gajv7d7tSl1XxTyD&shopId=Gajv7d7tSl1XxTyD&pageName=shop",
    "isNeedNewReview": "1",
    "shopUuid": "Gajv7d7tSl1XxTyD",
    "device_system": "",
    "yodaReady": "h5",
    "csecplatform": "4",
    "csecversion": "3.1.0"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)
data = json.loads(response.text)['shopReviewInfo']['reviewList']
for item in data:
    if item['userNickName'] == '勇义诚信的小爽':
        pic_url = item['reviewPics']
        for pic in pic_url:
            num += 1
            with open('MP4/' + str(num) + '.jpg', 'wb') as f:
                f.write(requests.get(pic['bigurl']).content)
print(response.text)
