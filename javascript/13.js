var x = "global";
function foo() {
  var x = "local";
  console.log(x);
}
foo();
console.log(x);

function foo2() {
  console.log("global function foo");
}
function bar() {
  function foo2() {
    console.log("local function foo");
  }
  foo2();
}
bar();

var x = 1;
function foo() {
  var x = 10;
  bar();
}
function bar() {
  console.log(x);
}
foo();
bar();
