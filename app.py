#!/usr/bin/env python3
"""Command-line entry point for the Lab 3 network inventory."""

from netinventory import Device, Inventory, connection_message


def build_inventory() -> Inventory:
    """Create and return the small training inventory."""
    inventory = Inventory()
    inventory.add(Device("edge-r1", "192.0.2.10", "router", "iosxe"))
    inventory.add(Device("access-sw1", "192.0.2.21", "switch", "iosxe"))
    inventory.add(Device("lab-fw1", "192.0.2.30", "firewall", "ftd", False))
    return inventory


def main() -> int:
    """Display the enabled devices in the training inventory."""
    inventory = build_inventory()
    print(f"Inventory devices: {len(inventory)}")
    for device in inventory.enabled():
        print(f"- {device.label()}")
        print(f"  {connection_message(device.name, device.management_ip)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
