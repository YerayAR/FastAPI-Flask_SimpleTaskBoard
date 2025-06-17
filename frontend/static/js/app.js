async function loadTasks() {
    const apiUrl = document.body.dataset.api;
    const response = await fetch(`${apiUrl}/tasks/`);
    const data = await response.json();
    const container = document.getElementById('tasks');
    container.innerHTML = '';
    data.forEach(task => {
        const card = document.createElement('div');
        card.className = 'card mb-4';
        card.innerHTML = `
            <h3 class="text-xl neon">${task.title}</h3>
            <p>${task.description || ''}</p>
            <button class="button-primary mt-2" onclick="deleteTask(${task.id})">Delete</button>
        `;
        container.appendChild(card);
    });
}

async function createTask(evt) {
    evt.preventDefault();
    const apiUrl = document.body.dataset.api;
    const title = document.getElementById('title').value;
    const description = document.getElementById('description').value;
    const response = await fetch(`${apiUrl}/tasks/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, description })
    });
    if (response.ok) {
        notify('Task created');
        loadTasks();
        evt.target.reset();
    } else {
        notify('Error creating task');
    }
}

async function deleteTask(id) {
    const apiUrl = document.body.dataset.api;
    const response = await fetch(`${apiUrl}/tasks/${id}`, { method: 'DELETE' });
    if (response.status === 204) {
        notify('Task deleted');
        loadTasks();
    } else {
        notify('Error deleting task');
    }
}

function notify(msg) {
    const box = document.getElementById('notification');
    box.textContent = msg;
    box.classList.remove('hidden');
    setTimeout(() => box.classList.add('hidden'), 2000);
}

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('task-form').addEventListener('submit', createTask);
    loadTasks();
});
