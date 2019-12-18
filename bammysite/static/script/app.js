const menu = document.querySelector(".menu")
const navHidden = document.querySelector(".nav-overlay")
const back = document.querySelector(".back")



const menuSan = () => {
    console.log("menuuuuu")
    navHidden.classList.add("wassa")
}

menu.addEventListener("click", menuSan)


const backSan = () => {
    console.log("backkkk")
    navHidden.classList.remove("wassa")
}

back.addEventListener("click", backSan)