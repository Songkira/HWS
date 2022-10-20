// let val
// console.log(val) // undefined

// // 함수 정의
// function myFunc(arg1, arg2, arg3) {
//   console.log(arg1, arg2, arg3)
// }
// // myFunc()   // undefined undefined undefined
// myFunc(1)     // 1 undefined undefined
// myFunc(1, 2)  // 1 2 undefined
// myFunc(1, 2, 3)     // 1 2 3
// myFunc(1, 2, 3, 4)  // 1 2 3

// function myFunc(arg1, arg2, ...arg3) {
//   console.log(arg1, arg2, arg3)
// }
// myFunc()      // undefined undefined []
// myFunc(1)     // 1 undefined []
// myFunc(1, 2)  // 1 2 []
// myFunc(1, 2, 3)     // 1 2 [ 3 ]
// myFunc(1, 2, 3, 4)  // 1 2 [ 3, 4 ]
// --------------------------------------

function myFunc(arg1, arg2, ...arg3) {
  console.log(arg1, arg2, arg3)
}

arr1 = [1, 2, 3, 4, 5]
myFunc(...arr1)  // myFunc(1, 2, 3, 4, 5)
// 1 2 [ 3, 4, 5 ]

arr2 = ['a', 'b', ...arr1, 'c']
console.log(arr2)
// [
//   'a', 'b', 1, 2,
//   3,   4,   5, 'c'
// ]







