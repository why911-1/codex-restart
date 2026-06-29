const welcomeButton = document.querySelector("#welcomeButton");
const welcomeMessage = document.querySelector("#welcomeMessage");
const nameInput = document.querySelector("#nameInput");

welcomeButton.addEventListener("click", () => {
  const name = nameInput.value.trim() || "朋友";
  welcomeMessage.textContent = `欢迎你，${name}！欢迎来到我的网页`;
});
