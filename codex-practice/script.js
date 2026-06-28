const welcomeButton = document.querySelector("#welcomeButton");
const welcomeMessage = document.querySelector("#welcomeMessage");

welcomeButton.addEventListener("click", () => {
  welcomeMessage.textContent = "欢迎你，王维！这是你用 Codex 做出的第一个网页互动。";
});
