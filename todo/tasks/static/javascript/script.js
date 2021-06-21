//Get the button:
mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

// Dark mode

const switch_btn = document.getElementById("switch");
const mode = localStorage.getItem('theme');

if (mode){
  document.body.setAttribute("theme", mode);

  if (mode === 'dark'){
    switch_btn.checked = true;
  }
}

function switchMode(event){
  if (event.target.checked){
    document.body.setAttribute('theme', 'dark');
    localStorage.setItem('theme', 'dark');
  }
  else{
    document.body.setAttribute('theme', 'light');
    localStorage.setItem('theme', 'light');
  }
}

switch_btn.addEventListener('click', switchMode, false);


