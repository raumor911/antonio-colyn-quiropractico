/* Menú adaptable: el enlace de WhatsApp funciona incluso sin JavaScript. */
const menu=document.querySelector(".menu"),nav=document.querySelector("#main-nav");
menu?.addEventListener("click",()=>{const open=menu.getAttribute("aria-expanded")!=="true";menu.setAttribute("aria-expanded",String(open));menu.setAttribute("aria-label",open?"Cerrar menú":"Abrir menú");nav?.classList.toggle("open",open)});
nav?.querySelectorAll("a").forEach(a=>a.addEventListener("click",()=>{nav.classList.remove("open");menu?.setAttribute("aria-expanded","false");menu?.setAttribute("aria-label","Abrir menú")}));
