/* 
1. forEach 메서드를 활용해 모든 사용자들의 이름을 출력하시오.
2. filter 메서드를 활용해 결혼한 사람들만 모아 married 상수에 할당하시오.
3. find 메서드를 활용해 이름이 Tom인 사람만 tom 상수에 할당하시오.
4. map 메서드를 활용해 모든 사용자에게 isAlive 키를 추가하고 true로 설정한 뒤, newUsers 상수에 할당하시오.
5. reduce 메서드를 활용해 모든 사용자들의 계좌잔액을 totalBalance 상수에 할당하시오.
*/

const users = [
  { name: 'John', age: 31, isMarried: true, balance: 100, },
  { name: 'Sarah', age: 22, isMarried: false, balance: 200, },
  { name: 'Ashley', age: 25, isMarried: true, balance: 300, },
  { name: 'Robert', age: 27, isMarried: false, balance: 400, },
  { name: 'Tom', age: 35, isMarried: true, balance: 500, },
]

// 1.
const printname = function (user) {
  console.log(user.name)
}
users.forEach((user) => console.log(user.name))
// users.forEach(printname)
// -----------------------------------------------
// 2.
// const marryFilter = function (user) {
//   return user.isMarried === true
// }
// const married = users.filter(marryFilter)
// console.log(married)
// -------------------------------------------
const married = users.filter((user) => user.isMarried)

// -----------------------------------
// 3. find 메서드를 활용해 이름이 Tom인 사람만 tom 상수에 할당하시오
// const tom = users.find((user) => {
//   return user.name === 'Tom'
// })
// console.log(tom)
// ---------------------------------
const tom = users.find((user) => user.name === 'Tom')
// -------------------------------------
// 4.map 메서드를 활용해 모든 사용자에게 isAlive 키를 추가하고 true로 설정한 뒤, newUsers 상수에 할당하시오.

const newUsers = users.map((user) => {
  user.isAlive = true
  return user
})

//--------------------------------------
// 5. reduce 메서드를 활용해 모든 사용자들의 계좌잔액을 totalBalance 상수에 할당하시오.
const totalBalance = users.reduce((result, user) => {
  // console.log(user.balance)
  return result + user.balance
}, 0)
console.log(totalBalance)
// 1500

// ------------------------------------------------------
const totalBalance2 = users.reduce((user1, user2) => {
  // console.log(user1, user2)
  return user2
})
console.log(totalBalance2) 
// { name: 'Tom', age: 35, isMarried: true, balance: 500, isAlive: true }

const totalBalance3 = users.reduce((curTotal, user) => {
  // console.log(user.balance)
  return curTotal + user.balance
}, 0)
console.log(totalBalance3)
// 1500
const totalBalance4 = users.reduce((curTotal, user) => curTotal + user.balance, 0)