function formatoPesoColombiano(numero) {
    return parseFloat(numero).toLocaleString('es-CO', {
      style: 'currency',
      currency: 'COP'
    });
}

function soloMayusculas(input) {
  if (typeof input.value === 'string') {
    input.value = input.value.toUpperCase();
  }
}


function soloNumeros(input) {
  input.value = input.value.replace(/[^\d]/g, '');
}



const ValidarForm = async(form) => {
  
  let valid = false;

  if(form == "terminar"){
    valid = validarCamposMasivo(formularioTerminar);
  }else if(form == "crear"){
    valid = validarCamposMasivo(formularioCrear);
  }else if(form == "info_conductor"){
    valid = validarCamposMasivo(formularioInfoConductor);
  }
  
  if (!valid) {
    return {
      "success": false,
      "msg": "Tienes algunos errores, Por favor verifica el formulario"
    }
  } else {
    return {
      "success": true,
      "msg": "Todos los campos son correctos"
    }
  }

}

const validarCamposMasivo = (arrayIds) => {
  let status = true;
  for (let i = 0; i < arrayIds.length; i++) {
      const id = arrayIds[i];
      if($(`#${id}`).val() == ''){
          $(`#${id}`).addClass("is-invalid");
          $(`#${id}`).attr("readonly", false)
          $(`#${id}`).attr("disabled", false)
          $(`#${id}`).removeClass("readOnly")
          status = false;
      }else{
          $(`#${id}`).removeClass("is-invalid");
      }
  }
  return status;
}

const validarCampo = (id) => {
  if($(`#${id}`).val() == ''){
      $(`#${id}`).addClass("is-invalid");
      return false;
  }else{
      $(`#${id}`).removeClass("is-invalid");
      return true;
  }
}


const validarOnChangeMasivo = (arrayIds) => {
  // console.log(arrayIds);
  for (let i = 0; i < arrayIds.length; i++) {
      const id = arrayIds[i];
      $(`#${id}`).attr('onchange', `validarCampo('${id}')`)
  }
}


const validarCampoRepiter = (input) => {

  let value = input.value ?? "";

  if(value == ''){
    $(`input[name='${input.name}']`).addClass("is-invalid");
  }else{
    $(`input[name='${input.name}']`).removeClass("is-invalid");
  }

}