"""Small reusable formatting functions for the network inventory."""


def format_device_label(name: str, role: str = "unknown") -> str:
    """Return a readable label containing a device name and role."""
    return f"{name.strip()} [{role.strip()}]"


def connection_message(name: str, address: str, port: int = 22) -> str:
    """Return a message describing a planned device connection."""
    return f"Connecting to {name.strip()} at {address.strip()}:{port}"
