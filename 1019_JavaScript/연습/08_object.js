const myInfo = {
  name: 'jack',
  phoneNumber: '123456',
  'samsung product': {
    buds: 'Buds pro',
    galaxy: 'S99',
  },
}

// console.log(myInfo.name)    // jack
// console.log(myInfo['name']) // jack

// console.log(myInfo['samsung product']) // { buds: 'Buds pro', galaxy: 'S99' }
// console.log(myInfo['samsung product'].galaxy) // S99

// ------------------------------------
// 2. 메서드명 축약
const obj = {
  name: 'jack',
  greeting() {
    console.log('hi')
  }
}

// console.log(obj.name)
// console.log(obj.greeting())
// hi
// undefined

//---------------------------------------
// 3. 계산된 속성
const key = 'ssafy'
const value = ['한국', '미국', '일본', '중국']

const myObj = {
  [key]: value,
}

// console.log(myObj)      //{ ssafy: [ '한국', '미국', '일본', '중국' ] }
// console.log(myObj.ssafy)//[ '한국', '미국', '일본', '중국' ]

// -------------------------------------
// JSON 변환
const jsonData = {
  coffee: 'Americano',
  iceCream: 'Mint Choco',
}

// Object -> json
const objToJson = JSON.stringify(jsonData)

console.log(objToJson) // {"coffee":"Americano","iceCream":"Mint Choco"}
console.log(typeof objToJson) // string

// json -> Object
const jsonToObj = JSON.parse(objToJson)
console.log(jsonToObj) //{ coffee: 'Americano', iceCream: 'Mint Choco' }
console.log(typeof jsonToObj) // object
