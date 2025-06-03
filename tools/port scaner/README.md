## Port Scanner
- **Features**:
  - Multi-threaded for speed (adjustable thread count).
  - Service detection using `getservbyport`.
  - Supports IP ranges and custom port lists.
- **Usage**:
  ```bash
  python port_scanner.py
  Enter target IP/hostname: example.com
  Enter ports: 1-1000  # Or specify 80,443,22