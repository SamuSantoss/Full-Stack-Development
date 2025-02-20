function addTask() {
    let taskText = document.getElementById("taskInput").value;
    if (taskText === "") return;
    
    let li = document.createElement("li");
    let taskContainer = document.createElement("div");
    taskContainer.classList.add("task-container");
    
    let checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.onchange = function() {
        li.classList.toggle("completed");
    };
    
    let span = document.createElement("span");
    span.textContent = taskText;
    
    let removeButton = document.createElement("button");
    removeButton.textContent = "Remover";
    removeButton.classList.add("remove-button");
    removeButton.onclick = function() {
        li.remove();
    };
    
    taskContainer.appendChild(checkbox);
    taskContainer.appendChild(span);
    taskContainer.appendChild(removeButton);
    li.appendChild(taskContainer);
    document.getElementById("taskList").appendChild(li);
    document.getElementById("taskInput").value = "";
}