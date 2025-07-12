# -*- coding: utf-8 -*-
import requests
from lxml import etree
from pathlib import Path
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs


requests = requests.Session()
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
}
url = "http://www.sgcc.com.cn/html/sgcc_main/gb/xwzx/yw/index.shtml"

def get_cookie():
    response = requests.get(url, headers=headers)
    print(f'第一次请求：{response.status_code}, 获取cookies')
    html_data = etree.HTML(response.text)
    ts_code = html_data.xpath('//script[1]/text()')[0]
    meta_content = html_data.xpath('//meta[2]/@content')[0]
    script_url = 'http://www.sgcc.com.cn' + html_data.xpath('//script[2]//@src')[0]
    script_response = requests.get(script_url, headers=headers).text

    # 获取当前脚本的完整路径
    current_script_path = Path(__file__).resolve()
    current_script_dir = current_script_path.parent
    ts_path = current_script_dir / '_ts.js'
    script_path = current_script_dir / '_wl.js'
    js_path = current_script_dir / 'rs.js'

    with open(ts_path, 'w', encoding='utf-8') as f:
        f.write(ts_code)
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(script_response)


    with open(js_path, encoding='utf-8') as f:
        js_code = f.read()
    # print(meta_content)
    js = execjs.compile(js_code.replace('$content$', meta_content))
    js_cookie = js.call('get_cookie')
    cookies = {
        js_cookie.split('=')[0]: js_cookie.split('=')[1].split(';')[0]
    }
    return cookies


def get_second(cookies):
    response = requests.get(url, headers=headers, cookies=cookies)
    print(f'第二次请求：{response.status_code}')
    print(response.text)


def main():
    cookies = get_cookie()
    print(cookies)
    get_second(cookies)




if __name__ == '__main__':
    main()
