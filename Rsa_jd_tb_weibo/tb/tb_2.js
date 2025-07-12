

function get_environment(proxy_array) {
    proxy_array.forEach(name => {
        try {
            // 尝试获取全局对象中的属性
            let target = globalThis[name];
            if (!target) throw new Error();

            // 创建 handler 对象
            const handler = {
                get(target, property, receiver) {
                    console.log("方法:", "get  ", "对象:", name, "  属性:", property, "  属性类型:", typeof property, "  属性值类型:", typeof target[property]);
                    return Reflect.get(target, property, receiver);
                },
                set(target, property, value, receiver) {
                    console.log("方法:", "set  ", "对象:", name, "  属性:", property, "  属性类型:", typeof property, "  属性值类型:", typeof target[property]);
                    return Reflect.set(target, property, value, receiver);
                }
            };

            // 应用 Proxy
            globalThis[name] = new Proxy(target, handler);
        } catch (e) {
            // 如果对象不存在，则初始化为一个新的被代理的空对象
            const handler = {
                get(target, property, receiver) {
                    console.log("方法:", "get  ", "对象:", name, "  属性:", property, "  属性类型:", typeof property, "  属性值类型:", typeof target[property]);
                    return Reflect.get(target, property, receiver);
                },
                set(target, property, value, receiver) {
                    console.log("方法:", "set  ", "对象:", name, "  属性:", property, "  属性类型:", typeof property, "  属性值类型:", typeof target[property]);
                    return Reflect.set(target, property, value, receiver);
                }
            };
            globalThis[name] = new Proxy({}, handler);
        }
    });
}

const proxy_array = ['window', 'document', 'location', 'navigator', 'history', 'screen', 'aaa', 'target'];
get_environment(proxy_array);


require('./tb_231算法_补环境.js')

e = {
    "noProxy": true,
    "MaxMTLog": 20,
    "MaxNGPLog": 10,
    "MaxKSLog": 5,
    "MaxFocusLog": 3,
    "location": "cn",
    "loadTime": 17,
    "timeout": 2000,
    "reqUrl": "/havanaone/loginLegacy/password/login.do?bizEntrance=taobao_pc&bizName=taobao"
}

aaa = window.fffff(0, e)
console.log(aaa)