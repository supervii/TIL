const me = {
  name : 'ssafy', // key 가 한단어 일때
  'phone number' : '01012345678', // key가 여러 단어일때 
  appleProducts:{
    ipad: '2018pro',
    iphone: '7',
    macbook: '2019pro',
    }
}
console.log(me.name) //ssafy
console.log(me['name']) //ssafy
console.log(me['phone number']) // 키가 여러 단어인 경우 반드시 []로 접근
console.log(me.appleProducts)
console.log(me.appleProducts.ipad)

// object Literal 
var books =['Learning JS', 'Eloquent JS']

var comics = {
  'DC': ['Joker', 'Aquaman'],
  'Marvel' : ['Captain Marvel', 'Avengers']

}
var magazines = null

var bookShop ={
  books : books,
  comics: comics,
  magazines: magazines,
}
console.log(bookShop)

// ES6
// 
let bookShop2 ={
  books,
  comics,
  magazines,
}
console.log(bookShop2)


//Json
const jsonData = JSON.stringify({ // JSON -> String
  coffe: 'Americano',
  iceCream: 'Mint Choco',

})

console.log(jsonData)
console.log(typeof jsonData)

const parseData = JSON.parse(jsonData)
console.log(parseData)
console.log(typeof parseData)
