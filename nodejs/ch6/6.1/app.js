const express = require("express");
const path = require("path");

const app = express();
app.set("port", process.env.PORT || 3000);
// app.set(키, 값) 을 통해 데이터를 저장할 수 있다.

app.get("/", (req, res) => {
  //res.send("Hello, Express");
  res.sendFile(path.join(__dirname, "/index.html"));
});

app.listen(app.get("port"), () => {
  console.log(app.get("port"), "번 포트에서 대기중");
});
