function addContact() {
    let name = document.getElementById("nameInput").value;
    let phone = document.getElementById("phoneInput").value;
    let email = document.getElementById("emailInput").value;
    if (name === "" || phone === "") return;
    
    let li = document.createElement("li");
    let contactInfo = document.createElement("span");
    contactInfo.textContent = `${name} - ${phone} - ${email}`;
    
    let editButton = document.createElement("button");
    editButton.textContent = "Editar";
    editButton.classList.add("edit-button");
    editButton.onclick = function() {
        let newName = prompt("Novo nome:", name);
        let newPhone = prompt("Novo telefone:", phone);
        let newEmail = prompt("Novo e-mail:", email);
        if (newName && newPhone) {
            contactInfo.textContent = `${newName} - ${newPhone} - ${newEmail}`;
            name = newName;
            phone = newPhone;
            email = newEmail;
        }
    };
    
    let removeButton = document.createElement("button");
    removeButton.textContent = "Remover";
    removeButton.classList.add("remove-button");
    removeButton.onclick = function() {
        li.remove();
    };
    
    li.appendChild(contactInfo);
    li.appendChild(editButton);
    li.appendChild(removeButton);
    document.getElementById("contactList").appendChild(li);
    
    document.getElementById("nameInput").value = "";
    document.getElementById("phoneInput").value = "";
    document.getElementById("emailInput").value = "";
}