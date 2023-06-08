/*
//default 預設的輸出 
let x="Hello";
//export default x;

//非預設的輸出
let data=[5,6,7];
let obj={x:10,y:2};
//export {data,obj};

//一次輸出
export {x as default, data, obj};
*/

//實際運用
let add=function(n1,n2){
    console.log(n1+n2);
};
let multiply=function(n1,n2){
    console.log(n1*n2);
};
let math={
    add1:add,
    multiply2:multiply
}
export {add,multiply}; // 單獨使用
export default math;  //包裝使用
