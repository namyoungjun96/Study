var person = {
  name: "Lee",
};
// 참조 값을 복사(얕은 복사). copy와 person은 동일한 참조 값을 갖는다.
var copy = person;
// copy와 person은 동일한 객체를 참조한다.
console.log(copy === person);

copy.name = "Kim";
person.address = "Seoul";

// copy와 person은 동일한 객체를 가리킨다.
// 따라서 어느 한쪽에서 객체를 변경하면 서로 영향을 주고받는다.
console.log(person);
console.log(copy);

var person1 = {
  name: "Lee",
};

var person2 = {
  name: "Lee",
};

console.log(person1 === person2);
console.log(person1.name === person2.name);
