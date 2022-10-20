// 가운데 정렬 별찍기

star = ''
for (let i = 1; i <= 9; i+=2) {
  star = '*'
  console.log(' '.repeat((9-i)/2) + star.repeat(i))
}