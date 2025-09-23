const btnEsconder = document.getElementById("btnEsconder")
const btnTamanho = document.getElementById("btnTamanho")
const foto = document.getElementById("foto")

btnEsconder.addEventListener("click", function(){
    if (btnEsconder){
        foto.style.display("none")
        btnEsconder.style.textcontent("mostrar")
    }
    else{
        foto.style.display("block")
    }
})
btnTamanho.addEventListener("click", function(){
    if(btnTamanho){
        foto.width("")
    }
})


const clique = addEventListener("click", function(){})