import os
import time
import subprocess
from pydbus import SystemBus

REMOTE_MAC = "ADD YOUR 88010 MAC ADDRESS HERE"  # your remote MAC
REMOTE_SCRIPT = "remote.py"       # script to launch after connect

bus = SystemBus()
adapter_path = "/org/bluez/hci0"
adapter = bus.get("org.bluez", adapter_path)

# Make sure bluetooth is powered on
print("Powering on Bluetooth...")
adapter.Powered = True

# Get object manager to find device
mngr = bus.get("org.bluez", "/")
devices = mngr.GetManagedObjects()

device_path = None

# Find device path if already known
for path, ifaces in devices.items():
    if "org.bluez.Device1" in ifaces:
        if ifaces["org.bluez.Device1"]["Address"] == REMOTE_MAC:
            device_path = path
            break

if not device_path:
    # Start discovery if device not found
    print("Scanning for device...")
    adapter.StartDiscovery()
    
    for _ in range(30):  # Scan for up to 30 seconds
        devices = mngr.GetManagedObjects()
        for path, ifaces in devices.items():
            if "org.bluez.Device1" in ifaces:
                if ifaces["org.bluez.Device1"]["Address"] == REMOTE_MAC:
                    device_path = path
                    break
        if device_path:
            break
        time.sleep(1)

    adapter.StopDiscovery()

if not device_path:
    print("Device not found.")
    exit(1)

print(f"Found device at {device_path}")

device = bus.get("org.bluez", device_path)

# Trust device
if not device.Trusted:
    print("Trusting device...")
    device.Trusted = True

# Pair if not already
if not device.Paired:
    print("Pairing device...")
    device.Pair()
    while not device.Paired:
        time.sleep(1)
    print("Paired!")

# Connect always (important)
if not device.Connected:
    print("Connecting to device...")
    device.Connect()
    while not device.Connected:
        time.sleep(1)
    print("Connected!")

print("LEGO Remote is ready. Launching remote.py...")

# Launch remote.py
subprocess.run(["python3", REMOTE_SCRIPT])
