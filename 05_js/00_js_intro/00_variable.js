let x = 1
if (x === 1) {
   let x = 2

   console.log(x) //2
}

console.log(x) //1


// const (상수) 값이 변하지 않는 값 but, not  불변

// const  선언시에 초기값을 생략하면 오류 발생 
// const MY_FAV
const MY_FAV = 7

console.log('my favourite number is ' + MY_FAV)
// 상수를 재선언 혹은 재할당하려는 시도는 모두 오류 발생 

//MY_FAV = 20
//var MY_FAV = 20
//let MY_FAV = 20
//const MY_FAV = 20



if (MY_FAV === 7) {
  // 블록 유효 범위로 지정된 MY_FAV 이라는 변수를 만듦으로 괜찮다.
  // 즉, 전역이 아닌 범위 안이므로 이름 공간에서 충돌이 나지 않는다.
  let MY_FAV = 20
  console.log('my favourite number is ' + MY_FAV)
}

console.log(MY_FAV) // ?



// var 
function varTest() {
  var x = 1
  if (true) {
    var x =2 
    console.log(x)//2

     
  }
  console.log(x) //2
}
varTest()

// let 
function letTest() {
  let x = 1
  if (true) {
    let x =2 
    console.log(x)//2

     
  }
  console.log(x) //1
}
letTest()


// let 과 var
var a = 1
let b = 2

if (a === 1) {
  var a = 11
  let b = 22

  console.log(a) //11
  console.log(b) //22
}

console.log(a) //11
console.log(b) //2


// 식별자 작성 스타일
// 1. 카멜 케이스(camelCase) - 객체 변수 함수 ( === lower-camel -case)

let dog
let variavleName

// 배열은 복수형 변수명을 사용
const dogs = []

// 정규 표현식은 'r'로 시작
const rDecs = /.*/

//함수
function getPropertyName() {
  return 1
  
}

// boolean을 반환하는 변수나 함수 = 'is'로 시작
let isAvailable = false

// 2 파스칼 케이스 = 클래스 생성자
class User{
  constructor(options) {
    this.name = options.name
  }
}

// 3. 대문지 스네이크 케이스(SNAKE_CASE) - 상수
// 이 표현은 변수와 변수의 속성이 변하지 않는 다는 것을 프로그래머에게 알려준다
const API_KEY = 'avcsjdw'
