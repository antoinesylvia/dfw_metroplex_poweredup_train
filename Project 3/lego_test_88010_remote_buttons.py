import asyncio
import os
from bleak import BleakScanner, BleakClient

# File to save the previously discovered remote address (so next run is faster)
ADDRESS_FILE = "remote_address.txt"

# LEGO 88010 Handset Bluetooth GATT service and characteristic UUIDs
SERVICE_UUID = "00001623-1212-efde-1623-785feabcd123"  # Service UUID (Fixed)
CHAR_UUID = "00001624-1212-efde-1623-785feabcd123"    # Characteristic UUID for communication

# Port numbers used to identify left and right button groups on the remote
PORT_LEFT = 0x00
PORT_RIGHT = 0x01

# Keep track of last button states to avoid duplicate prints
last_button_states = {PORT_LEFT: None, PORT_RIGHT: None}

# Decode button signal values into human readable button events
def parse_button(port, value):
    if port == PORT_LEFT:
        side = "Left"
    elif port == PORT_RIGHT:
        side = "Right"
    else:
        side = "Unknown"

    # Button state decoding based on LEGO protocol (value byte meaning)
    if value == 0xFF:
        return f"{side} - (Minus)"
    elif value == 0x7F:
        return f"{side} (Center)"
    elif value == 0x01:
        return f"{side} + (Plus)"
    elif value == 0x00:
        return f"{side} Released"
    else:
        return f"{side} Unknown"

# Called whenever the remote sends a notification (button pressed, released, etc)
def notification_handler(sender, data):
    global last_button_states

    # Always print raw packet for debug visibility
    print(f"Raw data: {list(data)}")

    # LEGO handset sends button packets like:
    # [ 0x05, 0x00, 0x45, <port>, <button_value> ]
    if len(data) != 5 or data[0] != 0x05 or data[2] != 0x45:
        return  # Not a valid button packet → ignore

    port = data[3]
    value = data[4]

    # If button state changed, print it
    if last_button_states.get(port) != value:
        button_desc = parse_button(port, value)
        print("Button event:", button_desc)
        last_button_states[port] = value

# Send command to the LEGO handset telling it:
# "Send me notifications when button state changes on this port"
async def enable_port_notifications(client, port):
    print(f"Enabling notifications for port {port}...")

    # This is a "Port Input Format Setup (Single)" command → 0x41
    # It configures the remote to:
    # - Port: port (0x00 = Left, 0x01 = Right)
    # - Mode: 0x01 → "Simple Button Press Mode"
    # - Notifications Enabled: 0x01 → notify on changes
    setup = bytearray([
        0x0A,  # Length of packet
        0x00,  # Hub ID (not used here)
        0x41,  # Command: Port Input Format Setup (Single)
        port,  # Which port (Left or Right)
        0x01,  # Mode (simple button mode)
        0x01,  # Delta (change threshold, leave 1)
        0x00,  # Unit (ignored)
        0x00,  # Not used
        0x00,  # Not used
        0x01   # Enable notifications (1=on)
    ])
    await client.write_gatt_char(CHAR_UUID, setup)

# Main connection + listen logic
async def connect_and_listen(address):
    async with BleakClient(address, address_type="random") as client:
        print(f"Connected to remote [{address}]")

        # Confirm and print discovered GATT services and characteristics
        services = await client.get_services()
        print(f"Using UUID: {CHAR_UUID}")
        for service in services:
            print(f"Service: {service.uuid}")
            for char in service.characteristics:
                print(f"  Characteristic: {char.uuid}")

        # Enable notifications for both Left and Right ports → so remote sends button state changes
        await enable_port_notifications(client, PORT_LEFT)
        await enable_port_notifications(client, PORT_RIGHT)

        # Start listening to notifications from the remote
        await client.start_notify(CHAR_UUID, notification_handler)

        print("Listening for button presses. Press Ctrl+C to exit.")
        try:
            # Keep program running until user stops it
            while True:
                await asyncio.sleep(1)
        except KeyboardInterrupt:
            print("Stopping...")
        finally:
            # Stop notifications when exiting
            await client.stop_notify(CHAR_UUID)

# Bluetooth scanning logic to find the LEGO remote
async def scan_for_remote():
    print("Scanning for LEGO 88010 Remote...")
    devices = await BleakScanner.discover(timeout=10.0)

    for d in devices:
        if d.name and ("Handset" in d.name or "LEGO" in d.name):
            print(f"Found remote: {d.name} [{d.address}]")
            with open(ADDRESS_FILE, "w") as f:
                f.write(d.address)
            return d.address

    print("Remote not found.")
    return None

# Program entry point
async def main():
    address = None

    # Try loading saved address (from previous run)
    if os.path.exists(ADDRESS_FILE):
        with open(ADDRESS_FILE, "r") as f:
            address = f.read().strip()
        print(f"Trying saved address: {address}")

        try:
            await connect_and_listen(address)
            return
        except Exception as e:
            print(f"Failed to connect with saved address: {e}")

    # If saved address fails, scan for remote
    address = await scan_for_remote()

    if address:
        await connect_and_listen(address)
    else:
        print("Unable to find remote. Please turn it on and try again.")

if __name__ == "__main__":
    asyncio.run(main())
