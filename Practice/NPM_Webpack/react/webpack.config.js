const path = require("path");
module.exports = {
  //入口
  entry: "./src/index.js", //主要的程式檔案

  //輸出
  output: {
    filename: "main.js", //輸出的檔名
    path: path.resolve(__dirname, "dist"), //輸出的資料夾
  },
  //模組載入規則
  module: {
    rules: [
      //CSS樣式表載入規則
      {
        test: /\.css$/i, //檔名為.css結尾，i代表不計較大小寫(正則表示式)
        use: ["style-loader", "css-loader"], //符合以上規則，就套用這兩個載入器
      },
      {
        test: /\.m?js$/, //針對JS檔案
        exclude: /node_modules/, //排除第三方資料夾
        use: {
          loader: "babel-loader",
          options: {
            presets: ["@babel/preset-env"],
          },
        },
      },
    ],
  },
};
