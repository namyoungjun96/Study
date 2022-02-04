// 9.4 단축 평가

// 9.1 [논리 연산자를 사용한 단축 평가]
var done = true;
var message = "";
// if문은 단축 평가로 대체 가능
if (done) message = "뭐지";
// done이 true라면 message에 '완료'를 할당
// done이 false라면 message에 false를 할당
message = done && "완료";
console.log(message);

var done = false;
var message = "";
if (!done) message = "뭐지";
// done이 false라면 mesasge에 '미완료'를 할당
// done이 true라면 message에 true를 할당
message = done || "미완료";
console.log(message);

// (함수 매개변수에 기본 값을 설정할 때)
function getStringLength(str) {
  // false라면 오른쪽을 str에 할당한다
  str = str || "";
  return str.length;
}

console.log(getStringLength());
console.log(getStringLength("hi"));

// ES6의 매개변수의 기본값 설정 > ??
function getStringLength(str = "") {
  return str.length;
}

console.log(getStringLength());
console.log(getStringLength("hi"));

// 9.2 [옵셔널 체이닝 연산자]

var elem = null;
var value = elem?.value;
console.log(value);

var elem = null;
// elem이 Falsy 값이면 elem으로 평가되고, elem이 Truthy 값이면 elem.value로 평가된다.
var value = elem && elem.value;
console.log(value);

var str = "";
// 문자열의 길이를 참조한다.
var length = str && str.length;
// 문자열의 길이를 참조 못한다. 왜냐면 str이 false기 때문에.
console.log(length);

str = "hi";
var length = str && str.length;
console.log(length);

var str = "";
// 문자열의 길이를 참조한다. 이때 좌항 피연산자가 false로 평가되는 Falsy 값이라도
// null 또는 undefined가 아니면 우항의 프로퍼티 참조를 이어간다.
var length = str?.length;
console.log(length);

// 9.3 [null 병합 연산자]
// 좌항의 피연산자가 null 또는 undefined이면 우항의 피연산자를 반환하고,
// 그렇지 않으면 좌항의 피연산자를 반환한다.
var foo = null ?? "default string";
console.log(foo);

// Falsy 값인 0이나 ''도 기본값으로써 유효하다면 예기치 않은 동작이 발생할 수 있다.
var foo = "" || "default string";
console.log(foo);

// 좌항의 피연산자가 Falsy 값이라도 null 또는 undefined가 아니면 좌항의 피연산자를 반환한다.
var foo = "" ?? "default string";
console.log(foo);
