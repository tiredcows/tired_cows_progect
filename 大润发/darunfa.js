const crypto = require('crypto');
var CryptoJS = require('crypto-js')
const base64 = require('base64-js');

function get_log_params(data) {
    // JSON 对象
    // var data = {
    //     addrId: '',
    //     apiVersion: 'a1.68',
    //     appVersion: '2.0.2',
    //     body: {
    //         cid: 'f1ae55cdba3e8e3a5dcb8829c301a9f8',
    //         client: '1',
    //         deviceType: 'Google Pixel 4',
    //         isNewStore: 0,
    //         password: 'Axu28MpzF3GgaPeqYN7S13VCFVmWH5yjjJwemHSxGIU=',
    //         phoneType: '0',
    //         picCaptcha: 'p7rq',
    //         storeCode: '2701',
    //         username: '/6W/tFjPb+Xsa4hqtKzdiRzGRspxF6py5nX0fM5tAOA='
    //     },
    //     businessId: '27010001',
    //     channel: 'WanDouJia',
    //     deliveryCircleType: '2',
    //     deviceId: 'ecfd56c4ed50bbb4-56c4-ecfd-bbb4-ed50',
    //     dockCode: '270120001',
    //     httpsEnable: 1,
    //     isSimulator: false,
    //     networkType: 'WIFI',
    //     osType: 1,
    //     reRule: '3',
    //     scopeType: 1,
    //     source: 'yx',
    //     time: '20250721170802',
    //     token: '0c5dda3f9cfd2f0bc859d49976f9b358',
    //     viewSize: '1080x2236'
    // };
    // // 额外参数
    // var additionalParams = ['false', '1080x2236', 'WIFI', '20250721170802'];
    var additionalParams = ['false', data['viewSize'], data['networkType'], data['time']]
    // 密钥（直接作为字符串，不解码）
    var keyString = 'cXZaSXFaUUIxeWprYnRZbCtDc1FlS0Qz';

    // 序列化 JSON 和拼接
    var jsonString = JSON.stringify(data);
    var inputString = jsonString + additionalParams.join('');

    // 计算 HMAC
    var messageBuffer = Buffer.from(inputString, 'utf8');
    var keyBuffer = Buffer.from(keyString, 'utf8');
    var hmac = crypto.createHmac('sha256', keyBuffer)
        .update(messageBuffer)
        .digest();
    var hmacBase64 = base64.fromByteArray(hmac);
    return hmacBase64
}

// console.log(get_log_params());

// 模拟 Java 的 KeyGenerator 和 SecureRandom 生成密钥和 IV
function generateKeyAndIV() {
    // 模拟 Java 的 KeyGenerator (SHA-256 哈希生成密钥)
    const secret = "KWbIWtoIoHbivcyJSOp2KOmTqwJLRqbt"; // 与 Java 代码相同的密钥种子
    const key = crypto.createHash('sha256').update(secret).digest();
    // 模拟 Java 的 SecureRandom 生成 IV (16字节)
    const iv = crypto.randomBytes(16);

    // const keyHex = 'd2f44b44b7e3316165309e0e7a910f50726c8ac367780103a7067a9551592dbb';
    // const ivHex = '7bd7ccad1b48e16def037d72119f21b8';
    // // 转换密钥和IV为Buffer
    // const key = Buffer.from(keyHex, 'hex');
    // const iv = Buffer.from(ivHex, 'hex');

    return {key, iv};
}

// 账号密码
function encryptAesCbc(plainText) {
    const {key, iv} = generateKeyAndIV();

    const cipher = crypto.createCipheriv('aes-256-cbc', key, iv);
    cipher.setAutoPadding(true); // 启用 PKCS7 填充

    let encrypted = cipher.update(plainText, 'utf8', 'base64');
    encrypted += cipher.final('base64');

    // 返回 IV + 密文（Base64 编码）
    const ivAndCiphertext = Buffer.concat([iv, Buffer.from(encrypted, 'base64')]);
    return ivAndCiphertext.toString('base64');
}


e = "KWbIWtoIoHbivcyJSOp2KOmTqwJLRqbt"
r = "9AxZV8sVMnrbf7Kl";

function aesCBC(s, c = e, p = r) {
    const n = CryptoJS.enc.Utf8.parse(c)
        , o = CryptoJS.enc.Utf8.parse(p)
        , y = CryptoJS.enc.Utf8.parse(s)
        , i = CryptoJS.AES.encrypt(s, c, {
        iv: p
    }).toString()
        , a = CryptoJS.AES.encrypt(y, n, {
        iv: o
    }).ciphertext.toString().toUpperCase()
        , j = CryptoJS.enc.Hex.parse(a);
    return {
        aes: i,
        hex: a,
        base64: CryptoJS.enc.Base64.stringify(j)
    }
}

function randomString(t = 36) {
    const e = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789"
        , r = e.length;
    let n = "";
    for (let o = 0; o < t; o++)
        n += e.charAt(Math.floor(Math.random() * r));
    return n
}

function aesCBCEncryptToBase64(e) {
    API_AES_KEY = "KWbIWtoIoHbivcyJSOp2KOmTqwJLRqbt"
    const n = CryptoJS.SHA256(API_AES_KEY)
        , c = CryptoJS.enc.Utf8.parse(randomString(16))
        , s = CryptoJS.AES.encrypt(e, n, {
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7,
        iv: c
    })
        , i = s.iv.clone().concat(s.ciphertext);
    return CryptoJS.enc.Base64.stringify(i)
}

function get_body(username, password, verify) {
    cardNum = aesCBC(username).base64
    cardPassword = aesCBC(password).base64
    userPassWord = aesCBCEncryptToBase64(verify)
    return {
        "cardNum": cardNum,
        "cardPassword": cardPassword,
        "userPassWord": userPassWord,
        "storeId": "2701"
    }
}

function get_params(data) {
    const t = JSON.stringify(data) + data.isSimulator + data.viewSize + data.networkType + data.time
    o = "@653yx#*^&HrTy99"
    paramsMD5 = CryptoJS.enc.Base64.stringify(CryptoJS.HmacSHA256(t, o))
    return paramsMD5
}
