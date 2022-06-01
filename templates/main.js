/* JavaScript para dar efeito na troca de links*/
function backgroundWhite(x) {
    x.style.backgroundColor = "white"
}

function backgroundNormal(x) {
    x.style.backgroundColor = "initial"
}

/* codigo para abrir o modal de contato  - W3school*/

// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}


/* codigo para abrir o modal de criação de postagem no forum  - W3school*/

// Get the modal
var cadtopico = document.getElementById("addtopico");

// Get the button that opens the modal
var adicionaritem = document.getElementById("adicionaritem");

// Get the <span> element that closes the modal
var spanforum = document.getElementsByClassName("closeaddppost")[0];

// When the user clicks the button, open the modal 
adicionaritem.onclick = function() {
  cadtopico.style.display = "block";
}

// When the user clicks on <span> (x), close the cadtopico
spanforum.onclick = function() {
  cadtopico.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == cadtopico) {
    cadtopico.style.display = "none";
  }
}
