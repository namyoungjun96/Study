setImmediate(() => {
  console.log("immediate");
});

process.nextTick(() => {
  console.log("nextTick");
});

setTimeout(() => {
  console.log("timeout");
}, 0);

Promise.resolve().then(() => console.log("promise"));

// nextTick, Promise == microtask 라고 구분지어 부른다.
// microtask는 다른 콜백함수보다 우선처리된다.
// 재귀 호출을 하게되면 이벤트 루프는 다른 콜백함수보다 우선 처리하여, 콜백 함수들이 실행되지 않을수도 있다.
