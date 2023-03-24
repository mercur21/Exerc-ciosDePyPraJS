// Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

let num1 = 2;
let num2 = 9;

let x = num2;
let y = num1;

let L = [];

if (num2 < num1){
    while (num2 < num1-1) {
        num2++
        L.push(num2)
    }
    console.log(L)
}
else{
    while (num1 < num2-1) {
        num1++
        L.push(num1)
    }
    console.log(L)
}