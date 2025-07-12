import requests
import re
import tqdm

headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "origin": "https://www.yfsp.tv",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.yfsp.tv/play/XIvOD16QqWE",
    "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}
url = "https://s6-e1.oneclickcdn.vip/ppot/_definst_/mp4:s15/ivod/dhp-hjhzblrd7j-01-02FC9926A.mp4/chunklist.m3u8"
params = {
    "vendtime": "1746064570",
    "vhash": "26Dyo7Dqqepy10uzNtnggnpMH6NNm8BB-mHwGScdj0Y=",
    "vCustomParameter": "0_18.100.102.125_ES_0_0",
    "lb": "8aa26f8f36b9cd3689e75fbca0bb5820",
    "proxy": "SpOjPJ4kRsvbOsnfOsjZP6ukTcbmV7CsBMKnBdHePMDiQMDhOsHkBdPfS7npDYrbCIvbONDvSsLqTN1tONakOsyslZcR5hAObpenDZIwlBONCRUslZcR5hAObpiuERcojZOokHSnjxD"
}
response = requests.get(url, headers=headers, params=params)

data = ['https://' + i for i in re.findall('https://(.*?)\n#EX', response.text)]
for uurl in tqdm.tqdm(data):
    m3u8 = requests.get(url=uurl, headers=headers)
    with open('../../zhuaqu_all_url/cecshi/MP4/111.mp4', mode='ab') as f:  # 这个地方的111.mp4 写的文件名（提前新建一个MP4文件）
        f.write(m3u8.content)

