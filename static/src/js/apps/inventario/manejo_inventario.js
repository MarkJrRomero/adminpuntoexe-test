const registrarInventario = async(tipo) => {

    let validacion = validarCamposMasivo(formularioRegistrarInventario)

    console.log(validacion)

    if(validacion){

        let producto = $('#producto').val()
        let cantidad = $('#cantidad').val()

    
        const data = new FormData()

        data.append("producto", producto)
        data.append("cantidad", cantidad)
        data.append("tipo", tipo)
        data.append("csrfmiddlewaretoken", csrftoken)
   



        try {
            
            const peticion = await fetch(registrarInventarioUrl, {
                method: "POST",
                body: data,
            });

            const respuesta = await peticion.json();
            console.log(respuesta);

            if(respuesta.success){

            
                Swal.fire({
                    icon: 'success',
                    title: 'Genial!!',
                    text: respuesta.msj,
                  })


                table.draw();
                $('#cantidad').val("")

            }else{
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: respuesta.msj,
                })
            }

           

            } catch (error) {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: error.toString(),
                })
            }
    }
}


$( "#sumar-inventario-btn" ).on( "click", function() {
    registrarInventario("suma");
});


$( "#restar-inventario-btn" ).on( "click", function() {
    registrarInventario("resta");
});