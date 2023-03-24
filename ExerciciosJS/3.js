// Faça um programa que leia um valor inteiro e mostre a tabuada de 1 a 10 do valor lido.

let num = 4;

console.log(`\nTABUADA DO ${num}:\n`)

for (let i = 0; i < 11; i++){
    console.log(`${num} x ${i}: ${num*i}`)
}