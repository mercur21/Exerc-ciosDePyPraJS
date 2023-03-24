// Faça um programa que leia uma lista de 5 números e informe a soma e a média dos números.

let L = [1,4,1,1,2]
let num = 0;
for (let i = 0; i < L.length;i ++){
    num = num + L[i]
}
let media = num / L.length
console.log(`A soma dos números é ${num}, e a média é ${media}.`)