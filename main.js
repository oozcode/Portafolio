/*popup de servicios a agenda*/
document.addEventListener("DOMContentLoaded", () => {
  const modalElement = document.querySelector("#bootstrapModal");
  const modalTitle = modalElement.querySelector(".modal-title");
  const modalBody = modalElement.querySelector(".modal-body");

  const cartas = document.querySelectorAll(".carta");

  const modal = new bootstrap.Modal(modalElement);

  cartas.forEach(carta => {
      carta.addEventListener("click", () => {
          // Obtener el título y el texto personalizado de la carta clicada
          const titulo = carta.querySelector("h2").innerText;
          const mensaje = carta.getAttribute("data-mensaje");

          // Actualizar el título y el texto del modal con los datos obtenidos
          modalTitle.innerText = titulo;
          modalBody.innerText = mensaje;

          // Mostrar el modal
          modal.show();
      });
  });
});
