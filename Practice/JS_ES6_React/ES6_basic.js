/* 
var 宣告時，可以先不指定資料var x;
function區域變數；for全域變數，可以重複宣告變數。

const 宣告時，需同時指定資料const y=1;
比起let更嚴謹，通常用在不可更動的數值，例如圓周率

let 宣告時，可以先不指定資料
function區域變數；for區域變數，不行重複宣告變數 。
*/

/* ------------------#3 箭頭函式 Arrow Function-----------------*/
//傳統JS用function建立函式，但現在可以用箭頭函式

/* //傳統
let add = function (n1, n2) {
  return n1 + n2;
};

//箭頭函式 
//1.(參數列表)=>(回傳值)
let add = (n1, n2) >= n1 + n2;

//2.(參數列表)>={函式內部程式}
let add=(n1, n2) >={
    return n1+n2;
} */

/* ------------------#4 參數的預設值 Default Parameter-----------------*/
//傳統
function show(message) {
  if (typeof message === "undefined") {
    message = "預設值";
  }
  alert(message);
}
show("hello"); //顯示 hello
show(); //顯示 預設值

//ES6 若未給定message資料，則直接採用=後方指定的資料
function show(message = "預設值") {
  alert(message);
}
show("hello"); //顯示 hello
show(); //顯示 預設值

//箭頭函式
let show = (message = "預設值") => {
  alert(message);
};
show("hello"); //顯示 hello
show(); //顯示 預設值

/* －－－範例一：乘法的預設值－－－ */
//傳統
function multiply(n1, n2 = 1) {
  return n1 * n2;
}
multiply(3, 4); //回傳12
multiply(5); //回傳5

//箭頭函式
let multiply = (n1, n2 = 1) => n1 * n2;
multiply(3, 4); //回傳12
multiply(5); //回傳5

/* －－－範例二：預設值可使用前面的參數名稱－－－ */
function combine(first = "預設名", last = "預設姓", name = first + " " + last) {
  alert(name);
}
combine("Ming", "Lin"); //顯示 Ming Lin
combine("Ming"); //顯示 Ming 預設姓
combine(); //顯示 預設名 預設姓

/* ------------------#5 類別與物件的基本觀念-----------------*/
//類別→設計圖→關鍵字：class、constructor
//物件→根據設計圖產生的物件→關鍵字：new
/* ------------------#6 定義類別並產生物件-----------------*/
//定義類別 class 類別名稱{}
class Car {}
//利用定義好的類別，產生新物件；建立物件 new 類別名稱()
// new Car()產生新物件，並放進變數 car1 中
let car1 = new Car();
// new Car()產生新物件，並放進變數 car2 中
let car2 = new Car();
/* ------------------#7 定義建構式 Constructor-----------------*/
//定義類別→建構式(建立新物件時，會被呼叫的函式)→物件
//constructor(參數列表){建構式的內部程式} 建構式也是一種函式

//定義一個類別
class Car {
  //在類別中，定義建構式（若沒有特別寫建構式，內建就是空白的建構式 ex：#6）
  constructor() {
    console.log("建構式被呼叫了");
  }
}
//利用已經定義好的類別，產生新物件
let car1 = new Car(); //new Car() 呼叫建構式，產生新物件
let car2 = new Car(); //new Car() 呼叫建構式，產生新物件
/* ------------------#8 定義、存取屬性 Attribute-----------------*/
//屬性：用來描述物件的"個別差異"
/* 
    constructor(參數列表) {
    this.屬性名稱=初始資料;
    } 
*/

//定義一個類別
class Car {
  constructor() {
    this.color = "red"; //建立新屬性color，指定資料"red"
  }
}
//利用已經定義好的類別，產生新物件
let car1 = new Car(); //新物件擁有color屬性，資料為"red"
let car2 = new Car(); //新物件擁有color屬性，資料為"red"
/* --------- */
//定義一個類別
class Car {
  constructor(color) {
    this.color = color; //指定資料可以透過參數，彈性的，在建立物件時提供
  }
}
//利用已經定義好的類別，產生新物件
let car1 = new Car("blue"); //新物件擁有color屬性，資料為"blue"
let car2 = new Car("green"); //新物件擁有color屬性，資料為"green"

//存、取物件屬性
//物件.屬性名稱 (取得資料)
//物件.屬性名稱=新的資料 (更新資料)
let car1 = new Car("blue"); //新物件擁有color屬性，資料為"blue"
console.log(car1.color); //取得資料，印出"blue"
car1.color = "black"; //更新屬性資料
console.log(car1.color); //取得更新後的屬性資料，印出"black"

/* ------------------#9 定義、呼叫方法 Method-----------------*/
//方法：用來描述物件可以做的事 (與"物件"綁定的函式)
/* 
    方法的名稱(參數列表){
        內部的程式碼
    }
*/
//定義類別
class Car {
  //定義建構式
  constructor(color) {
    this.color = color;
  }
  //定義一個run方法，透過物件呼叫，並執行內部程式碼
  run() {
    //在物件方法中使用this代表"綁定物件" (這裡的this代表car1)
    console.log("Car" + this.color + "Running");
  }
}
//產生新物件，物件擁有 color屬性 與 run方法
let car1 = new Car("blue");
//呼叫物件方法 物件.方法名稱(資料參數)
car1.run(); //呼叫run方法，執行run內部的程式，印出"Car blue Running"

/* 綜合運用 */
class Car {
  constructor(color) {
    this.color = color;
    this.speed = 0; //車子的初始速度固定為0
  }
  run() {
    this.speed = speed; //更新車子的速度
    console.log("Car" + this.color + "Running at" + this.speed + "Km/Hr");
  }
  stop() {
    this.speed = 0; //更新車子的速度
    console.log("Car" + this.color + "Stopped");
  }
}

//產生新物件，物件擁有 color屬性 與 run,stop方法
let car1 = new Car("blue");
car1.run(50); //印出 "Car blue Running at 50 Km/Hr"
car1.stop(); // 印出 "Car blue Stopped"

/* ------------------#10 類別繼承的基本觀念-----------------*/
//類別繼承的關鍵字：extends,super
/* ------------------#11 定義子類別並操作子類別物件-----------------*/
//定義父類別
class Car {
  constructor() {
    console.log("執行父類別建構式，建立基本的Car物件");
    this.color = this.color; //父類別中加入color屬性
  }
  run() {
    //定義run方法在父類別中
    console.log("Car" + this.color + "is Running");
  }
}

//定義子類別：class 子類別名稱 extends 父類別名稱{}
class ElectricCar extends Car {
  //定義子類別建構式
  constructor(color) {
    //呼叫父類別建構式（一定要先呼叫）：super()
    super(color);
    //子類別建構式中的其他程式
    console.log("繼續執行子類別建構式，衍伸出ElectricCar物件");

    //衍伸更多子類別，電動車專屬的定義
    this.battery = 100;
  }

  //在子類別中定義run方法，覆蓋/取代父類別中的run方法
  run(distance) {
    this.battery -= distance; //扣掉電量跑的距離
    console.log("Car" + this.color + "Runs" + distance + "KM");
  }

  //加入子類別專屬定義的方法
  charge() {
    this.battery = 100; //充電後回復到100%
  }
}
//建立子類別物件：new 子類別名稱()
let car = new ElectricCar("green");
/* 
會先進子類別建構式→呼叫父類別→進入父類別建構式→繼續跑子類別其他程式
先印出："執行父類別建構式，建立基本的Car物件"
後印出："繼續執行子類別建構式，衍伸出ElectricCar物件"
*/

console.log("車子顏色：" + car.color); //子類別物件同樣擁有父類別中定義的"屬性"
car.run(); //子類別物件同樣擁有父類別中定義的"方法"，印出 "Car" + this.color + "is Running"

console.log("目前的電量：" + car.battery); //使用子類別中定義的"屬性"

car.run(10); //被覆蓋後，印出 "Car" + this.color + "Runs" + distance + "KM"
console.log("目前的電量：" + car.battery); //會變成100-10=90(跑十公里消耗10格電)

car.charge(); //使用子類別中定義的"方法"
console.log("目前的電量：" + car.battery); //會變成100(充滿電)
