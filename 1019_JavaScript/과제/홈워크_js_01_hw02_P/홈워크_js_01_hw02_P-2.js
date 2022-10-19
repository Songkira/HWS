const nums = [1, 2, 3, 4]

// 1.
const tripleFunc = function (num) {
  return num * 3
}
 
const tripleNums = nums.map(tripleFunc)
console.log(tripleNums)

// 2. 
const tripleNums = nums.map(function (num) {
  return num * 3
})
console.log(tripleNums)

// 3.
const tripleNums = nums.map((num) => num * 3)
console.log(tripleNums)