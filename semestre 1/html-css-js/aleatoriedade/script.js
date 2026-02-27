function corale(){
    const letra = "0123456789ABCDEF";
    let cor = "#";

    for (let i = 0; i < 6; i++){
        cor += letra[Math.floor(Math.random() * 16)]
    };
    return cor;
}

document.getElementById("bot").addEventListener("click", function(){
    document.getElementById("ttl").style.color = corale();
})