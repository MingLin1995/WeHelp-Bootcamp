//主程式

/* //基本載入模組
import "./lib.js"; //會輸出副程式console.log(data)的結果 #12

//載入模組輸出的資料
import { x, y } from "./lib.js";
console.log(x, y); //會輸出3,4

//載入模組"預設"輸出的資料
import data from "./lib.js";
console.log(data); //會輸出12

//混合使用
import data, { x, y } from "./lib.js";
console.log(x, y, data); // 3 4 12 */

//載入自己建立的函式庫模組
import calculate from "./lib.js";
let result = calculate.add(3, 4);
console.log(result);
result = calculate.multiply(3, 4);
console.log(result);

/* -------------載入器 Loader---------- */
import "./style.css"; //因為非預設載入器，所以webpack無法辨識
/* 
1安裝套件 npm install style-loader css-loader --save-dev
2.到webpack.config.js設定
3.可以用開發人員工具觀察網頁，HTML沒有載入css檔案，是用動態載入
*/

import "./style.scss";
/* 安裝套件 npm install sass-loader node-sass --save-dev */

/* -------------透過JS動態產生HTML標籤------------- */
/* 
<div class="title">Webpack Loader</div>
    <ul>
      <li>CSS Loader</li>
      <li>SASS Loader</li>
      <li>Babel Loader</li>
    </ul> 
*/
//加入標題
import title from "./title.js";
/* let title = document.createElement("div");
title.className = "title";
title.textContent = "Webpack Loader"; */
document.body.appendChild(title);

//加入ul、li
import list from "./list.js";
/* let list = document.createElement("ul");
let item = document.createElement("li");
item.textContent = "CSS Loader";
list.appendChild(item);

item = document.createElement("li");
item.textContent = "SASS Loader";
list.appendChild(item);

item = document.createElement("li");
item.textContent = "Babel Loader";
list.appendChild(item); */

document.body.appendChild(list);
/* 將以上程式碼模組化，分別給不同人寫，拆開到不同的JS檔案(title.js、list.js) */
