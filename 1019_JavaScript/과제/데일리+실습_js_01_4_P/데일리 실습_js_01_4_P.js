const p1 = ['rock', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'paper', 'paper', 'rock', 'scissors']
const p2 = ['paper', 'paper', 'rock', 'scissors', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'rock']

const playGame = (p1_choice, p2_choice) => {
	for (let i = 0; i < p1.length ; i ++) {
		if (p1_choice[i] === p2_choice[i]) {
			console.log(0)
		} else if (p1_choice[i] === 'rock' && p2_choice[i] === 'paper') {
			console.log(2)
		} else if (p2_choice[i] === 'rock' && p1_choice[i] === 'paper') {
			console.log(1)
		} else if (p1_choice[i] === 'scissors' && p2_choice[i] === 'paper') {
			console.log(1)
		} else if (p2_choice[i] === 'scissors' && p1_choice[i] === 'paper') {
			console.log(2)
		} else if (p1_choice[i] === 'scissors' && p2_choice[i] === 'rock') {
			console.log(2)
		} else if (p2_choice[i] === 'scissors' && p1_choice[i] === 'rock') {
			console.log(1)
		}
	}
}

console.log(playGame(p1, p2))
// 2
// 0
// 2
// 0
// 2
// 1
// 2
// 1
// 0
// 2