
const foto = document.getElementById("foto")
const botao = document.getElementById("botao")

let alternar = false

botao.addEventListener("click", () => {
    alternar = !alternar
    if (alternar){
        foto.src = 'img/img2.jfif'
        foto.classList.add ('borda-alternada')
    }
    else{
        foto.src = 'img/img1.jfif'
        foto.classList.remove('borda-alternada')
    }
})