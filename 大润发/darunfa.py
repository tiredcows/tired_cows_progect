import base64

import requests
import json
import execjs
import time
import secrets
import sys
import random

# ----------------------------
# 加载 JS 加密文件
# ----------------------------
try:
    with open('darunfa.js', encoding='utf-8') as f:
        js_code = f.read()
    js = execjs.compile(js_code)
except Exception as e:
    print(f"[ERROR] Failed to load drf.js: {e}")
    sys.exit(1)


# ----------------------------
# 设备指纹随机化字段（仅这些变，其他不动！）
# ----------------------------
def gen_device_id():
    # return f"{secrets.token_hex(8)}-{secrets.token_hex(4)}-{secrets.token_hex(4)}-{secrets.token_hex(4)}-{secrets.token_hex(12)}"
    return 'ecfd56c4ed50bbb4-56c4-ecfd-bbb4-ed50'


def gen_resolution():
    return random.choice(["1080x2236", "1080x2340", "720x1280", "1440x2960"])


def gen_device_type():
    return random.choice(
        ["Xiaomi 13", "Huawei Mate 50", "Samsung Galaxy S23", "OPPO Find X6", "vivo X90", "Google Pixel 4"])


def gen_channel():
    return random.choice(["WanDouJia", "BaiDu", "XiaoMi", "HuaWei", "AnZhi"])


def gen_user_agent():
    ver = random.choice(["12", "13"])
    model = random.choice(["Xiaomi 13", "Huawei Mate 50"]).split()[0]
    build = f"TP1A.{random.randint(100000, 999999)}.{random.randint(1, 100):03d}"
    return f"Dalvik/2.1.0 (Linux; U; Android {ver}; {model} Build/{build})"


# ----------------------------
# 固定不变的 data1 基础结构（除了指纹字段！）
# ----------------------------
BASE_DATA1 = {
    "addrId": "",
    "apiVersion": "a1.68",
    "appVersion": "2.0.2",
    "businessId": "27010001",
    "channel": "",  # ← 由 gen_channel() 填充
    "deliveryCircleType": "2",
    "deviceId": "",  # ← 由 gen_device_id() 填充
    "dockCode": "270120001",
    "httpsEnable": 1,
    "isSimulator": False,
    "networkType": "WIFI",
    "osType": 1,
    "reRule": "3",
    "scopeType": 1,
    "source": "yx",
    "time": "",  # ← 由当前时间填充
    "token": "",  # ← 由 login 返回或传入
    "viewSize": "",  # ← 由 gen_resolution() 填充
    "deviceType": "",  # ← 由 gen_device_type() 填充
}


# ----------------------------
# 请求头（App 风格）
# ----------------------------
def get_headers():
    return {
        'Host': 'membase-yxapp.feiniu.com',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': gen_user_agent(),
    }


# ----------------------------
# 接口函数
# ----------------------------

def get_yzm(headers, data1, phone):
    data1["body"] = {
        "mode": 20,
        "phone": js.call('encryptAesCbc', phone)
    }
    data1["token"] = secrets.token_hex(16)  # 临时

    data = {
        'data': json.dumps(data1, ensure_ascii=False, separators=(',', ':')),
        'paramsMD5': js.call("get_log_params", data1),
    }
    res = requests.post(
        'https://membase-yxapp.feiniu.com/verificationCode/getPhoneCode/a168',
        headers=headers,
        data=data,
        timeout=10
    )
    print(res.text)
    return res


def login_yzm(headers, data1, phone, captcha):
    data1["body"] = {
        "cid": "f1ae55cdba3e8e3a5dcb8829c301a9f8",
        "client": "1",
        "deviceType": data1["deviceType"],
        "isNewStore": 0,
        "password": "",
        "phoneLoginCaptcha": captcha,
        "phoneType": "0",
        "storeCode": "2701",
        "username": js.call('encryptAesCbc', phone)
    }
    data1["token"] = secrets.token_hex(16)  # 临时

    data = {
        'data': json.dumps(data1, ensure_ascii=False, separators=(',', ':')),
        'paramsMD5': js.call("get_log_params", data1),
    }
    res = requests.post(
        'https://membase-yxapp.feiniu.com/loginController/loginPhone/a168',
        headers=headers,
        data=data,
        timeout=10
    )
    print(res.text)

    # 提取真实 token
    try:
        j = res.json()
        if j.get("success"):
            return j["body"]["token"]
        else:
            print(f"Login failed: {j.get('errorDesc')}")
            return None
    except:
        print("Parse login response failed.")
        return None


def login_v2_captcha(headers, data1, phone, captcha):
    headers['Host'] = 'membase-yxapp.feiniu.com'
    data1["token"] = secrets.token_hex(16)  # 临时

    password = '147258a'
    data1['body'] = {
        "captchaInfo": {
            "captcha": "505039",
            "captchaType": 3
        },
        "cid": "f1ae55cdba3e8e3a5dcb8829c301a9f8",
        "client": "1",
        "deviceType": "vivo X90",
        "isNewStore": 0,
        "password": js.call('encryptAesCbc', password),
        "phoneType": "0",
        "storeCode": "2701",
        "username": js.call('encryptAesCbc', phone),
    }
    data = {
        'data': json.dumps(data1, ensure_ascii=False, separators=(',', ':')),
        'paramsMD5': js.call("get_log_params", data1),
    }
    response = requests.post('https://membase-yxapp.feiniu.com/loginController/loginPd/a168', headers=headers,
                             data=data)
    print(response.text)


def login(headers, data1, username, password='147258a'):
    headers = {
        'Host': 'membase-yxapp.feiniu.com',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'okhttp/4.9.3',
    }
    data1["token"] = secrets.token_hex(16)  # 临时

    data1['body'] = {
        "cid": "f1ae55cdba3e8e3a5dcb8829c301a9f8",
        "client": "1",
        "deviceType": data1["deviceType"],
        "isNewStore": 0,
        "password": js.call('encryptAesCbc', password),
        "phoneType": "0",
        "storeCode": "2701",
        "username": js.call('encryptAesCbc', username),
    }
    data = {
        'data': json.dumps(data1, ensure_ascii=False, separators=(',', ':')),
        'paramsMD5': js.call("get_log_params", data1),
    }

    response = requests.post('https://membase-yxapp.feiniu.com/loginController/loginPd/a168', headers=headers,
                             data=data)
    print(response.text)
    if '为了您的帐号安全，请输入验证码验证您的身份' in response.text:
        get_yzm(headers, data1, username)
    elif '您的登录过于频繁，需要输入手机验证码验证您的身份' in response.text:
        get_yzm(headers, data1, username)
    return response


def reset(headers, data1, phone, password, captcha):
    headers['Host'] = 'member-yxapp.feiniu.com'
    data1["token"] = secrets.token_hex(16)  # 临时

    data1["body"] = {
        "captcha": captcha,
        "password": str(base64.b64encode(password.encode('utf-8')), 'utf-8'),
        "phone": str(base64.b64encode(phone.encode('utf-8')), 'utf-8'),
    }

    data = {
        'data': json.dumps(data1, ensure_ascii=False, separators=(',', ':')),
        'paramsMD5': js.call("get_log_params", data1),
    }

    response = requests.post('https://member-yxapp.feiniu.com/password/resetLoginPassword/a168', headers=headers,
                             data=data)
    print(response.text)


def login_v2(headers, data1, phone, captcha):
    password = '147258a'
    reset(headers, data1, phone, password, captcha)
    time.sleep(1)
    login(headers, data1, phone, password)


def get_yzm_v2(headers, data1, phone):
    headers['Host'] = 'membase-yxapp.feiniu.com'
    data1["token"] = secrets.token_hex(16)  # 临时

    data1["body"] = {
        "mode": 13,
        "phone": js.call('encryptAesCbc', phone)
    }

    data = {
        'data': json.dumps(data1, ensure_ascii=False, separators=(',', ':')),
        'paramsMD5': js.call("get_log_params", data1),
    }
    response = requests.post('https://membase-yxapp.feiniu.com/verificationCode/getPhoneCode/a168', headers=headers,
                             data=data)
    print(response.text)
    return response


def band(card_name, card_pwd, pay_password, token):
    body = js.call("get_body", card_name, card_pwd, pay_password)
    headers = {
    }

    data1 = {
        "isLoading": True,
        "version": "2.1.0",
        "apiVersion": "t172",
        "appVersion": "2.1.0",
        "areaCode": "CS000016",
        "channel": "online",
        "clientid": "a7ea53059fc868e2e3e2dd7c04027035",
        "device_id": "udid-HO57lbzaiCGF",
        "time": int(time.time() * 1000),
        "reRule": "4",
        "token": token,
        "source": "yx",
        "viewSize": "720x1184",
        "networkType": "wifi",
        "isSimulator": "false",
        "osType": "4",
        "body": body,
        "scopeType": 1,
        "businessType": 2,
        "businessId": "27010001",
        "deliveryCircleType": "2",
        "dockCode": "270120001"
    }
    paramsMD5 = js.call("get_params", data1)
    data = {
        'data': json.dumps(data1, ensure_ascii=False, separators=(',', ':')),
        'paramsMD5': paramsMD5,
    }

    response = requests.post('https://member-yxapp.feiniu.com/shoppingCard/newBindingCard/t172', headers=headers,
                             data=data)
    print(response.text)
    return response


def check_denomination(headers, data1, token):
    headers['Host'] = 'member-yxapp.feiniu.com'
    data1['token'] = token
    data1['body'] = {
        "index": 1,
        "size": 10
    }
    data = {
        'data': json.dumps(data1, ensure_ascii=False, separators=(',', ':')),
        'paramsMD5': js.call("get_log_params", data1),
    }

    response = requests.post('https://member-yxapp.feiniu.com/shoppingCard/bindingUseCardRecord/a168', headers=headers,
                             data=data)
    print(response.text)
    return response


def main(*args):
    # 模拟指纹
    headers = get_headers()
    data1 = BASE_DATA1.copy()
    data1["channel"] = gen_channel()
    data1["deviceId"] = gen_device_id()
    data1["viewSize"] = gen_resolution()
    data1["deviceType"] = gen_device_type()
    data1["time"] = str(int(time.time() * 1000))

    name = args[0]
    if name == 'get_yzm_v2':
        phone = args[1]
        get_yzm_v2(headers, data1, phone)
    elif name == 'login_v2':
        phone = args[1]
        captcha = args[2]
        login_v2(headers, data1, phone, captcha)
    elif name == 'login_v2_captcha':
        phone = args[1]
        captcha = args[2]
        login_v2_captcha(headers, data1, phone, captcha)
    elif name == 'get_yzm':
        phone = args[1]
        get_yzm(headers, data1, phone)
    elif name == 'login_yzm':
        phone = args[1]
        captcha = args[2]
        login_yzm(headers, data1, phone, captcha)
    elif name == 'login':
        phone = args[1]
        login(headers, data1, phone)
    elif name == 'band':
        token = args[1]
        card_name = args[2]
        card_pwd = args[3]
        pay_password = args[4]
        band(card_name, card_pwd, pay_password, token)
    elif name == 'check_denomination':
        token = args[1]
        check_denomination(headers, data1, token)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("用法: python script.py <功能名>")
        print("例如: python script.py get_yzm_v2")
        sys.exit(1)

    main(*sys.argv[1:])
    # token = '2042e5508ac0fdde2aadb130916f608d'
    # card_name = '145236445125448'
    # card_pwd = '123456'
    # pay_password = '147258q'
    # # main("band", token, card_name, card_pwd, pay_password)
    # main("check_denomination", token)
