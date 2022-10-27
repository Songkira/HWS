axios.(a)('https://api.example.com/data')
	.(b)(function (response) {
	console.log((c))
})

(a) => get 
(b) => then
(c) => response.data

// 동기, 비동기 함수의 차이점
// 동기 = 순서대로 하나씩 처리하는 것
// 				요청을 보내고 응답이 올때까지 기다렸다가 다음 로직을 처리
// 비동기 = 작업을 시작한 후 결과를 기다리지 않고 다음 작업을 처리하는 것(병렬적 수행)
//	시간이 필요한 작업들은 요청을 보낸 뒤 응답이 빨리오는 작업부터 처리