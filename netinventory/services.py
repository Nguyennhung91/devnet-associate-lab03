"""Inventory services that work with Device objects."""

from .models import Device


class Inventory:
    """Store a collection of Device objects and provide useful searches."""

    def __init__(self, devices: list[Device] | None = None) -> None:
        self._devices = list(devices) if devices is not None else []
    def add(self, device: Device) -> None:
        if not isinstance(device, Device):
           raise TypeError("Inventory accepts Device objects only")
        if any(existing.name == device.name for existing in self._devices):
           raise ValueError(f"Duplicate device name: {device.name}")
        self._devices.append(device)

    def enabled(self) -> list[Device]:
        return [device for device in self._devices if device.enabled]

    def by_role(self, role: str) -> list[Device]:
        return [device for device in self._devices if device.role == role]
    def __len__(self) -> int:
        return len(self._devices)