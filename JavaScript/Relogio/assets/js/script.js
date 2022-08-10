const li_hour = document.getElementsByTagName("li")[0];
const li_minute = document.getElementsByTagName("li")[1];
const li_second = document.getElementsByTagName("li")[2];


setInterval(() => {    
  let date = new Date();
  let hour = date.getHours();
  let minutes = date.getMinutes();
  let seconds = date.getSeconds();

  changeBack(5)

  if(seconds<10){seconds = '0'+seconds}
  if(hour<10){hour = '0'+ hour}
  if(minutes<10){minutes = '0'+ minutes}

  li_hour.textContent = hour;
  li_minute.textContent = minutes;
  li_second.textContent = seconds;

  li_hour.textContent = hour;
  li_minute.textContent = minutes;
  li_second.textContent = seconds;

  function changeBack(hours){
    let body = document.getElementsByTagName('body')[0];
    if(hours>=6 && hours<=12 ){
        body.classList.add("Dia")
        body.classList.remove("Tarde")
        body.classList.remove("Noite")
    }
    if(hours>=12 && hours<=18){
        body.classList.add("Tarde")
        body.classList.remove("Dia")
        body.classList.remove("Noite")
    }
    if(hours>18 && hours<6){
        body.classList.remove("Dia")
        body.classList.remove("Tarde")
    }
  }
});

