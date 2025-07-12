import json
import requests
import execjs
import time
import ddddocr

def get_requestId():
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://login.dangdang.com",
        "Pragma": "no-cache",
        "Referer": "https://login.dangdang.com/?returnurl=https%3A%2F%2Fwww.dangdang.com%2F",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    url = "https://login.dangdang.com/api/customer/loginapi/getRankey"
    t = str(int(time.time()*1000))
    ct = 'pc'
    permanent_id = "20250522144918533319693213013812018"
    sign = execjs.compile(open("456789.js", "r").read()).call("main", ct, permanent_id, t)
    data = {
        "t": t,
        "ct": permanent_id,
        "permanent_id": permanent_id,
        "requestId": "",
        "sign": sign
    }
    response = requests.post(url, headers=headers, data=data)
    data = json.loads(response.text)
    requestId = data["requestId"]
    rankey = data["rankey"]
    return requestId, rankey


def isShowSlide(requestId):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://login.dangdang.com",
        "Pragma": "no-cache",
        "Referer": "https://login.dangdang.com/?returnurl=https%3A%2F%2Fwww.dangdang.com%2F",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    url = "https://login.dangdang.com/api/customer/loginapi/isShowSlide"
    t = str(int(time.time() * 1000))
    ct = 'pc'
    permanent_id = "20250522144918533319693213013812018"
    sign = execjs.compile(open("456789.js", "r").read()).call("main1", ct, permanent_id, t, requestId)
    data = {
        "t": t,
        "ct": ct,
        "permanent_id": permanent_id,
        "requestId": requestId,
        "sign": sign
    }
    response = requests.post(url, headers=headers, data=data)


def getSlidingVerifyCode(requestId, rankey):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://login.dangdang.com",
        "Pragma": "no-cache",
        "Referer": "https://login.dangdang.com/?returnurl=https%3A%2F%2Fwww.dangdang.com%2F",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    url = "https://login.dangdang.com/api/customer/loginapi/getSlidingVerifyCode"
    t = str(int(time.time() * 1000))
    ct = 'pc'
    permanent_id = "20250522144918533319693213013812018"
    sign = execjs.compile(open("456789.js", "r").read()).call("main1", ct, permanent_id, t, requestId, rankey)
    data = {
        "t": t,
        "ct": ct,
        "permanent_id": permanent_id,
        "requestId": requestId,
        'situation':'login',
        "sign": sign
    }
    response = requests.post(url, headers=headers, data=data)
    data1 = json.loads(response.text)['data']
    slideImg = requests.get(data1['slideImg'], headers=headers).content
    bgImg = requests.get(data1['bgImg'], headers=headers).content
    token = data1['token']
    y = data1['y']
    heightRatio = data1['heightRatio']
    encryptKey = data1['encryptKey']
    x = get_x(bgImg, slideImg)['target'][0] * 350 /408
    return  token, encryptKey, y, heightRatio, x


def get_x(bg, slide):
    det = ddddocr.DdddOcr(det=False, ocr=True, show_ad=False)
    x = det.slide_match(bg, slide, simple_target=False)
    return x

def main():
    requestId, rankey = get_requestId()
    token, encryptKey, y, heightRatio, x = getSlidingVerifyCode(requestId, rankey)
    point_json = execjs.compile(open("456789.js", "r").read()).call("get_point_json", x, y, encryptKey)

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://login.dangdang.com",
        "Pragma": "no-cache",
        "Referer": "https://login.dangdang.com/?returnurl=https%3A%2F%2Fwww.dangdang.com%2F",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    url = "https://login.dangdang.com/api/customer/loginapi/checkSlidingVerifyCode"
    t = str(int(time.time() * 1000))
    ct = 'pc'
    permanent_id = "20250522144918533319693213013812018"
    sign = execjs.compile(open("456789.js", "r").read()).call("main2", ct, permanent_id, t, requestId, point_json, token, encryptKey)
    data = {
        "t": t,
        "ct": ct,
        "permanent_id": permanent_id,
        "requestId": requestId,
        "situation": "login",
        "verifyToken": token,
        "slide_cost_time": "1088",
        "need_new_verifydata": "0",
        "point_json": point_json,
        "sign": sign
    }
    response = requests.post(url, headers=headers, data=data)



if __name__ == '__main__':
    main()


