let i = 0;
let lista = [];
let listaimg = [];
let time = 3000;
let section = document.getElementById('sono');
// let div = document.getElementsByClassName('ache_uma_planta')

lista[0] = "aumentar o contato com a natureza";
lista[1] = "criar um ambiente bonito e agradável dentro de casa";
lista[2] = "atividade terapêutica para aliviar o stress do dia a dia";
lista[3] = "desenvolver hábitos alimentares mais saudáveis";
lista[4] = "ter acesso a uma alimentação sem agrotóxicos";
lista[5] = "diminuir a dependência da indústria alimentícia";

let imagem = document.getElementById("trocarImagem")

function tomara(){
        if (imagem.src.match("icone-frase1")){
            imagem.src="../static/imagens/cherry-blossom.png"
        }
        else if (imagem.src.match("cherry-blossom")){
            imagem.src="../static/imagens/woman.png"
        }
        else if (imagem.src.match("woman")){
            imagem.src="../static/imagens/vegetables.png"
        }
        else if (imagem.src.match("vegetables")){
            imagem.src="../static/imagens/poison.png"
        }
        else if (imagem.src.match("poison")){
            imagem.src="../static/imagens/industria.png"
        }
        else if (imagem.src.match("industria")){
            imagem.src="../static/imagens/icone-frase1.png"
        }
        setTimeout('tomara()', time)
}

function slideShow(){
    section.innerHTML = lista[i];
    if(i < lista.length - 1){
        i++;
    }
    else{
        i = 0;
    }
    setTimeout('slideShow()', time);
}

window = slideShow()
setTimeout('tomara()', time)


function clicar_planta(){
    window.location = "plantas/0"
}



function mais(codigo){
    var abre = document.querySelector(".info"+codigo)
    var esconde = document.querySelector(".principal"+codigo)
    esconde.style.visibility = "hidden"
    abre.style.visibility = "visible"

    document.querySelector("#plantar"+ codigo ).style.visibility = "visible"
    document.querySelector(".menos"+ codigo ).style.visibility = "visible"
    document.querySelector(".mais"+ codigo ).style.visibility = "hidden"
    document.querySelector(".img"+codigo).style.visibility = "hidden"

}

function menos(codigo){
    var abre = document.querySelector(".info"+codigo)
    var esconde = document.querySelector(".principal"+codigo)
    esconde.style.visibility = "visible"
    abre.style.visibility = "hidden"

    document.querySelector("#plantar"+ codigo ).style.visibility = "hidden"
    document.querySelector(".menos"+ codigo ).style.visibility = "hidden"
    document.querySelector(".mais"+ codigo ).style.visibility = "visible"
    document.querySelector(".img"+codigo).style.visibility = "visible"

}

let fadeIn = document.querySelector(".fadeIn");