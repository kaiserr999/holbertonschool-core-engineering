const socket = new WebSocket("ws://localhost:8000/ws");
const status = document.getElementById("status");
const messages = document.getElementById("messages");
const input = document.getElementById("input");

socket.onopen = () => {
    status.textContent = "Connecté";
    status.className = "status connected";
};

socket.onclose = () => {
    status.textContent = "Déconnecté";
    status.className = "status disconnected";
};

socket.onmessage = (event) => {
    addMessage(event.data, "received");
};

function sendMessage() {
    const text = input.value.trim();
    if (!text || socket.readyState !== WebSocket.OPEN) return;
    addMessage(text, "sent");
    socket.send(text);
    input.value = "";
}

function addMessage(text, type) {
    const div = document.createElement("div");
    div.className = `message ${type}`;
    const now = new Date().toLocaleTimeString();
    div.innerHTML = `<div>${text}</div><div class="time">${now}</div>`;
    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
}

input.addEventListener("keydown", (e) => {
    if (e.key === "Enter") sendMessage();
});
