import "./index.css";
/* console.log("test"); */

import React from "react";
import ReactDOM from "react-dom";

//傳統寫法
//let app = React.createElement("div", {}, "Hello React");
//JSX
let app = <div>Hello React by JSX</div>;
ReactDOM.render(app, document.getElementById("root")); //到index.html id選擇器

//直接執行會失敗，所以要利用Babel編譯器翻譯JSX語法

/* -------------------可以開始寫主要內容----------------------- */
import List from "./list.js";
class App extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div>
        <h3>React Project DEMO</h3>
        <List />
      </div>
    );
  }
}
ReactDOM.render(<App />, document.getElementById("root"));
