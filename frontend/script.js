const togglebtn = document.getElementsByClassName("toggle-btn")[0]
const navbarlinks = document.getElementsByClassName("nav")[0]


togglebtn.addEventListener('click', () => {
    navbarlinks.classList.toggle('active')
})