const numbers = [90, 80, 70, 100]

//총합

// const sumNum = numbers.reduce(function (result, number){
//   return result + number
// } , 0)  // 끝에 result의 초기값을 적어줘야한다.

// console.log(sumNum)

//2   위의 function 지우고 화살표 함수
const sumNum = numbers.reduce((result, number) => {
    return result + number
  } , 0)  // 끝에 result의 초기값을 적어줘야한다.
  
  console.log(sumNum)

//3 평균 값
const avgNum = numbers.reduce((result, number) => result + number , 0) / numbers.length
  
  console.log(avgNum)