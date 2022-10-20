// 화살표 함수(익명 함수다.)

// // 함수 선언식
// function functionName(name) {

// }

// // 함수 표현식
// const functionVar = function (name) {

// } 
// ------------------------------------
const add = function (a, b) {
  return a + b
}

// console.log(add(1, 2)) // 3

function func(f) {
  console.log('call f()')
  console.log(f(1, 2))
}

func(add)
func((a, b)=> a + b)
// call f()
// 3
// -----------------------------
// function (a, b) {
//   return a + b
// }

// // 1. function 날리기
// (a, b) => { return a + b }

// // 2. 매개변수가 '하나'면 괄호도 생략할 수 있음
// // 중괄호를 생략할 수 있다.

// // 3. return 문 '하나'면 중괄호를 생략할 수 있다.
// // return 생략
// (a, b) => a + b



