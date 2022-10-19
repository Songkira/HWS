// 1번
const nums = [1,2,3,4,5,6,7,8]

for (const i = 0; i < nums.length; i++) {
  console.log()
}

// for (const i = 0; i < nums.length; i++) {
//                                     ^
// 해답 : const는 재할당을 허용하지 않기때문에 
//        let으로 바꿔 작성해야 함.

// TypeError: Assignment to constant variable.

// 2번
for (num in nums) {
  console.log(num, typeof num)
}
// 해답 : in은 인덱스값을 출력하기 때문에 
      // 대신 of로 바꿔 작성해야 함. 
// 0 string
// 1 string
// 2 string
// 3 string
// 4 string
// 5 string
// 6 string
// 7 string
