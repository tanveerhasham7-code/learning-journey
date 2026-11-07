"""Collect a minimal local system inventory for a lab report."""
import json
import platform
import socket
import sys
from datetime import datetime, timezone


def main() -> None:
    inventory = {
        "collected_utc": datetime.now(timezone.utc).isoformat(),
        "os": platform.system(),
        "os_release": platform.release(),
        "python_version": sys.version.split()[0],
        "hostname": socket.gethostname(),
        "note": "Review and sanitize host identifiers before publishing."
    }
    print(json.dumps(inventory, indent=2))


if __name__ == "__main__":
    main()
