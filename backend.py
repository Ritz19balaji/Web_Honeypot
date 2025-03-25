from flask import Flask, request, jsonify, render_template
import logging
import time

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename="honeypot.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Store failed attempts per IP
attackers = {}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/log_attempt", methods=["POST"])
def log_attempt():
    data = request.json
    ip = request.remote_addr
    username = data.get("username")
    password = data.get("password")

    # Log attempt
    logging.info(f"Login Attempt - IP: {ip}, Username: {username}, Password: {password}")

    # Detect multiple attempts from the same IP
    if ip not in attackers:
        attackers[ip] = {"count": 1, "first_attempt": time.time()}
    else:
        attackers[ip]["count"] += 1

    # If more than 3 attempts in 60 seconds, mark as attack
    if attackers[ip]["count"] > 3 and (time.time() - attackers[ip]["first_attempt"] < 60):
        logging.warning(f"!!! Possible Brute Force Attack detected from {ip} !!!")
        return jsonify({"message": "Suspicious activity detected!"}), 403

    return jsonify({"message": "Login failed!"}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
