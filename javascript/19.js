function Person(name) {
  this.name = name;
}

// Person.prototype.sayHello = function () {
//   console.log(`Hi! My name is ${this.name}`);
// };

// Person.prototype.sayMyName = function () {
//   console.log(`My name is ${this.name}`);
// };

const me = new Person("Nam");
// const you = new Person("Kim");

// me.sayHello();
// you.sayHello();
// me.sayMyName();
// you.sayMyName();

const parent = {
  constructor: Person,
  sayHello() {
    console.log(`Hi! My name is ${this.name}`);
  },
};

Person.prototype = parent;

Object.setPrototypeOf(me, parent);

me.sayHello();

// constructor 프로퍼티가 생성자 함수를 가리킨다.
console.log(me.constructor == Person);
console.log(me.constructor == Object);

// 생성자 함수의 prototype 프로퍼티가 교체된 프로토타입을 가리킨다.
console.log(Person.prototype === Object.getPrototypeOf(me));
