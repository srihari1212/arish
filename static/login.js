var toggleButton = document.querySelector(".toggle-button");
var backdrop = document.querySelector(".backdrop");
var mobileNav = document.querySelector(".mobile-nav");
toggleButton.addEventListener("click", function () {
  // mobileNav.style.display = 'block';
  // backdrop.style.display = 'block';
  mobileNav.classList.add("open");
  backdrop.classList.add("open");
});

function closemodal(){
      backdrop.classList.remove("open");
}

backdrop.addEventListener("click", function () {
  // mobileNav.style.display = 'none';
  mobileNav.classList.remove("open");
    closemodal()
});