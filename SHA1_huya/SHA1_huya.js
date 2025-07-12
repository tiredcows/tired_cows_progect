// const SHA1 = {
//     hexEncode: function(e) {
//         return this.toHex(this.core(this.toArray(e)))
//     },
//     toArray: function(e) {
//         for (var t = (e.length + 8 >> 6) + 1, o = new Array(16 * t), a = 0; 16 * t > a; a++)
//             o[a] = 0;
//         for (a = 0; a < e.length; a++)
//             o[a >> 2] |= e.charCodeAt(a) << 24 - 8 * (3 & a);
//         return o[a >> 2] |= 128 << 24 - 8 * (3 & a),
//         o[16 * t - 1] = 8 * e.length,
//         o
//     },
//     toHex: function(e) {
//         for (var t = "0123456789abcdef", o = "", a = 0; a < 4 * e.length; a++)
//             o += t.charAt(e[a >> 2] >> 8 * (3 - a % 4) + 4 & 15) + t.charAt(e[a >> 2] >> 8 * (3 - a % 4) & 15);
//         return o
//     },
//     core: function(e) {
//         for (var t = e, o = new Array(80), a = 1732584193, n = -271733879, s = -1732584194, i = 271733878, r = -1009589776, c = 0; c < t.length; c += 16) {
//             for (var d = a, l = n, p = s, u = i, h = r, m = 0; 80 > m; m++) {
//                 o[m] = 16 > m ? t[c + m] : this.rol(o[m - 3] ^ o[m - 8] ^ o[m - 14] ^ o[m - 16], 1);
//                 var g = this.add(this.add(this.rol(a, 5), this.ft(m, n, s, i)), this.add(this.add(r, o[m]), this.kt(m)));
//                 r = i,
//                 i = s,
//                 s = this.rol(n, 30),
//                 n = a,
//                 a = g
//             }
//             a = this.add(a, d),
//             n = this.add(n, l),
//             s = this.add(s, p),
//             i = this.add(i, u),
//             r = this.add(r, h)
//         }
//         return new Array(a,n,s,i,r)
//     },
//     add: function(e, t) {
//         var o = (65535 & e) + (65535 & t)
//           , a = (e >> 16) + (t >> 16) + (o >> 16);
//         return a << 16 | 65535 & o
//     },
//     rol: function(e, t) {
//         return e << t | e >>> 32 - t
//     },
//     ft: function(e, t, o, a) {
//         return 20 > e ? t & o | ~t & a : 40 > e ? t ^ o ^ a : 60 > e ? t & o | t & a | o & a : t ^ o ^ a
//     },
//     kt: function(e) {
//         return 20 > e ? 1518500249 : 40 > e ? 1859775393 : 60 > e ? -1894007588 : -899497514
//     }
// };
//
//
// var g = '123456789';
// var password = SHA1.hexEncode(g);
//
// console.log('SHA-1 加密结果:', password);
// // 输出: 2c1d0d2a4c08e5f3b9c5a6d4e7f0b8a765432109




const CryptoJS = require("crypto-js");

var g = '123456789';
var password = CryptoJS.SHA1(g).toString(CryptoJS.enc.Hex);

console.log('SHA-1 加密结果:', password);




pwd = CryptoJS.MD5(g).toString()
console.log(pwd)

