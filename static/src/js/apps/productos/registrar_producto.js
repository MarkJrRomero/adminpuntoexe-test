
const registrarProducto = async() => {

    let validacion = validarCamposMasivo(formularioRegistrarProducto)

    console.log(validacion)

    if(validacion){

        let descripcion = $('#descripcion').val()
        let referencia = $('#referencia').val()
        let proveedor = $('#proveedor').val()
        let costo_uni = $('#costo_uni').val()
    
        const data = new FormData()

        data.append("descripcion", descripcion)
        data.append("referencia", referencia)
        data.append("proveedor", proveedor)
        data.append("costo_uni", costo_uni)
        data.append("csrfmiddlewaretoken", csrftoken)



        try {
            
            const peticion = await fetch(registrarProductoUrl, {
                method: "POST",
                body: data,
            });

            const respuesta = await peticion.json();
            console.log(respuesta);

            if(respuesta.success){

                Swal.fire({
                    position: 'top-end',
                    icon: 'success',
                    title: respuesta.msj,
                    showConfirmButton: false,
                    timer: 1500
                })

                $('#form-registrar-producto')[0].reset()


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
