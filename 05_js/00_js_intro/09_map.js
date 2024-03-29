//2. map(callback)
// 배열 내의 모든 요소에 대하여 각각 주어진 함수 를 호출한 결과를 모아 새로운 배열을 return 
// 일정한 형식의 배열을 다른 형식으로 바꿔야 할때 사용한다.


//for
var numbers = [1,2,3,]
var doubleNumbers = []

for (var i = 0; i < numbers.length; i++) {
  doubleNumbers.push(numbers[i]*2)
}

console.log(doubleNumbers)
console.log(numbers) //원본 유지

// map 
const NUMBERS = [1,2,3,]

const DOBLE_NUMBERS = NUMBERS.map(function(number){
  return number *2
})
console.log(DOBLE_NUMBERS)
console.log(NUMBERS)

// 2-1 practice

const newNumbers = [4, 9, 16,]
const roots = newNumbers.map(Math.sqrt)

console.log(roots)

// 2-2 practice  map 을 사용해 images 배열 안에 object 들만 저장 되어있는 heights  배열을 만드시오
const images = [
  { height: '34px', width: '39px'},
  { height: '12px', width: '11px'},
  { height: '29px', width: '56px'},
]

const heights = images.map(function(image){
  return image.height
})
console.log(heights)

// 2-3 map 을 사용해 trips 배열의 값을 게산해서 속도 값을 저장하는 speeds를 만드시오

const trips = [
  {distance: 35, time: 10},
  {distance: 90, time: 10},
  {distance: 60, time: 25},
]

const speeds = trips.map(function(speed){
  return speed.distance / speed.time
})
console.log(speeds)


// 2-4 
const brands = ['Marvel', 'DC', ]
const movies = ['Ironman', 'Batman',]

const comics = brands.map((x,i) => ({ name: x, hero: movies[i] })) 
console.log(comics)


