function dobro(num){
    let valor = num * 2
    console.log("o dobro é", valor);
};
dobro(3);

function somarTres(num1, num2, num3){
    let valor = num1 + num2 + num3
    console.log("a soma é", valor)
}
somarTres(3, 5, 7)

function CparaF(num){
    let valor = num * 9/5 + 32
    console.log("em farenheit isso é", valor)
}
CparaF(20)

function maiorNumero(num1, num2){
    let maior = 0
    if (num1 > num2){
        maior += num1
    }
    else{
        maior += num2
    }
    console.log("o maior numero é o", maior)
}
maiorNumero(32, 56)

function imc(altura, peso){
    let imc = peso/(altura*altura)
    if (imc < 18.5){
        console.log("o seu imc é", imc,"vc esta abaixo do peso")
    }
    else if (imc < 25){
        console.log("o seu imc é", imc,"vc esta com peso normal")
    }
    else if (imc < 30){
        console.log("o seu imc é", imc,"vc esta com sobrepeso")
    }
    else if (imc >= 30){
        console.log("o seu imc é", imc,"vc esta com obesidade")
    }
}
imc(1.80, 69)