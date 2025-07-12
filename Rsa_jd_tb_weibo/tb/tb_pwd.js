const NodeRSA = require('node-rsa');
const { Buffer } = require('buffer');

// 登录信息
const loginId = 'test_user@example.com';
const password = '123456789';
const keepLogin = false;

// RSA 公钥参数（从你提供的数据中获取）
const nHex = 'b5e9d2031eb1c31e39440bb63de4527c1c437fb2d453bc36f4ba8f317f5ca31a160ede372fe62beb7a239e1326f0e7824b21a04ce5f83dbbad5324ba657539ef0a721f3293f2e8e46543d503e7a1fc9e6ad4a4487feecef11b2bd0537dc02b23c0c349a169d7ad4469577795240a1e1f279d0ca2028074a371f4630cce31d1f0f133605ef26980b42dad7716ec4ea5253bbd8fe1e5d35573a00841b71a28c01d1aa3e04d665dcf10e1b1e6377a230e447e1e3f85e6b2ad51b83b049374a54a8e864ddf91ab93f05e7049573ca60892ef275ae378577a6d7ea48ae2c39b1487db9ec11ca3ae938ee2a69cada5905fa115b2e86e262e553d234b092f21dcf048db';
const eHex = '10001'; // 通常是 65537

function hexToBuffer(hex) {
    return Buffer.from(hex, 'hex');
}

function createPublicKey(nHex, eHex) {
    const modulus = hexToBuffer(nHex);
    const exponent = hexToBuffer(eHex);

    // 创建一个新的 RSA 实例
    const key = new NodeRSA();
    // 使用组件方式导入公钥
    key.importKey({
        n: modulus,
        e: exponent
    }, 'components-public');

    return key;
}

function rsaEncrypt(password, key) {
    return key.encrypt(password, 'base64'); // 返回Base64编码的加密结果
}

function loginProcess() {
    try {
        const publicKey = createPublicKey(nHex, eHex);
        const encryptedPassword = rsaEncrypt(password, publicKey);

        const loginData = {
            loginId: loginId,
            password2: encryptedPassword,
            keepLogin: keepLogin
        };

        console.log('加密后的登录数据:', loginData);
    } catch (err) {
        console.error("错误:", err.message);
    }
}

loginProcess();