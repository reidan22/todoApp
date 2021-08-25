const todo_bg = document.querySelector('.todo-bg');
const update_submit = document.querySelector('.todo-submit-register');


todo_bg?.addEventListener('click',function(e){
  e.preventDefault();
  todo_bg.style.opacity = "22%";
  todo_bg.style.transform = "translateY(-150%)";
  todo_bg.style.MozTransform = "translateY(-150%)";
  todo_bg.style.webkitTransform = "translateY(-150%)";
  setTimeout(function(){todo_bg.remove();}, 2000);
})

