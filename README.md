# Web Honeypot

## Overview
This is a simple web honeypot designed to detect unauthorized login attempts and brute force attacks. It consists of a **frontend** (fake login page) and a **backend** (Flask server) that logs and detects suspicious activity.

## Features
- Fake login page to lure attackers
- Logs login attempts with IP addresses
- Detects brute force attacks (3+ attempts in 60 seconds)
- Alerts when suspicious activity is detected

## Installation
### **Prerequisites**
Ensure you have **Python 3** installed. Install dependencies using:
```bash
pip install flask
```

## Running the Honeypot
### **Start the Backend**
```bash
python honeypot.py
```
If port **5000** is in use, run it on a different port:
```bash
python honeypot.py --port 5001
```

### **Access the Frontend**
Once the backend is running, open your browser and go to:
```
http://127.0.0.1:5000/
```

## Stopping the Honeypot
To stop the backend server, press:
```bash
Ctrl + C
```
If running in the background, find and kill the process:
```bash
lsof -i :5000
kill -9 <PID>
```

## Logs
All login attempts and attack alerts are stored in `honeypot.log`.

## Future Improvements
- Implement email alerts for attack notifications
- Add IP blocking mechanism for repeated attacks

## Disclaimer
This honeypot is for educational and security research purposes only. Deploying it on a live network may have legal implications. Use responsibly!

---
Developed by **Rithika** 🚀

