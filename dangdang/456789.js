const querystring = require('querystring');
const Cryptojs = require('crypto-js')


function  Y(t, e) {
            e = Cryptojs.enc.Utf8.parse(e);
            var n = Cryptojs.enc.Utf8.parse(t);
            return Cryptojs.AES.encrypt(n, e, {
                iv: U
            }).toString()
        }


function main(ct, permanent_id, t) {
    U= {
        "words": [
            808529970,
            808661044,
            808792118,
            808923192
        ],
        "sigBytes": 16
    }
    const a = {
        ct: ct,
        permanent_id: permanent_id,
        t: t
    };
    r = decodeURIComponent(querystring.stringify(a))
    r = Cryptojs.MD5(r).toString()
    sign = Y(r, '')
    return sign
}
function main1(ct, permanent_id, t, reqId, r_key) {
    U= {
        "words": [
            808529970,
            808661044,
            808792118,
            808923192
        ],
        "sigBytes": 16
    }
    const a = {
        ct: ct,
        permanent_id: permanent_id,
        requestId: reqId,
        situation: "login",
        t: t
    };
    r = decodeURIComponent(querystring.stringify(a))
    r = Cryptojs.MD5(r).toString()
    console.log(r);
    sign = Y(r, r_key)
    return sign
}

console.log(main1('pc', "20250522144918533319693213013812018", 1747900137336,"2505221539363570vHcLnm_a1bb", "Qs0WX2kWbZnHwM26"));


function get_point_json(x, y, encryptKey) {
    point_json = Y(JSON.stringify({
                x: x / 350,
                y: y
            }), encryptKey)
    return point_json
}




function main2(ct, permanent_id, t, reqId, point_json, verifyToken, slide_cost_time, r_key, t_T) {
    U= {
        "words": [
            808529970,
            808661044,
            808792118,
            808923192
        ],
        "sigBytes": 16
    }
    const a = {
            "ct": ct,
            "need_new_verifydata": 0,
            "permanent_id": permanent_id,
            "point_json": point_json,
            "requestId": reqId,
            "situation": "login",
            "slide_cost_time": t_T,
            "t": t,
            "verifyToken": verifyToken
        };
    r = decodeURIComponent(querystring.stringify(b))
    r = Cryptojs.MD5(r).toString()
    console.log(r);
    sign = Y(r, r_key)
    return sign
}

// console.log(get_point_json(91, 0.37254903, "qx83Mdo7OaqGRJvI"));
console.log(main2());
