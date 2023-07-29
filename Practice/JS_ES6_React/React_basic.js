/* React和ReactDOM這兩個物件是，是React套件的核心物件 */
console.log("React", React);
console.log("ReactDOM", ReactDOM);

/* －－－－－－－－－－#18 快速入門範例－－－－－－－－－－ */
/* 使用React.createElement(型態、[屬性]、[子元件]) */
/* 使用ReactDOM.render(React_Element,容器) */

//頁面加載完成後執行JS
window.addEventListener("load", () => {
  //1.建立型態為H1的React Element，並且包含文字Hello World(文字也是一種子元件)
  //相當於<h1>Hello World</h1>
  let reactElement = React.createElement("h1", null, "hello world");
  //2.將建立好的React Element 渲染到容器中，這裡的容器使用HTML Body Element
  //ReactDOM.render(組件實體,容器元件)
  ReactDOM.render(reactElement, document.body);
});

/* －－－－－－－－－#20 我的第一個組件Component－－－－－－－－ */
/* 
定義一個組件類別
class 組件類別名稱 extends React.Component{
    組件類別內的程式碼

    //在組件類別中定義render方法
    render(){
        return React_element;
    }
}
*/

//設計組件類別
class MyHead extends React.Component {
  render() {
    return React.createElement("h2", null, "hello Component");
  }
}
window.addEventListener("load", () => {
  //1.建立自訂的React組件實體
  let myComponent = React.createElement(MyHead, null);
  //2.將建立好的React組件實體渲染到容器中
  ReactDOM.render(myComponent, document.body);
});

/* －－－－－－－－－#21 組件的屬性 Props－－－－－－－－ */
//組件屬性：初始設定，建立後不變動
//在組件方法中，使用this.props可以取得屬性物件

class MyHead2 extends React.Component {
  render() {
    //console.log(this.props.level);
    return React.createElement(
      "h" + this.props.level,
      null,
      "hello Component2"
    );
  }
}
window.addEventListener("load", () => {
  //給定屬性
  let myComponent = React.createElement(MyHead2, { level: 4 });
  ReactDOM.render(myComponent, document.body);
});
/* －－－－－－－－－#22 巢狀組件結構－－－－－－－－ */
//[子元件]可以是其他的組件實體
//React.createElement(型態、[屬性]、[子元件])
class MyHead4 extends React.Component {
  render() {
    return React.createElement(
      "h" + this.props.level,
      null,
      "hello Component3"
    );
  }
}
class MyHeadList extends React.Component {
  render() {
    //建立子元件
    let heads = [];
    let head;
    for (let i = 1; i < 6; i++) {
      //參考MyHead4程式，做出五個head
      head = React.createElement(MyHead4, { level: i });
      heads.push(head);
    }
    //建立一個div，子元件(heads)是一個陣列，畫到div內
    return React.createElement("DIV", null, heads);
  }
}
window.addEventListener("load", () => {
  //1.網頁載入後產生React組件(MyHeadList)
  let myComponent = React.createElement(MyHeadList, null);
  //2.利用render把MyHeadList畫到body上
  ReactDOM.render(myComponent, document.body);
});
/* －－－－－－－－－#23 組件的狀態 State－－－－－－－－ */
/* //組件類別的建構式
class 組件類別名稱 extends React.Component {
  constructor(props) {
    //一定要先呼叫父類別的建構式
    super(props);
    //初始化狀態為空白物件
    this.state = {};
  }
}

//使用setState(新的組件狀態)來更新狀態
this.setState({ data: "新的資料" }); //禁止直接更新 ex. this.state={data:"新的資料"}

//更新狀態(與目前的狀態有關聯性)→會自動呼叫render()渲染畫面
setState((目前狀態, 目前屬性) => 新的狀態); */

class MyHead5 extends React.Component {
  render() {
    return React.createElement(
      "h" + this.props.level,
      null,
      "hello Component5"
    );
  }
}
class MyHeadList5 extends React.Component {
  //組件類別的建構式
  constructor(props) {
    //一定要先呼叫父類別的建構式
    super(props);

    //初始化狀態(只要繪製到二號標題就好了)
    this.state = { maxLevel: 3 };

    //做一些小變化，兩秒鐘後自動調整狀態 setTimeout
    window.setTimeout(() => {
      //使用setState(新的組件狀態)來更新狀態→會自動呼叫render()渲染畫面
      //this.setState({ maxLevel: 6 });

      //更新狀態→setState((目前狀態, 目前屬性) => 新的狀態)→會自動呼叫render()渲染畫面
      this.setState((currentState, currentProps) => ({
        //當前狀態的maxLevel+1(代表有關連性)
        maxLevel: currentState.maxLevel + 1,
      }));
    }, 2000);
  }
  render() {
    let heads = [];
    let head;
    //透過 this.state.maxLevel動態調整最大數字
    for (let i = 1; i < this.state.maxLevel; i++) {
      head = React.createElement(MyHead5, { level: i });
      heads.push(head);
    }

    return React.createElement("DIV", null, heads);
  }
}
window.addEventListener("load", () => {
  let myComponent = React.createElement(MyHeadList5, null);
  ReactDOM.render(myComponent, document.body);
});

/* －－－－－－－－－#24 組件的生命週期 Lifecycle－－－－－－－－ */
/* 
都是定義在組件的父類別中，所以可以複寫，自訂邏輯
  建立組件：依照順序執行以下方法
  1. constructor(); 呼叫組件類別的建構式
  2. componentWillMount(); React正要把這個組件放到畫面上(放上去以前)
  3. render(); 主要繪製畫面邏輯寫進去放到畫面上(放上去)
  4. componentDidMount(); 確定組件已經掛載到畫面上(放上去以後) 
  更新組件：依照順序執行以下方法
  1. componentWillUpdate(); 更新前，將要更新
  2. render(); 更新、重新繪製
  3. componentDidUpdate(); 確定更新完成
  刪除組件：依照順序執行以下方法
  1. componentWillUnmount(); 
*/

class MyHead6 extends React.Component {
  render() {
    return React.createElement(
      "h" + this.props.level,
      null,
      "hello Component6"
    );
  }
}
class MyHeadList6 extends React.Component {
  constructor(props) {
    super(props);
    //給定動態屬性 props.start
    this.state = { maxLevel: props.start };
  }

  //複寫，建立自己的邏輯
  componentWillMount() {
    //每秒鐘執行的程式碼(setTimeout只會執行一次)
    this.intervalID = window.setInterval(() => {
      this.setState((currentState, currentProps) => {
        if (currentState.maxLevel > currentProps.end) {
          //大於六(給定動態屬性 currentProp.end )，不更新(回傳原始狀態)
          return currentState;
        } else {
          //小於六，每秒+1
          return { maxLevel: currentState.maxLevel + 1 };
        }
      });
    }, 1000);
  }

  //設定上面的排程的時候，順便設定一個排程ID，離開組件以前把排程刪除，避免資源浪費
  componentWillUnmount() {
    window.clearInterval(this.intervalID);
  }

  render() {
    let heads = [];
    let head;
    for (let i = 1; i < this.state.maxLevel; i++) {
      head = React.createElement(MyHead6, { level: i });
      heads.push(head);
    }
    return React.createElement("DIV", null, heads);
  }
}
window.addEventListener("load", () => {
  //MyHeadList的屬性物件{ start: 2, end: 5 }會傳遞到props
  let myComponent = React.createElement(MyHeadList6, { start: 3, end: 6 });
  ReactDOM.render(myComponent, document.body);
});
