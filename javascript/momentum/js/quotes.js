const quotes = [
  {
    quote: "후회해도 바뀌지않으니, 다음엔 늦지않게 노력하라.",
    author: "남영준",
  },
  {
    quote: "오늘 걷지않으면 내일 뛰어야한다.",
    author: "이동희",
  },
  {
    quote:
      "인생을 이해하려고 애쓰지 말고 인생을 살아라. 사랑을 애써 이해하려고 들지 말라. 사랑속으로 들어가라.",
    author: "오쇼",
  },
  {
    quote: "살야야 할 이유를 아는 사람은 어떠한 상황도 견딜 수 있다.",
    author: "니체",
  },
  {
    quote:
      "아무리 약한 사람이라도 단 하나의 목적에 자신의 온 힘을 집중시킴으로써 무엇인가 성취할 수 있지만, 아무리 강한 사람이라도 힘을 많은 목적에 분산하면 어떤 것도 성취할 수 없다.",
    author: "몽테스키외",
  },
  {
    quote: "스스로를 신뢰하는 순간 어떻게 살아야 할지 깨닫게 된다.",
    author: "요한 볼프강 폰 괴테",
  },
];

const quote = document.querySelector("#quote span:first-child");
const author = document.querySelector("#quote span:last-child");
const todaysQuote = quotes[Math.floor(Math.random() * quotes.length)];

quote.innerText = todaysQuote.quote;
author.innerText = todaysQuote.author;
