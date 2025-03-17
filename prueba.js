$(document).ready(function () {


    console.log(typeof jQuery);
    $("#btnLogin").click(function () {
        let usuario = $("#username").val();
        let password = $("#password").val();
        let sendInfo = JSON.stringify({ "usuario": usuario, "password": password });
    
        $.ajax({
            url: "http://127.0.0.1:5000/validar_usuario",
            type: "POST",
            data: sendInfo,
            contentType: "application/json", // Enviar como JSON
            success: function (data) {
                alert("Inicio de sesión exitoso: " + data.mensaje);
                $("#loginResult").text(data.mensaje);
            },
            error: function (xhr) {
                alert("Error: " + xhr.responseText);
                $("#loginResult").text("Error en el inicio de sesión.");
            }
        });
    });
    
    $(".btnMenu").click(function () {
        var dia = $(this).data("nombre");  // Obtener el valor de 'data_nombre'
    
        // Determinar el id del ul correspondiente basado en el valor de 'dia'
        var listaId = "#menuList" + 
            (dia == 1 ? "Lunes" : 
            dia == 2 ? "Martes" : 
            dia == 3 ? "Miercoles" : 
            dia == 4 ? "Jueves" : 
            dia == 5 ? "Viernes" : 
            dia == 6 ? "Sabado" : 
            "Domingo");
    
        // Realizar la petición con el parámetro correcto
        $.get("http://127.0.0.1:5000/menu?data=" + dia, function (data, status) {
            $(listaId).empty();
            console.log(data);
            data.forEach(item => {
    
                $(listaId).append(`<li>${item.alimento} - $${item.precio}</li>`);
            });
        });
    });

$(".btnGatos").click(function () {

    let nombreGato = $(this).data("nombre");
    var id = "#gato" + nombreGato;

    // Hacer la solicitud GET para obtener la información del gato
    $.get("http://127.0.0.1:5000/gatos/" + nombreGato, function (data, status) {
        $(id).empty();

        // Verificar si la respuesta contiene datos válidos
        if (data.error) {
            $(id).append(`<li>${data.error}</li>`);
        } else {
            // Mostrar el nombre y la descripción del gato
            $(id).append(`
                <p>${data.descripcion}</p>
            `);
        }
    });
});
 
     $(document).ready(function() {
    $(".imagen-gato").each(function() {
        // Obtener el nombre del gato desde el atributo data-nombre
        let nombreGato = $(this).data("nombre");

        // Construir la URL para obtener la imagen desde el backend
        let imgSrc = "http://127.0.0.1:5000/obtener_imagen/" + nombreGato;

        // Establecer la fuente de la imagen automáticamente
        $(this).attr("src", imgSrc);
    });
});




    $(".btnGatos").click(function () {
        // Obtener el nombre del gato desde el atributo 'data-nombre'
        let nombreGato = $(this).data("nombre");
    
        // Construir la URL para obtener la imagen
        let imgSrc = "http://127.0.0.1:5000/obtener_imagen/" + nombreGato;
    
        // Establecer la fuente de la imagen automáticamente
        $("#imagen").attr("src", imgSrc);
    });


    $("#btnTextos").click(function () {
        $.get("http://127.0.0.1:5000/textos", function (data, status) {
            alert("El estatus es: " + status);
            $("#textoSaludo").text("Saludo: " + data.saludo);
            $("#textoDespedida").text("Despedida: " + data.despedida);
        });
    });

});
