


function UUID() {
    let chars = '0123456789abcdefghijklmnopqrstuvwxyz';
    let uuid = '';
    for (let i = 0; i < 36; i++) {
        if ([8, 13, 18, 23].includes(i)) {
            uuid += '-'; // 插入分隔符
        } else if (i === 14) {
            uuid += '4'; // 设置版本号为4
        } else if (i === 19) {
            // 随机选择'8', '9', 'a', 或'b'
            uuid += chars[Math.floor(Math.random() * 4 + 8)];
        } else {
            uuid += chars[Math.floor(Math.random() * 16)];
        }
    }
    return uuid;
}

_0xb071cc = parseInt(Date.now() / 1000);

x_sign_nonce = UUID()
x_sign_version = "1.0"
x_sign_timestamp = _0xb071cc


_0x2486c0 = {
    "words": [
        774984018,
        -799212943,
        819120469,
        1167925004,
        1527218185
    ],
    "sigBytes": 20
}

function wordsToHex(words) {
    let hex = '';
    for (let i = 0; i < words.length; i++) {
        let val = words[i];
        // 转为无符号 32 位整数
        val = (val >>> 0).toString(16);
        // 补足 8 位
        while (val.length < 8) val = '0' + val;
        hex += val;
    }
    return hex;
}

const hex = wordsToHex(_0x2486c0.words);
// 调用某个对象的 toString 方法，得到签名值
let sign = hex.toString();
// 将该签名值赋给 params 对象中的 sign 字段
uuid = '490db468d82af9f873fb9ace8b1480db'


console.log(sign);
console.log(x_sign_timestamp);
console.log(x_sign_version);
console.log(x_sign_nonce);
console.log(uuid);
