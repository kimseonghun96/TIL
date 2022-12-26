// console.log(add(2,7)) // 선언식은 위에 올려도 출력이 되지만 표현식은 안된당.
// function add(num1, num2) {
//     return num1 + num2
// }

// const sub = function (num1, num2) {
//     return num1 - num2  
// }
// console.log(sub(2,7))

// const greeting = function(name) {
//     return `HI ${name}`
// }

// //1단계
// const greeting = (name) => {
//     return `HI ${name}`
// }

// //2단계
// const greeting = name =>  {
//     return `HI ${name}`
// }

// //3단계
// const greeting = (name) => `HI ${name}`

// // 보통 1, 2단계를 사용한다. but 명확성과 일관성을 위해 항상 인자 주위에는 ('()')를 포함하는 것을 권장한다.

// function (num) {return num ** 3}

// (num) => {return num ** 3}


// console.log(((num) => num ** 3)(2))  //2**3

const numbers = [1, 2, 3, 4, 5]

console.log(numbers[0])
console.log(numbers[-1]) // undefined
console.log(numbers.length) //길이가 출력된다
console.log(numbers[numbers.length] -1) //길이의 마지막 마지막 인자가 출력됨

numbers.reverse()
console.log(numbers)

numbers.push(100)
console.log(numbers)

numbers.pop()
console.log(numbers)

console.log(numbers.includes(1))  //있어서 true
console.log(numbers.includes(100)) //없어서 false

console.log(numbers.indexOf(3))     // 인덱스 출력
console.log(numbers.indexOf(100))   // 없으면 -1 출력

console.log(numbers.join())
console.log(numbers.join(''))
console.log(numbers.join(' '))
console.log(numbers.join('-'))