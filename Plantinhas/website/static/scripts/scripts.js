let i = 0;
let lista = [];
let time = 2000;
let section = document.getElementById('sono');

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
    var abre = document.querySelector(".info"+codigo)
    var esconde = document.querySelector(".principal"+codigo)
    abre.style.visibility = "visible"
    esconde.style.visibility = "hidden"

    document.querySelector(".plantar"+ codigo ).style.visibility = "visible"
    document.querySelector(".menos"+ codigo ).style.visibility = "visible"
    document.querySelector(".mais"+ codigo ).style.visibility = "hidden"
    document.querySelector(".img"+codigo).style.visibility = "hidden"


    x.style.width = "100%"
    x.style.visibility = "visible"  
}

function menos(codigo){
    var abre = document.querySelector(".info"+codigo)
    var esconde = document.querySelector(".principal"+codigo)
    esconde.style.visibility = "visible"
    abre.style.visibility = "hidden"

    document.querySelector(".plantar"+ codigo ).style.visibility = "hidden"
    document.querySelector(".menos"+ codigo ).style.visibility = "hidden"
    document.querySelector(".mais"+ codigo ).style.visibility = "visible"
    document.querySelector(".img"+codigo).style.visibility = "visible"

}