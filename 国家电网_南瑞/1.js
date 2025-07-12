function get_enviroment(proxy_array) {
  for (var i = 0; i < proxy_array.length; i++) {
    handler = '{\n' +
      '    get: function(target, property, receiver) {\n' +
      '        console.log("方法:", "get  ", "对象:", ' +
      '"' + proxy_array[i] + '" ,' +
      '"  属性:", property, ' +
      '"  属性类型:", ' + 'typeof property, ' +
      // '"  属性值:", ' + 'target[property], ' +
      '"  属性值类型:", typeof target[property]);\n' +
      '        return target[property];\n' +
      '    },\n' +
      '    set: function(target, property, value, receiver) {\n' +
      '        console.log("方法:", "set  ", "对象:", ' +
      '"' + proxy_array[i] + '" ,' +
      '"  属性:", property, ' +
      '"  属性类型:", ' + 'typeof property, ' +
      // '"  属性值:", ' + 'target[property], ' +
      '"  属性值类型:", typeof target[property]);\n' +
      '        return Reflect.set(...arguments);\n' +
      '    }\n' +
      '}'
    eval('try{\n' + proxy_array[i] + ';\n'
         + proxy_array[i] + '=new Proxy(' + proxy_array[i] + ', ' + handler + ')}catch (e) {\n' + proxy_array[i] + '={};\n'
         + proxy_array[i] + '=new Proxy(' + proxy_array[i] + ', ' + handler + ')}')
  }
}

proxy_array = ['window', 'document', 'location', 'navigator', 'history', 'screen']

// ------------- 补环境开始  ------------
let is_logging = true

_log = console.log

function v_log() {
  if (is_logging) {
    _log(...arguments)
  }
}

// 去掉 Interval
!(function () {
  setInterval_ = setInterval;
  v_log("原函数已被重命名为setInterval_")
  setInterval = function (v1, v2) {
    v_log("--setInterval--", ...arguments)
    v1()
  }
  setInterval.toString = function () {
    v_log("有函数正在检测setInterval是否被hook");
    return setInterval_.toString();
  };
})();
// 去掉 Timeout
!(function () {
  setTimeout_ = setTimeout;
  v_log("原函数已被重命名为setTimeout_")
  setTimeout = function (v1, v2) {
    v_log("--setTimeout--", ...arguments)
    v1()
  }
  setTimeout.toString = function () {
    v_log("有函数正在检测setInterval是否被hook");
    return setTimeout.toString();
  };
})();

// Window = function Window(){};
// window = new Window();
// for(let name in global){
//     switch(name){
//         case "window":
//             continue;
//         case "global":
//             continue;
//     }
//     window[name] = global[name];
//     delete global[name];
// }
// Object.setPrototypeOf(global,window); // 设置原型链给global 设置window


window = global;

var _null = function () {
  v_log("--arguments--", ...arguments)
};

window.outerHeight = 1080
window.outerWidth = 1920
window.Math = Math;
window.Date = Date;
window.parseInt = parseInt;
window.addEventListener = _null
window.attachEvent = _null
window.top = window


Navigator = function Navigator() {
}
Navigator.prototype = {
      userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
      webdriver: false,
      languages: ['en-GB', 'zh-CN', 'zh'],
    appCodeName: "Mozilla",
    appName: "Netscape",
    appVersion: "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    language: "zh-CN",
}
window.navigator = {};
window.navigator.__proto__ = Navigator.prototype


Location = function () {
}
Location.prototype ={
    "ancestorOrigins": {},
    "href": "https://zhaopin.sgcc.com.cn/sgcchr/static/unitPart.html?bullet_id=24ea423d661c43ff82edaadca1df5fcf&particulars=true",
    "origin": "https://zhaopin.sgcc.com.cn",
    "protocol": "https:",
    "host": "zhaopin.sgcc.com.cn",
    "hostname": "zhaopin.sgcc.com.cn",
    "port": "",
    "pathname": "/sgcchr/static/unitPart.html",
    "search": "?bullet_id=24ea423d661c43ff82edaadca1df5fcf&particulars=true",
    "hash": ""
}
window.location = new Location;

History = function History() {
}
History.prototype.back = function back() {
}
window.history = new History

Screen = function () {
}
Screen.prototype = {
    availWidth: 1920,
    availHeight: 1080,
    availLeft: 0,
    availTop: 0,
    height: 960,
    width: 1707
}
window.screen = new Screen


div = {
    getElementsByTagName: function getElementsByTagName(args) {
        console.log('div 的 getElementsByTagName 接收的参数为', args)
        if (args === 'i'){
            return wacth({length: 0}, "i")
        }
    }
}
script = {
    length: 2,
    0: {
        type: "text/javascript",
        getAttribute: function (args) {
            _log("script >>> getAttribute", arguments)
            if (args === 'r'){
                return "m"
            }
        },
        parentElement: {
            removeChild: _null
        }

    },
    1: {
        type: "text/javascript",
        getAttribute: function (args) {
            _log("script >>> getAttribute", arguments)
            if (args === 'r'){
                return "m"
            }
        },
        parentElement: {
            removeChild: _null
        }

    },
}
meta = {
    length: 2,
    0: {
        "getAttribute":function (args){
            console.log("meta >>> getAttribute >>> args:", args)
            if (args === "r"){
                return 'm'
            }
        },
        "parentNode":{
            "removeChild": _null
        },
    },
    1: {
        "getAttribute":function (args){
            console.log("meta >>> getAttribute >>> args:", args)
            if (args === "r"){
                return 'm'
            }
        },
        "parentNode":{
            "removeChild": _null
        },
        "content": "yzJSiwfpHUAP8xdhjBBTgFUwRveouH0YgbQwRrMGqZWHWgcPeYYrkFo6EWzcrOKh"
        // "content": "$content$"

    },
}


Document = function Document() {
}
Document.prototype = {
    createElement: function createElement(args){
        _log("document >>> createElement", arguments)
        if (args === 'div'){
            return div
        }
        if (args === 'a'){
            return wacth({}, "aaa")
        }
        if (args === 'form'){
            return '[object HTMLFormElement]'
        }
        if (args == 'input'){
            return '[object HTMLFormElement]'

        }
    },
    getElementsByTagName: function createElement(args) {
        _log("document >>> getElementsByTagName", arguments)
        if (args === 'script'){
            return wacth(script, "script")
        }
        if (args === 'meta'){
            return wacth(meta, "meta")
        }
        if (args === 'base'){
            return wacth({length: 0}, "base")
        }

    },
    getElementById: function createElement(args) {
        _log("document >>> getElementById", arguments)

    },
    attachEvent: _null
}
window.document = new Document;


window.localStorage = function () {
};
Storage = function () {
};
Storage.prototype.getItem = function getItem(key) {
};
Storage.prototype.setItem = function setItem(key, value) {
};


var XMLHttpRequest = function () {
    console.log("--XMLHttpRequest--", ...arguments)
}
window.open = function () {
    console.log("--window.open--", ...arguments)
}
let xhr_proto = {
    open: function (v1, v2, v3) {
        return void 0
    },
    send: function () {
        return void 0
    }
}
Object.setPrototypeOf(XMLHttpRequest, xhr_proto)
XMLHttpRequest.prototype = xhr_proto
window.XMLHttpRequest = XMLHttpRequest


get_enviroment(proxy_array)


