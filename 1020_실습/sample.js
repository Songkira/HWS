
// Array Helper Method
arr = [1, 2, 3, 4, 5]

// elem: 개별 요소, idx: 요소의 인덱스, arr: 배열
// const myFunc = function (elem, idx, arr) {
//   console.log(elem, idx, arr)
// }

// arr.forEach(myFunc)
// 1 0 [ 1, 2, 3, 4, 5 ]
// 2 1 [ 1, 2, 3, 4, 5 ]
// 3 2 [ 1, 2, 3, 4, 5 ]
// 4 3 [ 1, 2, 3, 4, 5 ]
// 5 4 [ 1, 2, 3, 4, 5 ]

// arr.forEach((elem, idx) => {
//   console.log(elem, idx)
// })
// 1 0
// 2 1
// 3 2
// 4 3
// 5 4
//-------------------------------
// map

let result = arr.map((elem) => {
  return elem ** 3
})

// console.log(result, arr) // [ 1, 8, 27, 64, 125 ] [1, 2, 3, 4, 5]
//------------------------------------------
// filter
result = arr.filter((elem) => {
  return elem % 2
})
// console.log(result) // [ 1, 3, 5 ]

// ---------------------------------------
result = arr.filter((elem) => {
              return elem % 2
            }).map((elem) => {
              return elem ** 3
            })

// console.log(result) // [ 1, 27, 125 ]

//-----------------------------------
// reduce

// elem: 개별 요소, idx: 요소의 인덱스, arr: 배열
// arr.reduce((acc, elem) => {
//   console.log(acc, elem)
//   return elem
// })
// 1 2
// 2 3
// 3 4
// 4 5
// -----------------------------------------
// arr.reduce((acc, elem) => {
//   console.log(acc, elem)
//   return elem
// }, 0)
// 0 1
// 1 2
// 2 3
// 3 4
// 4 5
// -----------------------------
const sum = arr.reduce((acc, elem) => {
  return acc + elem
})
console.log(sum) // 15

