/*popup de servicios a agenda*/
document.addEventListener("DOMContentLoaded", () => {
  const abrirmodal = document.querySelector("#agendar");
  const modalElement = document.querySelector("#bootstrapModal");
  const modal = new bootstrap.Modal(modalElement);

  if (abrirmodal) {
      abrirmodal.addEventListener("click", () => {
          modal.show();
      });
  }
});