// 배열(Array)
const numbers = [1, 2, 3, 4, 5]

console.log(numbers[0]) // 1
console.log(numbers[-1]) // undefined
console.log(numbers.length) // 길이 = 5
console.log(numbers[numbers.length - 1]) // 인덱스([numbers.length - 1]) 위치에 있는 값 = 5

numbers.reverse()
console.log(numbers) // [ 5, 4, 3, 2, 1 ]

numbers.push(100)
console.log(numbers) // [ 1, 2, 3, 4, 5, 100 ]

numbers.pop()
console.log(numbers) // [ 1, 2, 3, 4, 5 ]

console.log(numbers.includes(1))   // true 
console.log(numbers.includes(100)) // false

console.log(numbers.indexOf(3)) // 2
console.log(numbers.indexOf(100)) // -1

console.log(numbers.join())     // 1,2,3,4,5
console.log(numbers.join(''))   // 12345
console.log(numbers.join(' '))  // 1 2 3 4 5
console.log(numbers.join('-'))  // 1-2-3-4-5