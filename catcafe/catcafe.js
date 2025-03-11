function darkmode() {
    //recordemos que el tag regresa un array
    document.getElementsByTagName("body")[0].style.backgroundImage="url('https://marmoles.mx/3049-large_default/marmol_negro_monterrey_veta_blanca_305xllx1.jpg')";
    document.body.style.color="white";

    document.getElementById("encabezado").style.color = "black";
    document.getElementById("encabezado").style.backgroundColor = "#D7CCC8"; 

    elements = document.getElementsByClassName("descripcion");
    for (var i = 0; i < elements.length; i++) {
        elements[i].style.color = "white";
    }
    elements = document.getElementsByClassName("titulo");
    for (var i = 0; i < elements.length; i++) {
        elements[i].style.color="beige";
        elements[i].style.backgroundColor="black";
    }
}


let indice = 0; // Comienza en lunes
let dias = [ "martes", "miercoles", "jueves", 'viernes','sabado']; // IDs de los divs

function menu() {
 
    // Oculta el día actual
    document.getElementById(dias[indice]).style.display = "none";

    // Avanza al siguiente día (y vuelve a 0 si llega al final)
    indice = (indice + 1) % dias.length;

    // Muestra el nuevo día
    document.getElementById(dias[indice]).style.display = "block";


}

function mostrar(id){
    contenedores =document.getElementsByClassName("descripcion");
    contenedor= contenedores[id];
    display = window.getComputedStyle(contenedor).display
    if (display=="none") {
       contenedor.style.display= "inline-block";
    } else {
        contenedor.style.display= "none";
    }
    

}




let gato = [
    " /\\_/\\  ",
    "( o.o )",
    " > ~ < ",
    "/       \\",
    "| | | | |",
    "'-'-'-'-'"
];

for (let i = 0; i < gato.length; i++) {
    console.log(gato[i]);
}


