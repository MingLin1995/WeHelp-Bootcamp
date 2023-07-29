/* ------------------#12 了解原型鍊 Prototype Chain-----------------*/
//車子物件→Car(車子的原型物件)→Object(Car的原型物件)→null(Object的原型物件) 原型鍊的終點
//原型物件：每個物件都有對應的原型物件
//取得原型物件：Object.getPrototypeOf(物件)

//定義類別
class Car {
  //定義建構式
  constructor(color) {
    this.color = color;
  }
  //定義方法
  run() {}
}
//產生類別物件
let car = new Car("green");
//取得並將原型物件顯示出來
let carProto = Object.getPrototypeOf(car); //Car 原型物件
console.log(carProto);
let objProto = Object.getPrototypeOf(carProto); //Object原型物件
console.log(objProto);
let lastOne = Object.getPrototypeOf(objProto); //原型鍊的終點：null
console.log(lastOne);

//繼承關係中的原型鍊
//電動車物件→ElectricCar(電動車的原型物件)→Car(車子的原型物件)→Object(Car的原型物件)→null(Object的原型物件) 原型鍊的終點

//可以直接在物件實體上，建立屬性或方法
//建立新的屬性，物件.屬性名稱=新的資料 (更新資料)
car.name = "彭彭的車";
//car物件.方法名稱 直接在car物件上，定義新的方法，接上函式
car.test = function () {
  console.log("建立物件後，在物件實體上新增方法");
  console.log(this.name); // 印出：彭彭的車
};
car.test(); //呼叫test方法

/* ------------------#13 定義、呼叫靜態方法 Static-----------------*/
//靜態方法：與類別綁定的方法　（之前介紹的方法或是屬性都是與物件綁定）
/* 
定義靜態方法
static 方法的名稱(參數列表){
    內部的程式碼
}

呼叫靜態方法
類別名稱.方法名稱(參數資料)
*/
//定義類別
class Car {
  //定義建構式
  constructor(color) {
    this.color = color;
  }
  //定義方法
  run() {
    console.log("Car" + this.color + "Running");
  }
  //定義靜態方法
  static showColors() {
    console.log("我們提供三種顏色，藍色、紅色、綠色");
  }
}

let carObj = new Car("blue"); //產生新物件實體
carObj.run(); //使用物件實體，呼叫物件的方法 run();
carObj.showColors(); //會產生錯誤，showColors為靜態方法，必須由類別名稱呼叫

Car.showColors(); //直接使用類別名稱，呼叫靜態方法
Car.run(); //會產生錯誤，因為run非靜態方法，必須由物件實體呼叫

/* ------------------#14 什麼是非同步程式-----------------*/
//時間排程是一個"非同步的程式"
//主程式設定排程後，交由"背景子程式"負責監控時間

//此為回呼函式
window.setTimeout(function () {
  //兩秒後，"背景子程式"喚醒"主程式"，執行此函式
  alert("兩秒後執行");
}, 2000);
//主程式設定排程後，立刻往下執行
alert("立刻被呼叫");
//主程式結束，暫時沒事做

//Ajax預設是一個"非同步的程式"
let req = new XMLHttpRequest();
req.open("get", "data.txt");
req.onload = function () {
  //連線完成後，"背景子程式"觸發"主程式"的load事件處理函式
  alert(this.responseText); //取得伺服器回應
};
//主程式送出連線後，交由"背景子程式"負責處理連線細節
req.send();
//主程式送出連線，立刻往下執行
alert("立刻被呼叫");
//主程式結束暫時沒事做

/* ------------------#14 使用回呼函式處理非同步程式-----------------*/
function getData(callback) {
  // 2.準備做Ajax連線
  let req = new XMLHttpRequest();
  req.open("get", "data.txt");
  req.onload = function () {
    // 5.等待一段時間後，"子程式"完成連線，觸發"主程式"的load事件，取得資料
    // 6.呼叫callback，即透過參數傳入的showData函式
    callback(this.responseText);
  };
  req.send(); // 3.送出連線，建立"子程式"進行非同步處裡
  // 4."主程式"立刻結束函式，回傳undefined
}

//回呼函式呼叫回來
function showData(result) {
  alert(result); // 7.可以從result，取得連線後得到的資料
}

getData(showData); // 1.呼叫取資料用的函式，並將showData函式透過參數傳入
alert(getData); //因為子程式還沒連線完成，所以會出現undefined，所以要用回呼函式處理
/* ------------------#15 使用 Promise 處理非同步程式-----------------*/
//使用Promise物件串接非同步流程
function getData() {
  //new Promise(執行函式(成功程序, 失敗程序));
  return new Promise(function (resolve, reject) {
    let req = new XMLHttpRequest();
    req.open("get", "url.txt");

    //連線成功
    req.onload = function () {
      //如何將連線後得到的資料this.responseText，串接到主流程上
      resolve(this.responseText);
    };

    //連線失敗
    req.onerror = function () {
      reject("Error");
    };

    req.send();
  });
}
//這是主流程，嘗試從網路取得資料，回傳Promise物件，並接續工作
let dataPromise = getData(); //嘗試從網路取得資料，回傳Promise物件

//使用then方法接續工作
/* 
then(
    函式(){成功時的動作}
    函式(){失敗時的動作}
) 
*/
dataPromise.then(
  function (result) {
    //這裡可以從參數result，取得正確連線後的資料
    console.log(result);
  },
  function (error) {
    //這裡可以從參數error，取得失敗報告
    console.log(error);
  }
);
