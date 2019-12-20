const menu = document.querySelector(".menu")
const navHidden = document.querySelector(".nav-overlay")
const back = document.querySelector(".backBtn")



const menuSan = () => {
    console.log("menuuuuu")
    navHidden.classList.add("show")
}

menu.addEventListener("click", menuSan)


const backSan = () => {
    console.log("backkkk")
    navHidden.classList.remove("show")
}

back.addEventListener("click", backSan)