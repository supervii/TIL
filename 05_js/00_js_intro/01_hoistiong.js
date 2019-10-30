console.log(a)
var a = 10
console.log(a)

// Js 가 이해한 코드
var a // 선언+초기화 
console.log(a)
var a = 10
console.log(a)


// let 은 안된다 ReferenceError
console.log(b)
let b = 15
console.log(b)

// 마찬가지로 아래와 같은 과정을 거친다
// js 가 이해한 코드
let b // 선언 +TDZ (초기화 X)
console.log(b)
let b = 15 // 할당 불가(초기화가 아직 안됨)
console.log(b)
// 왜 안되지 ?

// js 가 이해한 코드 
var x
var y

if (x !== 1) {
  console.log(y) //undefined
  var y =3
  if (y === 3) {
    var x = 1
  }
  console.log(y) //3
}

if (x ===1) {
  console.log(y)//3
  
}
