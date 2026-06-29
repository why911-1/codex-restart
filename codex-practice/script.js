const welcomeButton = document.querySelector("#welcomeButton");
const welcomeMessage = document.querySelector("#welcomeMessage");
const nameInput = document.querySelector("#nameInput");

welcomeButton.addEventListener("click", () => {
  const name = nameInput.value.trim() || "朋友";
  welcomeMessage.textContent = `欢迎你，${name}！这是你用 Codex 做出的输入框互动。`;
});
