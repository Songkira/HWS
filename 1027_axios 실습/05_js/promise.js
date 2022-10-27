function asyncFunc() {
  const result = new Promise(function (resolve, reject) {
    const now = new Date()
    if (now.getSeconds() % 2 == 0) {
      // 뭔가 일을 처리하고
      resolve('성공이야')
    } else {
      reject('실패했어요')
    }
  })
  return result
}

asyncFunc()
  .then(function (success) { // 성공한 경우 실행할 코드
    console.log(success)
    return 100    
  })
  .then(res => console.log(res))
  .then(res => console.log(res))
  .then(res => console.log(res))
  .catch(fail => console.log(fail))
  .finally(() => console.log('final'))