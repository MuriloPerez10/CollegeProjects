const btn_dark = document.getElementById("btn-d");
const body = document.getElementsByTagName("body")[0];
const project = document.getElementsByClassName(".projects")[0];
const service = document.getElementsByClassName(".service")[0];

console.log(project)
function darkMode(){
    body.classList.toggle("dark-mode");
}

btn_dark.addEventListener('click',darkMode)