/*
//預設的輸入 (因為是預設，所以變數可以跟輸出的不一樣)
//import abc from "./lib2.js" ;
console.log(abc);

//非預設的輸入(變數名稱一定要有對應到)
//import {obj} from "./lib2.js";
console.log(obj);

//一次輸入
import abc, {data,obj} from "./lib2.js";
console.log(data);
*/

//實際運用
import {multiply} from "./lib2.js"
multiply(3,4);
multiply(-9,2);

import math from "./lib2.js"
math.add1(5,6);
math.multiply2(4,4);

