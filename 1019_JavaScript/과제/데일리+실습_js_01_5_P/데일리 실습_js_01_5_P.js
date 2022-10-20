const participantNums =  [[1, 3, 2, 2, 1], 
[3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21],
[9, 1, 8, 7, 71, 33, 62, 35, 11, 4, 7, 71, 33, 8, 9, 1, 4, 11, 35]
]

// 3
// 100
// 62
for (let i = 0; i < participantNums.length; i++) {
  console.log()
}
// console.log(participantNums)

// let i = 0
// for (let idx= 0; idx < participantNums.length; idx++) {
//   for (let n = 0; n < participantNums[idx].length - 1 ; n += 2) {
//     if (participantNums[idx][n] === participantNums[idx][n + 1]) {
//       continue
//     } else if (participantNums[idx][n] !== participantNums[idx][n+1]) {
//       console.log(participantNums[idx][n])
//     }
//   }
// }

const game = (arr1) => {
  for (let i = 0; i < arr1.length; i++) {
    let count = 0
    for (let j = 0; j < arr1.length; j++) {
      if (arr1[i] === arr1[j]) {
        count ++
        }
      }
      if(count === 1) {
        console.log(arr1[i]) 
    }
  }
}

for (let i = 0; i <participantNums.length; i++) {
  console.log(game(participantNums[i]))
}
