console.log(this);
console.log(this === module.exports);
console.log(this === exports);

function whatIsThis() {
  console.log("function", this === exports, this === global);
}
whatIsThis();

// 최상위 스코프에 존재하는 this == exports, function안에 선언하는 this == global
