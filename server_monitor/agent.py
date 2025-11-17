import psutil
import socket
import time
from datetime import datetime, timedelta, timezone
from flask import Flask, jsonify

app = Flask(__name__)
start_time = time.time()

def get_system_info():
    uptime_seconds = int(time.time() - start_time)
    uptime = str(timedelta(seconds=uptime_seconds))

    cpu_percent = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    net_io = psutil.net_io_counters()

    info = {
        "hostname": socket.gethostname(),
        "cpu": cpu_percent,
        "memory": {
            "percent": memory.percent,
            "used": round(memory.used / (1024**2), 2),
            "total": round(memory.total / (1024**2), 2),
        },
        "disk": {
            "percent": disk.percent,
            "used": round(disk.used / (1024**2), 2),
            "total": round(disk.total / (1024**2), 2)
        },
        "network": {
            "sent_MB": round(net_io.bytes_sent / (1024**2), 2),
            "recv_MB": round(net_io.bytes_recv / (1024**2), 2),
        },
        "uptime": uptime,
        "timestamp": datetime.now(tz=timezone.utc).isoformat() + "Z"
    }
    return info

@app.route("/metrics", methods=["GET"])
def metrics():
    return jsonify(get_system_info())

@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"status": "ok", "hostname": socket.gethostname()})

def main():
    app.run(host="0.0.0.0", port=8000, debug=False)

if __name__ == "__main__":
    main()