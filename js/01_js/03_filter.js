const products = [
    { name: 'cucumber', type : 'vegetable'},
    { name: 'banana', type : 'fruit'},
    { name: 'carrit', type : 'vegetable'},
    { name: 'apple', type : 'fruit'},
]

const fruitFilter = function (product) {
    return product.type === 'fruit'
}

// const newArry = products.filter(fruitFilter)

// console.log(newArry)

// //2
// const newArry = products.filter(function (product) {
//     return product.type === 'fruit'
// })

// //3
// const newArry = products.filter((product) => {
//     return product.type === 'fruit'
// })

//4