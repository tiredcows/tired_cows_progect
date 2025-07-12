const NodeRSA = require('node-rsa');

// 公钥（与你前端提供的公钥一致）
const PUBLIC_KEY = `-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDC7kw8r6tq43pwApYvkJ5lalja
N9BZb21TAIfT/vexbobzH7Q8SUdP5uDPXEBKzOjx2L28y7Xs1d9v3tdPfKI2LR7P
AzWBmDMn8riHrDDNpUpJnlAGUqJG9ooPn8j7YNpcxCa1iybOlc2kEhmJn5uwoanQ
q+CA6agNkqly2H4j6wIDAQAB
-----END PUBLIC KEY-----`;

// 要加密的内容
const plainText = '123456789';

// 创建 RSA 实例并设置公钥
const encryptor = new NodeRSA(PUBLIC_KEY, 'pkcs8-public', {
    encryptionScheme: 'pkcs1_oaep' // 与 JSEncrypt 默认填充方式一致
});

// 设置加密选项为兼容 JSEncrypt
encryptor.setOptions({
    encryptionScheme: 'pkcs1_oaep'
});

// 加密函数
function getEntryptPwd(password) {
    if (!password) return password;

    const encrypted = encryptor.encrypt(password, 'base64');
    return encrypted;
}

// 执行加密
const encryptedPassword = getEntryptPwd(plainText);
console.log('加密后的密码:', encryptedPassword);