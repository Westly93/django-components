/* In a file called [project root]/components/calendar/script.js */
(function () {
  const buttons = document.querySelectorAll("button");
  buttons.forEach((button) => {
    button.addEventListener("click", (e) => {
      alert(button.textContent);
    });
  });
})();
