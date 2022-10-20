const numbers = [90, 80, 70, 100]

// 총합

// const sumNum = numbers.reduce(function (result, number) {
//   return result + number
// }, 0)
// console.log(sumNum) // 340

// // 2. 화살표 함수
const sumNum = numbers.reduce((result, number) => {
  return result + number
}, 0)
console.log(sumNum) // 340

// 3.
// const sumNum = numbers.reduce((result, number) => result + number, 0)
// console.log(sumNum) // 340

// 평균
const avgNum = numbers.reduce((result, number) => result + number, 0) / numbers.length
// console.log(avgNum) // 85







