// 1.
function palindrome(str) {
    let lst = str.split('')
    let rev = lst.reverse()

    console.log(str === rev.join(''))
  }

// 2.
// function palindrome(str) {
//   for (let)
// }
  // 출력
  palindrome('level')
  // palindrome('level') => true
  // palindrome('hi') => false


// const arr = [...'abcde']
// console.log(arr) // [ 'a', 'b', 'c', 'd', 'e' ]