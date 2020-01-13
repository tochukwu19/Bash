const menu = document.querySelector(".menu")
const navHidden = document.querySelector(".nav-overlay")
const back = document.querySelector(".cancel")
const hamburger = document.querySelector('.hamburger');
const mobileNav = document.querySelector('.menubar');

//const menuSan = () => {
//navHidden.classList.add("show")
//}
//
//menu.addEventListener("click", menuSan);
//
//const backSan = () => {
// navHidden.classList.remove("show")
//}
//
//back.addEventListener("click", backSan)

hamburger.addEventListener("click",()=>{
navHidden.classList.remove("animate-out");
    hamburger.style.display = 'none';
navHidden.classList.add("animate-in")
    console.log('yes');
});

back.addEventListener("click",()=>{
    navHidden.classList.remove("animate-in");
   hamburger.style.display = 'block'; navHidden.classList.add("animate-out");
    
})