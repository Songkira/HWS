// num = 2 // 0, 1, 2, 3

// switch 는 값에 일치하는 것에서 시작해서 출력
// 범위 표현이 안됨.
// switch(num) {
//   case 0:
//     console.log(0)
//   case 1:
//     console.log(1)
//   case 2:
//     console.log(2)
//   case 3:
//     console.log(3)
// }
// // 2
// // 3

// ---------------------------
// num = 1

// switch(num) {
//   case 0:
//     console.log(0)
//   case 1:
//     console.log(1)
//   case 2:
//     console.log(2)
//   case 3:
//     console.log(3)
// }
// // 1
// // 2
// // 3
// -----------------------
// num = 1

// switch(num) {
//   case 0:
//     console.log(0)
//   case 1:
//     console.log(1)
//   case 2:
//     console.log(2)
//     break
//   case 3:
//     console.log(3)
// }
// // 1
// // 2
// -----------------------
// num = 0

// switch(num) {
//   case 0:
//     console.log(0)
//     break
//   case 1:
//     console.log(1)
//     break
//   case 2:
//     console.log(2)
//     break
//   case 3:
//     console.log(3)
// }
// // 0
// --------------------
color = 'red'

// switch(color) {
//   case 'blue':
//     console.log(0)
//     break
//   case 'green':
//     console.log(1)
//     break
//   case 'red':
//     console.log(2)
//     break
//     default:
//     console.log(3)
// }
// // 2

switch(color) {
  case 'blue':
    console.log(0)
    break
  case 'green':
  case 'red':
    console.log(1)
    console.log(2)
    break
  default:
    console.log(3)
}
// 1
// 2

// if (color=='blue') {

// } else if (color === 'green') {

// } else if (color === 'red') {

// } else { // default 

// }

