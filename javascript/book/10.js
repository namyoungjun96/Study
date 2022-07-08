var person = {
  name: "Lee",
  sayHello: function () {
    console.log("Hello! My Name is ${this.name}.");
  },
};

console.log(typeof person);
console.log(person);

var empty = {};
console.log(typeof empty);

var obj = {};
var key = "hello";
// 키를 동적으로 할당할 수 있다.
obj[key] = "world";

console.log(obj);

var foo = {
  0: 1,
  1: 2,
  2: 3,
};
// 키가 숫자여도 문자열로 자동 컨버팅을 한다. 밸류는 아님.
console.log(foo);

var foo = {
  name: "Lee",
  name: "Kim",
};
// 키가 똑같으면 나중에 선언한 밸류를 덮어씌운다.
console.log(foo);

var person = {
  name: "Lee",
};
// 자동으로 동적 생성한다.
person.age = 20;
console.log(person);

delete person.age;
// 없는 프로퍼티를 삭제하면 에러도 나지않고 무시한다.
delete person.address;

console.log(person);

var x = 1,
  y = 2;

var obj = {
  x: x,
  y: y,
};
console.log(obj);

let a = 1,
  b = 2;
const obj1 = { a, b };
console.log(obj1);

var prefix = "prop";
var i = 0;

var obj = {};
// 프로퍼티 이름으로 프로퍼티 키 동적으로 생성 가능
obj[prefix + "-" + ++i] = i;
obj[prefix + "-" + ++i] = i;
obj[prefix + "-" + ++i] = i;

console.log(obj);

const prefix1 = "prop";
let i1 = 0;
// 객체 내부에서 계산된 프로퍼티 이름으로 프로퍼티 키를 동적으로 생성
const obj2 = {
  [`${prefix1}-${++i1}`]: i,
  [`${prefix1}-${++i1}`]: i,
  [`${prefix1}-${++i1}`]: i,
};

console.log(obj2);

// ES 5
var obj = {
  name: "Nam",
  sayHi: function () {
    console.log("Hi! " + this.name);
  },
};

obj.sayHi();

// ES6
const obj3 = {
  name: "Nam",
  // 메서드 축약 가능
  sayHi() {
    console.log("Hi! " + this.name);
  },
};

obj3.sayHi();
