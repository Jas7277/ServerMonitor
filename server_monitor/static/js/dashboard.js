const refreshBtn = document.getElementById("refresh");
const addServerBtn = document.getElementById("add-server-btn");
const modal = document.getElementById("add-server-modal");
const overlay = document.getElementById("modal-overlay");
const cancelBtn = document.getElementById("cancel-add");
const form = document.getElementById("add-server-form");

addServerBtn.addEventListener("click", function() {
    modal.classList.remove("hidden");
    overlay.classList.remove("hidden");
});

cancelBtn.addEventListener("click", function() {
    modal.classList.remove("hidden");
    overlay.classList.remove("hidden");
    form.reset();
    location.reload();
});

overlay.addEventListener("click", function() {
   modal.classList.add("hidden");
   overlay.classList.add("hidden");
});

refreshBtn.addEventListener("click", function() {
    location.reload();
});

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const data = Object.fromEntries(new FormData(form));
    const res = await fetch("/add-server", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });

    if (res.ok) {
        modal.classList.add("hidden");
        overlay.classList.add("hidden");
        location.reload();
    }
});

async function loadServers() {
    const res = await fetch("/get_server_data");
    const data = await res.json();
    const container = document.getElementById("server-list");
    container.innerHTML = "";

    data.forEach((server) => {
        const card = document.createElement("div");
        card.className = "server-card";
        if (server.status) {
            card.innerHTML = `
                <h2>${server.name}</h2>
                <p><strong>IP:</strong> ${server.ip}</p>
                <p class="status offline">Status: ${server.status}</p>`;
        } else {
            card.innerHTML = `
                <h2>${server.name}</h2>
                <p><strong>IP:</strong> ${server.ip}</p>
                <div class="stats">
                    <div class="stat">
                        <label>CPU</label>
                        <div class="bar">
                            <div class="fill" style="width: ${server.cpu}%"></div>
                        </div>
                        <span>${server.cpu}%</span>
                    </div>
                    <div class="stat">
                        <label>Memory</label>
                        <div class="bar">
                            <div class="fill" style="width: ${server.memory}%"></div>
                        </div>
                        <span>${server.memory}%</span>
                    </div>
                    <div class="stat">
                        <label>Disk</label>
                        <div class="bar">
                            <div class="fill" style="width: ${server.disk}%"></div>
                        </div>
                        <span>${server.disk}%</span>
                    </div>
                </div>
                <p class="uptime">Uptime: ${server.uptime}</p>
                <p class="status online">Online</p>`;
        }

        container.append(card);
    })
}

setInterval(loadServers, 5000);
window.addEventListener("load", loadServers);