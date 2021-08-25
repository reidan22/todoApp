const add_task_view = document.getElementById("account-tasks");
const button_bi_plus_square = document.querySelector("button-bi-plus-square");

button_bi_plus_square?.addEventListener('click',function(e){
    e.preventDefault();
    alert("OK");
    setTimeout(function(){add_task_view.scrollIntoView()
    }, 250);
  });