from flask import Flask, render_template, request, jsonify
import requests
app = Flask(__name__)

servers = []

@app.route("/get_server_data")
def get_server_data():
    results = []
    for server in servers:
        try:
            server_url = server["ip"].rstrip('/')
            if not server_url.startswith('http://') and not server_url.startswith('https://'):
                server_url = 'http://' + server_url
            if ':' not in server_url.split('//')[-1]:
                server_url += ':8000'
            
            print(f"Fetching from: {server_url}/metrics")
            res = requests.get(f"{server_url}/metrics", timeout=5)
            if res.ok:
                metrics = res.json()
                results.append({
                    "name": server["name"],
                    "ip": server["ip"],
                    "cpu": metrics["cpu"],
                    "memory": metrics["memory"]["percent"],
                    "disk": metrics["disk"]["percent"],
                    "uptime": metrics["uptime"],
                })
            else:
                print(f"Server {server['name']} returned status {res.status_code}")
                results.append({
                    "name": server["name"],
                    "status": f"unreachable (HTTP {res.status_code})"
                })
        except Exception as e:
            print(f"Error fetching {server['name']}: {e}")
            results.append({
                "name": server["name"],
                "status": f"offline ({str(e)})"
            })
    return jsonify(results)
@app.route("/")
def dashboard():
    return render_template("dashboard.html", servers=servers)

@app.route("/add-server", methods=["POST"])
def add_server():
    data = request.get_json()
    servers.append({
        "name": data["name"],
        "ip": data["ip"],
        "notes": data.get("notes", ""),
        "cpu": 0,
        "memory": 0,
        "disk": 0,
        "uptime": "N/A",
        "online": True
    })
    return jsonify({"message": "Server added successfully!"}), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)