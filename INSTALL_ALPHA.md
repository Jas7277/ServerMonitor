# Server Monitor - Alpha Installation Guide

This is an **alpha version (1.0.0a)** for testing purposes.

## Quick Install (Recommended for Testers)

### Method 1: Install directly from GitHub (Easiest)

```bash
pip install git+https://github.com/yourusername/ServerMonitor.git@v1.0.0a
```

### Method 2: Install with pipx (Isolated environment)

```bash
# Install pipx if you don't have it
pip install --user pipx
pipx ensurepath

# Install server-monitor
pipx install git+https://github.com/yourusername/ServerMonitor.git@v1.0.0a
```

### Method 3: Clone and install in development mode

```bash
git clone https://github.com/yourusername/ServerMonitor.git
cd ServerMonitor
git checkout v1.0.0a
pip install -e .
```

## Running the Server Monitor

After installation, run:

```bash
server-monitor
```

Or with custom settings:

```bash
export MONITOR_HOST="0.0.0.0"
export MONITOR_PORT=8000
server-monitor
```

Access the dashboard at: http://localhost:8000/

## Testing Endpoints

### Check metrics (JSON):
```bash
curl http://localhost:8000/metrics | python -m json.tool
```

### Health check:
```bash
curl http://localhost:8000/ping
```

## Uninstall

```bash
pip uninstall server-monitor
# or if using pipx:
pipx uninstall server-monitor
```

## Report Issues

Please report any bugs or issues to: https://github.com/yourusername/ServerMonitor/issues

Include:
- Your OS and Python version
- Steps to reproduce
- Error messages or unexpected behavior
