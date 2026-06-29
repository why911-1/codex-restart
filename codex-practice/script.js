const welcomeButton = document.querySelector("#welcomeButton");
const welcomeMessage = document.querySelector("#welcomeMessage");
const nameInput = document.querySelector("#nameInput");
const clearButton = document.querySelector("#clearButton");
const todoInput = document.querySelector("#todoInput");
const addTodoButton = document.querySelector("#addTodoButton");
const todoList = document.querySelector("#todoList");
welcomeButton.addEventListener("click", () => {
  const name = nameInput.value.trim() || "朋友";
  welcomeMessage.textContent = `欢迎你，${name}！欢迎来到我的网页`;
});
clearButton.addEventListener("click", () => {
  nameInput.value = "";
  welcomeMessage.textContent = "";
});
addTodoButton.addEventListener("click", () => {
  const task = todoInput.value.trim();

  if (task === "") {
    return;
  }

  const item = document.createElement("li");
  item.className = "todo-item";

  item.innerHTML = `
    <input type="checkbox">
    <span class="todo-text">${task}</span>
    <button type="button" class="todo-delete">删除</button>
  `;
const checkbox = item.querySelector("input[type='checkbox']");

checkbox.addEventListener("change", () => {
  item.classList.toggle("completed", checkbox.checked);
});

const deleteButton = item.querySelector(".todo-delete");

deleteButton.addEventListener("click", () => {
  item.remove();
});

  todoList.appendChild(item);
  todoInput.value = "";
});
