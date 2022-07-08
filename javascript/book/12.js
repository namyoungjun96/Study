var add = function add(x, y) {
  return x + y;
};

console.log(add(2, 5));

// 익명 함수
var add = function (x, y) {
  return x + y;
};

console.log(add(2, 5));

// // 함수 참조
// console.dir(set);
// console.dir(sub);
// // 함수 호출
// console.log(set(2, 5));
// console.log(sub(2, 5));
// // 함수 선언문 ( 표현식은 선언 이전에 호출 할 수 있다. )
// function set(x, y) {
//   return x + y;
// }
// 함수 표현식 ( 표현식은 선언 이전에 호출 할 수 없다. ) 이쪽을 더 권장
// var sub = function (x, y) {
//   return x - y;
// };

res = (function () {
  var a = 3;
  var b = 5;
  console.log("실행 되는건가??");
  return a * b;
})();

console.log(res);
console.log(res);

// 순수 함수 ( 매개변수를 통해 값을 조작함. )
function increase(n) {
  return ++n;
}
// 비순수 함수 ( 매개변수가 아닌 직접 값을 조작하는 함수. 별로 안쓰는걸 권장 )
function increase() {
  return ++n;
}
