let tot_webhits = 0;

document.addEventListener("DOMContentLoaded", function () {
  tot_webhits = tot_webhits + 1;
  document.getElementById("webhits").innerHTML = tot_webhits;
});
