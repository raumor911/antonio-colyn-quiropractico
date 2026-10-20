/* Menú adaptable: el enlace de WhatsApp funciona incluso sin JavaScript. */
const menu=document.querySelector(".menu"),nav=document.querySelector("#main-nav");
menu?.addEventListener("click",()=>{const open=menu.getAttribute("aria-expanded")!=="true";menu.setAttribute("aria-expanded",String(open));menu.setAttribute("aria-label",open?"Cerrar menú":"Abrir menú");nav?.classList.toggle("open",open)});
nav?.querySelectorAll("a").forEach(a=>a.addEventListener("click",()=>{nav.classList.remove("open");menu?.setAttribute("aria-expanded","false");menu?.setAttribute("aria-label","Abrir menú")}));

/* El mapa no solicita recursos de Google hasta aproximarse a la pantalla.
   El enlace externo de indicaciones funciona incluso sin JavaScript. */
const mapArea=document.getElementById("map-area");
const mapFrame=document.getElementById("mapa-consultorio");
const mapPreview=document.getElementById("map-preview");
const mapLoad=document.getElementById("map-load");
const showMap=()=>{
  if(!mapFrame || mapFrame.dataset.requested==="true")return;
  const src=mapFrame.getAttribute("data-src");
  if(!src)return;
  mapFrame.dataset.requested="true";
  mapFrame.addEventListener("load",()=>{
    mapArea?.classList.add("map-ready");
    if(mapPreview)mapPreview.hidden=true;
  },{once:true});
  mapFrame.hidden=false;
  mapFrame.src=src;
};
mapLoad?.addEventListener("click",showMap);
if(mapArea && "IntersectionObserver" in window){
  const observer=new IntersectionObserver(entries=>{
    if(entries.some(entry=>entry.isIntersecting)){
      showMap();
      observer.disconnect();
    }
  },{rootMargin:"160px 0px",threshold:0});
  observer.observe(mapArea);
}
