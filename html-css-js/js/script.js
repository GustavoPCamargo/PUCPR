document.getElementById("botao").addEventListener("click", function(){
    let nome = document.getElementById("nome").value;
    
    if(nome.trim() !== ""){
        alert("ola, " + nome + ", vc esta usando js.")
    }
    else{
        alert("preencha o formulario.")
    }
});