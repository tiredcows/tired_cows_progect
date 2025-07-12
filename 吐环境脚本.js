// 方法一
function setProxy(proxyObjs) {
    for (let i = 0; i < proxyObjs.length; i++) {
        const handler = `{
          get: function(target, property, receiver) {
          if (property!="Math" && property!="isNaN"){
             if (target[property] && typeof target[property] !="string" &&  Object.keys(target[property]).length>3){
              }else{
            console.log("方法:", "get  ", "对象:", "${proxyObjs[i]}", "  属性:", property, "  属性类型：", typeof property, ", 属性值：", target[property]);}}
            return target[property];
          },
          set: function(target, property, value, receiver) {
            console.log("方法:", "set  ", "对象:", "${proxyObjs[i]}", "  属性:", property, "  属性类型：", typeof property, ", 属性值：", value, ", 属性值类型：", typeof target[property]);
            return Reflect.set(...arguments);
          }
        }`;
        eval(`try {
            ${proxyObjs[i]};
            ${proxyObjs[i]} = new Proxy(${proxyObjs[i]}, ${handler});
        } catch (e) {
            ${proxyObjs[i]} = {};
            ${proxyObjs[i]} = new Proxy(${proxyObjs[i]}, ${handler});
        }`);
    }
}

// 方法二

window = new function monitorWindow() {
    // 设置打印字符串长度
    const MAX_VALUE_LENGTH = 70;
    /**
     截取 value 值，用于在日志中输出时限制字符串长度，避免日志过长。
     @param {Object} value - 需要被截取的值。
     @returns {Object} 返回截取后的字符串值。
     */
    function truncateValue(value) {
        if (typeof value === "string" && value.length > MAX_VALUE_LENGTH) {
            return value.substring(0, MAX_VALUE_LENGTH) + "...";
        }

        if (typeof value !== "object") {
            return value;
        }

        const keys = Object.keys(value);
        const result = {};

        if (keys.length > 2) {
            result[keys[0]] = value[keys[0]].toString().substring(0,MAX_VALUE_LENGTH) + "...";
        }

        return "{" + Object.entries(result).map(([k, v]) => `${k}: ${v}`).join(", ") + "}";
    }

    /**
     序列化 value 值，用于在日志中输出时处理对象或方法。
     @param {Object} value - 需要被序列化的值。
     @returns {Object} 返回序列化后的字符串值。
     */
    function serializeValue(value) {
        if (typeof value === "object") {
            try {
                return JSON.stringify(value);
            } catch {
                return value;
            }
        }
        return value;
    }

    /**
     * 创建代理处理程序，用于对被代理对象的属性访问、属性设置、方法调用等进行监听并打印操作日志。
     * @param {Object} name - 对象名。
     * @returns {Object} 返回代理处理程序。
     */
    function createHandler(name) {

        function shouldSkipKey(key, name) {

            if (key === 'window' || key === 'self' || key === 'global' ||key === 'globalThis' || key === name || key === "_globalObject") {
                return true;
            }

            if (typeof key === 'string' && (key.startsWith('__') || key.endsWith('__'))) {
                return true;
            }

            return String(key) === "Symbol(impl)" || String(key) === "Element" || String(key) === "prototype" || truncateValue(serializeValue(name)).includes("Symbol(impl)");


        }
        return {
            get(target, key, receiver) {
                // 打印调用栈
                // console.log(new Error().stack);
                // target=Object.defineProperty(target)
                // 获取属性值

                const value = target[key];

                // 不打印toString和valueOf特定的信息
                if (key === Symbol.unscopables || key === 'toString' || key === 'valueOf') {
                    return Reflect.get(target, key, receiver);
                }

                // 内部属性
                if (shouldSkipKey(key, name)) {
                    console.log(`访问: "${(String(key) + "\"内部属性").padEnd(28, " ")}|"${(truncateValue(serializeValue(name)) + "\"对象").padEnd(50, " ")}|值=`,truncateValue(serializeValue(value)));
                    return value;
                }

                // 处理代理函数的构造函数
                if (typeof value === 'function' && value.hasOwnProperty('prototype')) {
                    try{
                        new value
                        // console.log(`调用了构造函数: ${String(key).padEnd(22, " ")} |"参数": ${JSON.stringify(value)}`);
                        return new Proxy(value,createHandler(`${String(name)}.${String(key)}`))
                    }catch (e) {
                    }
                }

                // 处理代理对象的属性访问和设置()
                if (typeof value === 'function' && !value.hasOwnProperty('prototype')) {
                    return function getFunc(...args) {
                        try{
                            var result = Reflect.apply(value, target, args);
                            console.log(`调用了函数: ${(String(key)).padEnd(27, " ")}|"${(truncateValue(serializeValue(name)) + "\"对象").padEnd(50, " ")}|参数= ${truncateValue(serializeValue(args))}`);
                            return result
                        } catch (e){
                            // return  Reflect.apply(value, target, args[1])
                        }
                    }
                }

                // 处理代理对象的属性访问和设置(递归调用)
                if (value != null && (typeof value === 'object')) {
                    console.log(`访问: "${(String(key) + "\"属性").padEnd(30, " ")}|"${(truncateValue(serializeValue(name)) + "\"对象").padEnd(50, " ")}|值=`, truncateValue(serializeValue(value)));
                    return new Proxy(value,createHandler(`${String(name)}.${String(key)}`));
                }

                if (typeof value === 'function'){
                    // 在Node上和windows有些差异,node有函数也有prototype,所以需要继续回调
                    return new Proxy(value,createHandler(`${String(name)}.${String(key)}`));
                }else{
                    // 不进行代理的属性或方法
                    console.log(`获取: "${(String(key) + "\"属性").padEnd(30, " ")}|"${(truncateValue(serializeValue(name)) + "\"对象").padEnd(50, " ")}|值=`, truncateValue(serializeValue(value)));
                }
                return value;
            },
            set(target, key, value, receiver) {
                // 打印调用栈
                // console.log(new Error().stack);
                console.log(`设置对象: "${(String(key) + "\"").padEnd(28, " ")}|"${(truncateValue(serializeValue(name)) + "\"对象").padEnd(50, " ")}|值=`, truncateValue(serializeValue(value)));
                return Reflect.set(target, key, value, receiver);
            },
            apply(target, thisArg, args) {
                // 打印调用栈
                // console.log(new Error().stack);
                console.log(`调用了函数: ${(String(name)).padEnd(27, " ")}|"${(truncateValue(serializeValue(name)) + "\"对象").padEnd(50, " ")}|参数= ${truncateValue(serializeValue(args))}`);
                return Reflect.apply(target, thisArg, args);
            },
            construct(target, args, newTarget) {
                // 打印调用栈
                // console.log(new Error().stack);
                console.log(`调用了构造函数: ${String(target.name).padEnd(23, " ")}|"${(truncateValue(serializeValue(name)) + "\"对象").padEnd(50, " ")}|参数= ${JSON.stringify(args)}`);
                return Reflect.construct(target, args, newTarget);
            },
        };
    }
    return new Proxy(window,createHandler('window'));
}

// 方法三
//function setProxy(proxyObjs) {
//     for (let i = 0; i < proxyObjs.length; i++) {
//         const handler = `{
//           get: function(target, property, receiver) {
//           if (property!="Math" && property!="isNaN"){
//              if (target[property] && typeof target[property] !="string" &&  Object.keys(target[property]).length>3){
//               }else{
//             console.log("方法:", "get  ", "对象:", "${proxyObjs[i]}", "  属性:", property, "  属性类型：", typeof property, ", 属性值：", target[property]);}}
//             return target[property];
//           },
//           set: function(target, property, value, receiver) {
//             console.log("方法:", "set  ", "对象:", "${proxyObjs[i]}", "  属性:", property, "  属性类型：", typeof property, ", 属性值：", value, ", 属性值类型：", typeof target[property]);
//             return Reflect.set(...arguments);
//           }
//         }`;
//         eval(`try {
//             ${proxyObjs[i]};
//             ${proxyObjs[i]} = new Proxy(${proxyObjs[i]}, ${handler});
//         } catch (e) {
//             ${proxyObjs[i]} = {};
//             ${proxyObjs[i]} = new Proxy(${proxyObjs[i]}, ${handler});
//         }`);
//     }
// }
// setProxy(['window', 'document', ' navigator', 'screen', 'localStorage', 'location'])


//方法四
//memory.proxy = function proxy(object){
//     return new Proxy(object, {
//         get(obj, prop, receiver){
//             // if(prop=='self'){
//             //     debugger;
//             // }
//             // debugger;
//             objName = obj.name == undefined ? obj : obj.name;
//             // console.table([{"方法": "get", "对象": objName, "属性/方法": prop, "获取到的值": obj[prop]}]);
//             console.log({"方法": "get", "对象": objName, "属性/方法": prop, "获取到的值": obj[prop]});
//             return obj[prop];
//         },
//         set(obj, prop, value){
//             // debugger;
//             objName = obj.name == undefined ? obj : obj.name;
//             console.table([{"方法": "set", "对象": objName, "属性/方法": prop, "赋值前的值": obj[prop], "赋值后的值": value}]);
//             // console.log({"方法": "set", "对象": objName, "属性/方法": prop, "赋值前的值": obj[prop], "赋值后的值": value});
//             return Reflect.set(...arguments);
//         }
//     });
// };



// 最强封装大法
// function get_environment(proxy_array) {
//     proxy_array.forEach(function (variableName) {
//         try {
//             // 尝试获取全局对象上的属性
//             let target = this[variableName];
//
//             if (target === undefined) throw new Error('Target not found');
//
//             const handler = {
//                 get: function(target, property, receiver) {
//                     console.log("方法:", "get  ", "对象:", variableName,
//                                 "  属性:", property,
//                                 "  属性类型:", typeof property,
//                                 "  属性值类型:", typeof target[property]);
//                     return Reflect.get(target, property, receiver);
//                 },
//                 set: function(target, property, value, receiver) {
//                     console.log("方法:", "set  ", "对象:", variableName,
//                                 "  属性:", property,
//                                 "  属性类型:", typeof property,
//                                 "  属性值类型:", typeof target[property]);
//                     return Reflect.set(target, property, value, receiver);
//                 }
//             };
//
//             // 创建代理对象
//             this[variableName] = new Proxy(target, handler);
//         } catch (e) {
//             console.error(`无法为 ${variableName} 创建代理: `, e.message);
//             // 如果目标不存在，则初始化为空对象并创建代理
//             this[variableName] = new Proxy({}, handler);
//         }
//     }, window); // 使用 window 作为 this 上下文，以便于访问全局对象
// }
//
// const proxy_array = ['window', 'document', 'location', 'navigator', 'history', 'screen', 'aaa', 'target'];
// get_environment(proxy_array);