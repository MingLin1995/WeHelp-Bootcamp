//副程式

/* let x = 3;
let y = 4;
let data = x * y;

//基本載入模組
console.log(data);

//載入模組輸出的資料
export { x, y };

//載入模組"預設"輸出的資料
export default data;

//混合使用
export { data as default, x, y }; */

//載入自己建立的函式庫模組
const calculate = {
  add: function (n1, n2) {
    return n1 + n2;
  },
  multiply: function (n1, n2) {
    return n1 * n2;
  },
};
export default calculate;
