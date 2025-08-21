# 📡 Raspberry Pi Serial to Web Poster

This Python script runs on a Raspberry Pi (or any Linux system) and:

1. Reads incoming text data from a serial port (e.g. a USB-connected device such as a pager, sensor, or microcontroller).
2. Detects when the incoming data changes.
3. Saves each unique line to a local CSV log file.
4. Sends each unique line as an HTTP POST request to a remote web server for further processing.

---

## 🛠 Features

- ✅ Works with `/dev/serial/by-id/...` or `/dev/ttyUSB0`
- ✅ Filters out duplicate lines (only sends new data)
- ✅ Logs timestamped entries to `test_data.csv`
- ✅ Sends data to a remote PHP/HTTP endpoint via `requests.post()`
- ✅ Handles serial decoding issues gracefully
- ✅ Recovers from most runtime errors without crashing

---

## 🧰 Requirements

- Python 3.x
- Installed Python packages:
  ```bash
  pip install pyserial requests
