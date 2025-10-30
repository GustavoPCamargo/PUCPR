const btn = document.getElementById("botao")
const ttl = document.getElementById("titulo")
const foto = document.getElementById("foto")
const body = document.getElementById("body")
const cont = document.getElementsByClassName("container")
const msg = document.getElementById("msg")


let alternar = false
let alternar2 = false

btn.addEventListener("click", () => {
    alternar = !alternar
    if (alternar){
        foto.src = "img/img2.jfif"
        ttl.classList.add("fonte-alternada")
        body.style.background = corale()
        msg.innerText = ("Sou o Gustavo P Camargo, e irei Gabaritar esta prova")
        alternar2 = !alternar2
        if(alternar2){
            foto.src = "img/img3.jfif"
            ttl.classList.add("fonte-alternada")
            body.style.background = corale()
        }
    }
    else {
        foto.src = 'img/img1.jfif'
        ttl.classList.remove('fonte-alternada')
        body.style.background = corale()
    }
})

function corale(){
    const letra = "0123456789ABCDEF";
    let cor = "#";

    for (let i = 0; i < 6; i++){
        cor += letra[Math.floor(Math.random() * 16)]
    };
    return cor;
}
