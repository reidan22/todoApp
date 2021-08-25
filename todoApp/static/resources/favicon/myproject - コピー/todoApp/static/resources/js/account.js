const button_bi_list = document.querySelector('.button-bi-list');
const button_bi_user_update = document.querySelector('.button-bi-user-update');
const button_bi_user_delete = document.querySelector('.button-bi-user-delete');
let todo_bg_toggle = true;
const id_month = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC",]
const id_day = ["SUN","MON","TUE","WED","THU","FRI","SAT","SUN",]

var dt = new Date();
document.getElementById("id-account-year").innerHTML = dt.getFullYear();
document.getElementById("id-account-month").innerHTML = id_month[dt.getMonth()];
document.getElementById("id-account-day").innerHTML = id_day[dt.getDay()];
document.getElementById("id-account-date").innerHTML = dt.getDate();
document.getElementById("id-account-time").innerHTML = dt.toLocaleTimeString();

setInterval(function(){var dt = new Date();
    document.getElementById("id-account-year").innerHTML = dt.getFullYear();
    document.getElementById("id-account-month").innerHTML = id_month[dt.getMonth()];
    document.getElementById("id-account-day").innerHTML = id_day[dt.getDay()];
    document.getElementById("id-account-date").innerHTML = dt.getDate();
    document.getElementById("id-account-time").innerHTML = dt.toLocaleTimeString();
}, 1000);

button_bi_list?.addEventListener('click',function(e){
  e.preventDefault();

  button_bi_list.classList.toggle("button-bi-list-on");
  button_bi_user_update.classList.toggle("button-bi-user");
  button_bi_user_delete.classList.toggle("button-bi-user");
  setTimeout(function(){
  }, 250);
})
