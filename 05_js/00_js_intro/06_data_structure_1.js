const numbers =[1,2,3,4,]

console.log(numbers[0])
console.log(numbers[-1]) // undedined 정확한 양의 정수 index 만 가능 
console.log(numbers.length) // 4
console.log(numbers.reverse()) // 원본 파괴

//push
console.log(numbers.push('a')) // return arr length
console.log(numbers)

//pop 마지막 요소를 제거후 returb
console.log(numbers.pop())
console.log(numbers)

//unshift 배열의 가장 앞요소를 추가하고 return 은 배열의 길이
console.log(numbers.unshift('a'))
console.log(numbers)

//shift  배열의 가장 앞의 요소 제거후 return
console.log(numbers.shift())
console.log(numbers)

// boolean return
console.log(numbers.includes(1))
console.log(numbers.includes(0))

console.log(numbers.push('a','a'))
console.log(numbers)
console.log(numbers.indexOf('a')) // 4 -> 중복이 존재한다면 처음 찾은 요소의 index를 리턴 
console.log(numbers.indexOf('b'))

// join  배열의 요소를 join 함수의 인자를 기준으로 이어서 문자열로 return 
console.log(numbers.join()) // 4,3,2,1,a,a  아무것도 넣지 않으면 , 를 기준으로 가져옴 
console.log(numbers.join('')) // 4321aa 
console.log(numbers.join('-')) // 4-3-2-1-a-a 

console.log(numbers) //원본을 변화 하지 않음
