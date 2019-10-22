let i = 0;
let lista = [];
let time = 2000;
let section = document.getElementById('sono');
let div = document.getElementsByClassName('ache_uma_planta')

lista[0] = "ter acesso a uma alimentação sem agrotóxicos";
lista[1] = "atividade terapêutica para aliviar o stress do dia a dia";
lista[2] = "criar um ambiente bonito e agradável dentro de casa";
lista[3] = "desenvolver hábitos alimentares mais saudáveis";
lista[4] = "aumentar o contato com a natureza";
lista[5] = "diminuir a dependência da indústria alimentícia";

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


function mais(codigo){
    var x = document.querySelector(".info")
    x.style.visibility = "visible"
}


function clicar_planta(){
    window.location = "plantas/0"
}

function clicar_jardim(){
    window.location = "jardim/cadastro/1"
}