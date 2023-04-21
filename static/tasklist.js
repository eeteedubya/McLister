let tasks = [];

function addTask() {
  const input = document.getElementById('taskInput');
  const taskList = document.getElementById('taskList');

  if (input.value !== '') {
    tasks.push(input.value);
    input.value = '';

    const newTask = document.createElement('li');
    newTask.textContent = tasks[tasks.length - 1];
    taskList.appendChild(newTask);
  }
}

function removeTask() {
  const taskList = document.getElementById('taskList');
  taskList.removeChild(this);
  tasks.splice(tasks.indexOf(this.textContent), 1);
}

document.addEventListener('DOMContentLoaded', () => {
  const taskList = document.getElementById('taskList');

  taskList.addEventListener('click', function (e) {
    if (e.target.tagName === 'LI') {
      removeTask.call(e.target);
    }
  });
});
