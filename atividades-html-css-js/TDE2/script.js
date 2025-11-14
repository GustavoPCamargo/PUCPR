//Funções básicas
function soma(a, b) {
    return a + b;
}

function subtracao(a, b) {
    return a - b;
}

function multiplicacao(a, b) {
    return a * b;
}

function divisao(a, b) {
    if (b === 0) return "Erro: divisão por zero!";
    return a / b;
}
//Manipulação de arrays
//pares
const filtrarPares = (arr) => arr.filter(num => num % 2 === 0);

// Calcular média dos valores
const calcularMedia = (arr) => {
    if (arr.length === 0) return 0;
    const somaTotal = arr.reduce((acc, num) => acc + num, 0);
    return somaTotal / arr.length;
};

//(callback)
function executarOperacao(a, b, callback) {
    return callback(a, b);
}

const numeros = [1, 2, 3, 4, 5, 6];

console.log("Soma:", soma(10, 5));
console.log("Subtração:", subtracao(10, 5));
console.log("Multiplicação:", multiplicacao(10, 5));
console.log("Divisão:", divisao(10, 5));

console.log("\nNúmeros pares:", filtrarPares(numeros));
console.log("Média:", calcularMedia(numeros));

console.log("\nUsando callback (multiplicação):",
    executarOperacao(3, 4, multiplicacao)
);

console.log("Usando callback (soma):",
    executarOperacao(3, 4, soma)
);
