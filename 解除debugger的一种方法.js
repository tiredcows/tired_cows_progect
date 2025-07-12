// 打开F12点击Console
//
// 输入(function(){}).constructor === Function，回车；
//
// 如果返回的是true，继续输入Function.prototype.constructor = function(){},并回车；
//
// 切换回sources选项卡,点击继续执行，无限debugger的问题就解决了
//
// 注意：如果第二步返回的是false,则此方法不可用。


// 2：
setInterval(()=>{debugger;}, 100);
setInterval(()=>{eval("debugg"+"er");}, 100);

// 3
//配合编程猫专用工具进行hook
(function() {
'use strict'
//过瑞数 debuger
var eval_ = window.eval;
window.eval_ = function(x){
	eval_(x.replace("debugger;", "   ;  "));
	}
//过瑞数debuger检测
window.eval.toString = eval_.toString;
})();

// 　3
Function.prototype.__constructor_back = Function.prototype.constructor;
Function.prototype.constructor = function() {
    if(arguments && typeof arguments[0]==='string'){
        if("debugger" === arguments[0]){
            return
        }
    }
   return Function.prototype.__constructor_back.apply(this,arguments);
}


// 　4
let _constructor = constructor;
Function.prototype.constructor = function(s) {
    if (s == "debugger") {
        console.log(s);
        return null;
    }
    return _constructor(s);
};


// 5
let originalSetInterval = setInterval;

setInterval = function(callback, delay) {
  if (callback.toString().indexOf('debugger') === -1) {
    return null;
  }
  return originalSetInterval(callback, delay);
};

// 下面的定时器会被设置，因为函数体中有debugger语句
setInterval(function() {
  console.log('Hello, world!');
  debugger;
}, 1000);

// 下面的定时器不会被设置，因为函数体中没有debugger语句
let timerId = setInterval(function() {
  console.log('This will not be executed');
}, 1000);
if (timerId === null) {
  console.log('Timer was not set because the callback does not contain debugger statement.');
}
