/*popup de servicios*/
document.addEventListener("DOMContentLoaded", () => {
  const abrirmodal = document.querySelector("#agendar");
  const btncerrarmodal = document.querySelector("#btn-cerrar");
  const modal = document.querySelector("#modal");

  abrirmodal.addEventListener("click", () => {
      modal.showModal();
  });

  btncerrarmodal.addEventListener("click", () => {
      modal.close();
  });
});
