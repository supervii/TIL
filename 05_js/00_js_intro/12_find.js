// array helper method
// 5 .find(callback())
// 주어진 콜백함수를 만족하는 첫번째 요소의 값을 반환.
// 없다면 undefined를 반환
// 조건에 맞는 인덱스가 아니라 요소 자체를 원할 때 사용

// for
var users = [
  { name: 'Tony Stark', age: 45 },
  { name: 'Steve Rogers', age: 32 },
  { name: 'Thor', age: 40 },
  { name: 'Tony Stark', age: 23 },
]

for (var i =0; i < users.length; i++) {
  if (users[i].name === 'Tony Stark') {
    user = users[i]
    break // 원하는 조건에 도달하면 더 돌지 않는다.
  }
}
console.log(user)

//find
const USERS = [
  { name: 'Tony Stark', age: 45 },
  { name: 'Steve Rogers', age: 32 },
  { name: 'Thor', age: 40 },
  { name: 'Tony Stark', age: 23 },
]
const user1 = USERS.find(user=> user.name =='Tony Stark')

console.log(user1)
