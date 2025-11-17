# Server Monitor

Lightweight Flask-based agent to monitor a server and expose current system metrics (CPU, memory, disk, network, uptime, etc.) via a JSON endpoint and a minimal auto-refreshing dashboard.

- JSON metrics: `GET /metrics`
- Health check: `GET /health`
- HTML dashboard: `GET /`
- Default Dashboard Port: `5000`
- Default Agent Port: `8000`

## Features
- CPU usage, logical/physical cores, load averages
- Memory usage, swap stats
- Disk usage for `/`
- Network I/O counters (bytes/packets)
- Process info for the running agent (PID, threads, RSS, open files)
- System uptime and app uptime
- Optional API key protection for `/metrics` and non-root routes

## Requirements
- Python 3.10+
- `psutil` requires appropriate system headers on some platforms. On Debian/Ubuntu ensure `python3-dev` and build tools are present if building from source.
- `flask` is required to run the necessary web interfaces.
## Quick start (development)
```bash
# From repo root
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .

# Optional: set an API key (recommended for remote access)
export MONITOR_API_KEY="change-me"
# Optional: change bind address/port
export MONITOR_HOST="0.0.0.0"
export MONITOR_PORT=5000

# Run
server-monitor
# or
python -m server_monitor
```
Navigate to http://localhost:5000/ for the dashboard.

- `GET /metrics` requires the header `X-API-Key: <key>` if `MONITOR_API_KEY` is set, or `?api_key=<key>` query.

Example curl:
```bash
curl -H "X-API-Key: $MONITOR_API_KEY" http://localhost:5000/metrics | jq
```

## Configuration (env vars)
- `MONITOR_HOST` (default `0.0.0.0`) – listen address.
- `MONITOR_PORT` (default `5000`) – listen port.
- `MONITOR_DEBUG` (default `false`) – Flask debug mode.
- `MONITOR_API_KEY` (unset by default) – if set, required for `/metrics` and other non-root routes.
- `MONITOR_TITLE` (default `Server Monitor`) – title shown on dashboard.

## Production tips
- For public networks, always set a strong `MONITOR_API_KEY` and restrict inbound traffic via firewall/VPC.
- Consider running behind a reverse proxy (nginx, Caddy) and enabling HTTPS.
- You can also serve with a WSGI server like `gunicorn`:
  ```bash
  pip install gunicorn
  gunicorn -w 2 -b 0.0.0.0:5000 'server_monitor.app:create_app()'
  ```

## Install as a systemd service (Linux)
Create or adjust a Python virtualenv for isolation, then use the sample unit below. An example unit file is included under `deploy/server-monitor.service`.

1) Copy and edit the unit file:
```bash
sudo mkdir -p /opt/server-monitor
sudo cp -r . /opt/server-monitor
sudo cp deploy/server-monitor.service /etc/systemd/system/server-monitor.service
sudo $EDITOR /etc/systemd/system/server-monitor.service
```
Update the paths, user, and environment variables as needed.

2) Reload and enable service:
```bash
sudo systemctl daemon-reload
sudo systemctl enable --now server-monitor
sudo systemctl status server-monitor -n 100
```

3) Test:
```bash
curl -H "X-API-Key: <your-key>" http://<host>:5000/metrics
```

## Directory structure
```
server_monitor/
  agent.py        # Flask app and routes for the managed server
  dashboard.py    # Flask app and routes for the dashboard web UI
  static/
    css/
       style.css
    js/
       dashboard.js
  templates/
    index.html    # Minimal dashboard
```

## License
MIT
