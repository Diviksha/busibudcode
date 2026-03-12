import $ from "jquery";

const rootApp = document.getElementById("root");

rootApp.innerHTML = "<button id='toggleBtn'>ON</button>";

rootApp.addEventListener("click", function (e) {
  if (e.target && e.target.id === "toggleBtn") {
    e.target.innerText = e.target.innerText === "ON" ? "OFF" : "ON";
  }
});
