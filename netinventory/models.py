"""Classes that represent network inventory objects."""

import ipaddress

from .formatters import format_device_label


class Device:
    """Represent one network device and its basic properties."""

    def __init__(
        self,
        name: str,
        management_ip: str,
        role: str,
        platform: str = "unknown",
        enabled: bool = True,
    ) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Device name is required")
        if not isinstance(role, str) or not role.strip():
            raise ValueError("Device role is required")
        if not isinstance(enabled, bool):
            raise TypeError("enabled must be a Boolean")

        self.name = name.strip()
        self.management_ip = str(ipaddress.ip_address(management_ip))
        self.role = role.strip()
        self.platform = platform.strip()
        self.enabled = enabled

    def label(self) -> str:
        """Return a readable label for this device."""
        return format_device_label(self.name, self.role)

    def disable(self) -> None:
        """Mark this device as unavailable for automation."""
        self.enabled = False
    def __repr__(self) -> str:
        """Return a developer-oriented representation of this object."""
        return (
    f"Device(name={self.name!r}, management_ip={self.management_ip!r}, "
    f"role={self.role!r}, platform={self.platform!r}, "
    f"enabled={self.enabled!r})"
)