const path = require("path");
module.exports = {
  //建置的模式
  mode: "development", //開發模式 //預設production 上線模式

  //入口
  entry: "./src/index.js", //主要的程式檔案

  //輸出
  output: {
    filename: "main.js", //輸出的檔名
    path: path.resolve(__dirname, "dist"), //輸出的資料夾
  },
  //DevServer 設定
  devServer: {
    static: "./dist", //伺服器根目錄，根資料夾在甚麼地方(因為最後使用webpack最後產生的檔案是在dist)
  },
  //模組載入規則
  module: {
    rules: [
      //CSS樣式表載入規則
      {
        test: /\.css$/i, //檔名為.css結尾，i代表不計較大小寫(正則表示式)
        use: ["style-loader", "css-loader"], //符合以上規則，就套用這兩個載入器
      },
      //SASS樣式表載入規則
      {
        test: /\.scss$/i, //檔名為.scss結尾，i代表不計較大小寫(正則表示式)
        use: ["style-loader", "css-loader", "sass-loader"], //符合以上規則，就套用這兩個載入器
      },
    ],
  },
};
