const NodeRSA = require('node-rsa');

// 模拟 cp() 和 ap()
function cp() {
    return 'mock_cp_value'; // 替换为真实值
}

function ap() {
    return 'mock_ap_value'; // 替换为真实值
}

// 拼接明文
const plainText = [cp(), ap()].join('\t') + '\n' + '123456789';

// 公钥（确保完整且格式正确）
const publicKey = `-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDrKjhWhmGIf6GAvdtcq9XyHHv9
WcCQyy0kWoesJTBiiCcpKT5VBjUFCOf5qju3f0MzIxSQ+RX21jxV/i8IpJs1P0RK
05k8rMAtt4Sru45CqbG7//s4vhjXjoeg5Bubj3OpKO4MzuH2c5iEuXd+T+noihu+
SVknrEp5mzGB1kQkQwIDAQAB
-----END PUBLIC KEY-----`;

// 创建 RSA 实例
const encryptor = new NodeRSA(publicKey, 'pkcs8-public', {
    encryptionScheme: 'pkcs1_oaep'
});

// 加密函数
function Qh(text, key) {
    if (!text || !key) return null;

    encryptor.importKey(key, 'pkcs8-public');
    const encryptedBuffer = encryptor.encrypt(text, 'buffer');
    return encryptedBuffer.toString('base64');
}

// 执行加密
const password = Qh(plainText, publicKey);
console.log('加密后的密码:', password);


