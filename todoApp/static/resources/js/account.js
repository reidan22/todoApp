const button_bi_list = document.querySelector('.button-bi-list');
const button_bi_user_update = document.querySelector('.button-bi-user-update');
const button_bi_user_delete = document.querySelector('.button-bi-user-delete');

const add_task_view = document.querySelector(".account-tasks");
const button_bi_plus_square = document.querySelector(".button-bi-plus-square");

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
  // alert("OK")
  button_bi_list.classList.toggle("button-bi-list-on");
  button_bi_user_update.classList.toggle("button-bi-user");
  button_bi_user_delete.classList.toggle("button-bi-user");
  setTimeout(function(){
  }, 250);
});

// $(document).ready(function () {
//   // Handler for .ready() called.
//   $('html, body').animate({
//       scrollTop: $('#account-tasks').offset().top
//   }, 'slow');//w  w w.j a v a 2s.com
// });


// button_bi_plus_square?.addEventListener('click',function(e){
//   e.preventDefault();
//   setTimeout(function(){add_task_view.scrollIntoView()
//   }, 2000);
// });