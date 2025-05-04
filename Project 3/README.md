Project 3 - Coming this summer, will leverage a Raspberry Pi and a Raspberry Pi Build HAT instead of a Lego Powered Hub. Same idea as project #2, with 2 locomotives working together but it will be direct instead of Bluetooth, the HATs support connection of up to 4 Powered Up connections unlike the Hubs which support only 2. Users going this route might need to invest in a $25 Powered Up extension cable for at least one of the motors.

![p5](https://raw.githubusercontent.com/antoinesylvia/dfw_metroplex_poweredup_train/main/Project%203/project3a.jpg)
![p6](https://raw.githubusercontent.com/antoinesylvia/dfw_metroplex_poweredup_train/main/Project%203/project3.jpg)
--------------
Lego Track Color Layout 

Yellow <--> Red <--> Blue <--> Green
--------------
2025:
Started working on the PoweredUp Train remote, 88010. Created two scripts (lego_pair_88010_remote.py & lego_test_88010_remote_buttons.py) that will help you connect a Lego 88010 remote to a Pi via Bluetooth. These scripts are using some old code and raw data from 2 years ago, in addition to assistance from ChatGPT 4o and these repos:
- https://github.com/larsgk/lego-handset/blob/main/lego-handset-driver.js
- https://github.com/DanieleBenedettelli/TechnicMoveHub/blob/main/LEGO%20Technic%2042176%20RC%20Handset%2088010.py
- https://github.com/pybricks/technical-info/blob/master/assigned-numbers.md

# LEGO 88010 Remote — Debugger and Button Parser

This script (lego_test_88010_remote_buttons.py) provides a simple Python script to connect to a LEGO 88010 Handset remote (also known as the Powered Up Remote) and read button presses using BLE (Bluetooth Low Energy).

---

## - How It Works

### 1️ - Connect to the Remote

- Scan or use a saved Bluetooth address to connect to the LEGO 88010 remote.
- Establish a BLE connection to the device.

### 2️ - Discover Services and Characteristics

- Verify correct **Service UUID** and **Characteristic UUID** exist.
- Print detected services for validation.

### 3️ - Enable Notifications (CRITICAL)

- Send `0x41` ("Port Input Format Setup") command.
- Enable notifications for both **Left (0x00)** and **Right (0x01)** ports.
- This tells the remote to notify the app when button states change.

### 4️ - Start Notifications

- Begin listening for button press and release notifications.
- BLE sends button state packets when buttons are pressed or released.

### 5️ - Handle Notifications

- Filter incoming BLE packets to detect button events.
- Decode and display which buttons are pressed or released.

| Value | Meaning          |
|-------|------------------|
| 0xFF  | Minus (pressed)  |
| 0x7F  | Center (neutral) |
| 0x01  | Plus (pressed)   |
| 0x00  | Released (no press) |

### 6️ - Display Button Events

- Button states are printed in a user-friendly format.
- Example output: `Button event: Left + (Plus)`

### 7️ - Clean Exit

- On exit (Ctrl+C), stop notifications and clean up.
- Disconnect from the remote safely.

---

## ✅ Summary

- LEGO 88010 requires **proper input format setup** using `0x41` before sending button events.
- **Both Left and Right ports** must be enabled for full button detection.
- Notifications provide raw data + parsed button states live during operation.

---

## - Additional Notes

- Tested and validated on LEGO 88010 (Handset / Powered Up Remote).
- Designed for use with Python and the `bleak` library.
- Includes debug mode for raw BLE packet inspection.

---

## -  Requirements

- Python 3.7+
- `bleak` library (`pip install bleak`)

```bash
pip install bleak

------------------------------
# LEGO 88010 Remote — OS Level Pair & Launch Helper

This helper script (lego_pair_88010_remote.py) automates pairing, trusting, and connecting to the LEGO 88010 Handset remote at the Bluetooth OS level before launching your main remote listening script.

This is needed because LEGO remotes must be properly paired and connected before they begin sending button press notifications.  
Without this step → `remote.py` will connect, but buttons **will not register**.

---

## - How It Works

### 1️ - Power On Bluetooth

- Turns on Bluetooth if disabled.

### 2️ - Find the LEGO Remote

- Checks if the remote is already saved in Bluetooth devices.
- If not found → Scans for up to 30 seconds to discover it.

### 3️ - Trust + Pair the Remote

- **Trusts the device** so it connects automatically next time.
- **Pairs the device** if not already paired.

> Pairing is essential — without pairing, the LEGO 88010 will NOT send button data.

### 4️ - Connect to the Remote

- Ensures the remote is connected before launching your main script.
- Keeps trying until connected.

### 5️ - Launch the Button Listener (`remote.py`)

- Once paired, trusted, and connected → runs `remote.py` which starts listening for button events.

---

## - When and How to Run This

- Run **this helper script** first whenever the remote is off or unpaired.
- If the LEGO remote has already been paired/trusted and powered on → this script will skip unnecessary steps and just ensure connection → then launch `remote.py`.

✅ **Recommended Usage**

- Each time you power cycle or re-pair the LEGO remote → run this script.
- If your remote stays paired and trusted → you may skip running this sometimes, but running it ensures proper connection and avoids bugs.

Requirements:

- pip install pydbus

