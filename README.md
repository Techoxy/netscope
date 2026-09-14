# NetScope

Python-based network reconnaissance and TCP service analysis tool for authorized security testing and network experimentation.

NetScope is a hands-on project built to strengthen my understanding of computer networking, TCP behavior, Python socket programming, concurrency, and basic service identification.

---

## Features

- TCP port scanning
- Concurrent multi-port scanning
- Custom port specifications
- Port ranges and comma-separated ports
- Port specification validation
- Hostname and IPv4 resolution
- Connection latency measurement
- Basic service identification
  - HTTP
  - SSH
  - FTP
- Terminal output
- JSON output
- Configurable connection timeout
- Configurable worker count
- Automated test suite

---

## How It Works

NetScope follows a simple scanning and analysis pipeline:

```text
Target
  │
  ▼
Target Resolution
  │
  ▼
Port Specification
  │
  ▼
Concurrent TCP Scanning
  │
  ▼
Open Port Detection
  │
  ▼
Service Analysis
  │
  ├── HTTP Probe
  │
  └── Passive Banner Grab
          │
          ▼
   Service Identification
          │
          ▼
      Scan Results
          │
          ├── Terminal Output
          │
          └── JSON Output
```

The project is organized into separate modules for scanning, service analysis, target resolution, output formatting, and command-line handling.

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Techoxy/netscope.git
cd netscope
```

### Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

### Install NetScope

Install the project in editable mode:

```bash
pip install -e .
```

After installation, the `netscope` command is available directly from the environment.

Verify the installation:

```bash
netscope --help
```

---

## Usage

### Basic scan

```bash
netscope 127.0.0.1
```

By default, NetScope scans TCP ports `1-1024`.

### Scan a specific port

```bash
netscope 127.0.0.1 --ports 80
```

### Scan a port range

```bash
netscope 127.0.0.1 --ports 1-1024
```

### Scan multiple ports

```bash
netscope 127.0.0.1 --ports 22,80,443
```

### Combine ranges and individual ports

```bash
netscope 127.0.0.1 --ports 20-22,80,443
```

### Configure the connection timeout

```bash
netscope 127.0.0.1 --ports 80 --timeout 0.5
```

### Configure concurrent workers

```bash
netscope 127.0.0.1 --ports 1-1024 --workers 20
```

### JSON output

```bash
netscope 127.0.0.1 --ports 80,443 --format json
```

---

## Example Output

NetScope was tested against a controlled local environment containing three TCP services:

- HTTP on port 9001
- SSH-like test service on port 9002
- FTP-like test service on port 9003

Command:

```bash
netscope localhost --ports 9001-9003
```

Output:

```text
PORT   STATE   LATENCY      SERVICE   VERSION
--------------------------------------------------
9001  OPEN    0.16 ms      HTTP      SimpleHTTP/0.6 Python/3.14.6
9002  OPEN    3.08 ms      SSH       2.0
9003  OPEN    0.08 ms      FTP       -

Ports scanned: 3
Open ports:   3
Closed ports: 0
```

JSON output is also supported:

```bash
netscope localhost --ports 9001-9003 --format json
```

Example structure:

```json
[
  {
    "port": 9001,
    "is_open": true,
    "latency_ms": 0.234,
    "service": "HTTP",
    "version": "SimpleHTTP/0.6 Python/3.14.6"
  },
  {
    "port": 9002,
    "is_open": true,
    "latency_ms": 0.168,
    "service": "SSH",
    "version": "2.0"
  },
  {
    "port": 9003,
    "is_open": true,
    "latency_ms": 1.388,
    "service": "FTP",
    "version": null
  }
]
```

Latency values vary between runs and depend on the local environment.

```
---

## Service Detection

NetScope currently performs basic identification for several TCP services.

### HTTP

For HTTP services, NetScope sends a minimal `HEAD /` request and analyzes the response headers.

It can identify:

* HTTP response
* Server header
* Basic service information

### SSH

NetScope can identify SSH services from their protocol banner.

Example:

```text
SSH-2.0-NetScope-Test
```

### FTP

NetScope can identify FTP services from their initial server response.

Example:

```text
220 NetScope FTP Test Server
```

Service detection is intentionally lightweight and should not be considered equivalent to advanced service fingerprinting.

---

## Testing

NetScope includes an automated test suite covering the main components of the application.

Tests currently cover:

* TCP scanning
* Concurrent scanning
* Port specification parsing
* Port range handling
* Duplicate port handling
* Invalid port handling
* Target resolution
* HTTP identification
* SSH identification
* FTP identification
* Service detection
* Scan engine behavior
* Terminal output
* JSON output
* CLI argument parsing
* CLI validation
* Invalid timeout handling
* Invalid worker handling

Run the complete test suite:

```bash
pytest -q
```

Current test status:

```text
33 passed
```

---

## Project Structure

```text
netscope/
├── docs/
├── examples/
├── netscope/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── cli.py
│   ├── engine.py
│   ├── models.py
│   ├── output.py
│   ├── resolver.py
│   └── scanner.py
├── tests/
│   ├── test_analyzer.py
│   ├── test_cli.py
│   ├── test_engine.py
│   ├── test_output.py
│   ├── test_resolver.py
│   └── test_scanner.py
├── .gitignore
├── pyproject.toml
└── README.md
```

### Module Overview

| Module        | Responsibility                                            |
| ------------- | --------------------------------------------------------- |
| `scanner.py`  | TCP scanning, concurrency, and port specification parsing |
| `resolver.py` | Hostname and IPv4 address resolution                      |
| `analyzer.py` | Protocol probing and service identification               |
| `engine.py`   | Coordinates scanning and service analysis                 |
| `models.py`   | Structured result and service data models                 |
| `output.py`   | Terminal and JSON result formatting                       |
| `cli.py`      | Command-line interface and argument validation            |

---

## Design Focus

NetScope is primarily a learning and engineering project.

The goal is not to reproduce the feature set of established network scanners, but to understand how the underlying pieces work by implementing them directly in Python.

The project focuses on:

* TCP connection behavior
* Socket programming
* Concurrent network operations
* Hostname resolution
* Protocol responses
* Service identification
* CLI design
* Structured data models
* Modular software architecture
* Automated testing

Building these components from scratch provides a practical foundation for deeper work in networking and network security.

---

## Current Limitations

NetScope is intentionally a small reconnaissance and service-analysis tool.

It currently does not provide:

* UDP scanning
* Operating-system fingerprinting
* Advanced service fingerprinting
* Packet-level analysis
* Network stealth or evasion
* Vulnerability exploitation
* Credential attacks
* Brute-force functionality
* Exploit delivery
* IDS/IPS bypass techniques

These limitations are intentional for the current version.

NetScope is **not intended to replace established tools such as Nmap**.

---

## Responsible Use

NetScope should only be used against systems and networks where you have permission to perform security testing.

Appropriate targets include:

* Systems you own
* Systems where you have explicit authorization
* Local development environments
* Purpose-built security labs
* Training platforms where scanning is permitted

Do not use NetScope to scan systems or networks without authorization.

The project is designed around controlled security experimentation and responsible learning.

---

## Future Direction

Potential future development includes:

* Additional protocol-specific service detection
* Improved service fingerprinting
* Better scan reporting
* Expanded test coverage
* More example scenarios
* Additional network-security-oriented analysis

Future development will remain focused on understanding network behavior and security rather than turning NetScope into a general-purpose replacement for established scanners.

---

## Learning Objectives

Through NetScope, I am using practical implementation to strengthen my understanding of:

```text
Python
  ↓
Socket Programming
  ↓
TCP Networking
  ↓
Concurrent Network Operations
  ↓
Service Identification
  ↓
Network Reconnaissance
  ↓
Network Security
```

This project is part of my broader path toward deeper work in **network security and security research**.

---

## Author

**Amitesh Mondal**

Computer Science and Engineering (Cyber Security) student interested in:

* Computer Networking
* Network Security
* Linux
* Python
* Offensive Security
* Security Research

Long-term direction: **Network Security Research**
