let modal = document.getElementById("modal_psw");
let btn = document.getElementById("btn_rec_psw");
let span = document.getElementsByClassName("close")[0];

btn.addEventListener("click", function(){
    modal.style.display = "block";
});
span.addEventListener("click", function(){
    modal.style.display = "none";
})
window.addEventListener("click", function(event){
    if(event.target == modal){
        modal.style.display = "none";
    }
});