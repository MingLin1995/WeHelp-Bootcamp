// let x=666;
// //export default 資料;
// export default x; //輸出


function echo(msg){
    console.log(msg);
}
let name="檔案是獨立的，所以用一樣的變數會不會發錯誤";
/*
export default echo;
*/


//若要輸出兩個函式
function add(n1,n2){
    console.log(n1+n2);
}

export default { //用一個物件，包裝兩個函式
    echo1:echo,
    add1:add

};


