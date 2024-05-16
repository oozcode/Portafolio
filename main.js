document.addEventListener("DOMContentLoaded", () => {
  const modalElement = document.querySelector("#bootstrapModal");
  const modalTitle = modalElement.querySelector(".modal-title");
  const modalBody = modalElement.querySelector(".modal-body");

  const cartas = document.querySelectorAll(".carta");

  const modal = new bootstrap.Modal(modalElement);

  cartas.forEach(carta => {
      carta.addEventListener("click", () => {
          // Obtiene el titulo al clickear
          const titulo = carta.querySelector("h2").innerText;
          const mensaje = carta.getAttribute("data-mensaje");

          // ACTUALIZA TEXTO 
          modalTitle.innerText = titulo;
          modalBody.innerText = mensaje;

          // Muestra el modal
          modal.show();
      });
  });
});

document.addEventListener("DOMContentLoaded", function() {
  var nombreInput = document.getElementById("name");
  var telefonoInput = document.getElementById("numero");
  var emailInput = document.getElementById("email");

  nombreInput.addEventListener("input", function() {
    validarNombre();
  });

  telefonoInput.addEventListener("input", function() {
    validarTelefono();
  });

  emailInput.addEventListener("input", function() {
    validarEmail();
  });

  // Funciones de validación
  function validarNombre() {
    var nombre = nombreInput.value.trim();
    if (nombre === "") {
      mostrarError(nombreInput, "Por favor, ingresa tu nombre.");
      return false;
    } else if (/\d/.test(nombre)) {
      mostrarError(nombreInput, "El nombre no puede contener números.");
      return false;
    } else {
      ocultarError(nombreInput);
      return true;
    }
  }

  function validarTelefono() {
    var telefono = telefonoInput.value.trim();
    if (telefono === "") {
      mostrarError(telefonoInput, "Por favor, ingresa tu número de teléfono.");
      return false;
    } else if (!/^\d{9}$/.test(telefono)) {
      mostrarError(telefonoInput, "Por favor, ingresa un número de teléfono válido (9 dígitos).");
      return false;
    } else {
      ocultarError(telefonoInput);
      return true;
    }
  }

  function validarEmail() {
    var email = emailInput.value.trim();
    if (email === "") {
      mostrarError(emailInput, "Por favor, ingresa tu email.");
      return false;
    } else if (!/^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/g.test(email)) {
      mostrarError(emailInput, "Por favor, ingresa un correo electrónico válido.");
      return false;
    } else {
      ocultarError(emailInput);
      return true;
    }
  }

  //ESTO SIRVE PARA MOSTRAR U OCULTAR LOS ERRORES , DISOCIACION TOTAL
  function mostrarError(input, mensaje) {
    var errorMensaje = input.nextElementSibling;
    errorMensaje.textContent = mensaje;
    errorMensaje.style.display = "block";
  }

  function ocultarError(input) {
    var errorMensaje = input.nextElementSibling;
    errorMensaje.textContent = "";
    errorMensaje.style.display = "none";
  }

  var submitButton = document.getElementById("submitButton");

  submitButton.addEventListener("click", function(event) {
    event.preventDefault(); //Espera a la validacion o0-
    
    console.log("Botón de envío clicado");
    if (validarFormulario()) {
      console.log("El formulario es válido. Enviar...");
      alert("¡Formulario enviado correctamente!");
      document.getElementById("formulario").reset();
    } else {
      console.log("El formulario no es válido. Mostrar alerta de error...");
      alert("Por favor, completa correctamente todos los campos antes de enviar el formulario.");
    }
  });

  // VALIDA FORMULARIO AAAAAA
  function validarFormulario() {
    console.log("Validando formulario...");
    var nombreValido = validarNombre();
    var telefonoValido = validarTelefono();
    var emailValido = validarEmail();

    return nombreValido && telefonoValido && emailValido;
  }
});
