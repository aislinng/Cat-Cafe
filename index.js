function darkmode() {
    document.getElementsByTagName("body")[0].style.backgroundColor = "#000000";
    elements = document.getElementsByClassName("seccion");
    for (var i = 0; i < elements.length; i++) {
        elements[i].style.backgroundColor = "#000000";
        elements[i].style.color = "#ffebcd";
    }
    document.getElementById("encabezado").style.color = "#grey";
    document.getElementById("encabezado").style.backgroundColor = "#black";
    console.log("dark mode");
}

function mostrarDescripcion(id) {
    var descripcion = document.getElementById(id);
    if (descripcion.style.display === "none") {
        descripcion.style.display = "block";
    } else {
        descripcion.style.display = "none";
    }
}

function mostrarMenu(dia) {
    var menus = document.getElementsByClassName('menu');
    for (var i = 0; i < menus.length; i++) {
        menus[i].style.display = "none";
    }

    var menuDia = document.getElementById(dia);
    menuDia.style.display = "block";
}
