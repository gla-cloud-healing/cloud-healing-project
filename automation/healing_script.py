import subprocess
import requests
import time
import datetime

APP_URL = "http://localhost:5000/health"
CHECK_INTERVAL = 10
ALERT_LOG = "automation/alerts.log"

def log_alert(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] {message}"
    print(log_message)
    with open(ALERT_LOG, "a", encoding="utf-8") as f:
        f.write(log_message + "\n")

def check_app_health():
    try:
        response = requests.get(APP_URL, timeout=5)
        if response.status_code == 200:
            print(f"[OK] App is healthy - {datetime.datetime.now().strftime('%H:%M:%S')}")
            return True
        else:
            log_alert(f"[WARNING] App returned status code: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        log_alert("[DOWN] App is DOWN - Connection failed!")
        return False
    except requests.exceptions.Timeout:
        log_alert("[WARNING] App is slow - Request timed out!")
        return False

def restart_container():
    log_alert("[RESTART] Attempting to restart container...")
    try:
        subprocess.run(["docker", "restart", "my-app"], check=True)
        log_alert("[SUCCESS] Container restarted successfully!")
        time.sleep(5)
        return True
    except subprocess.CalledProcessError:
        log_alert("[FAILED] Failed to restart container!")
        return False

def main():
    log_alert("[START] Self-Healing Monitor Started!")
    failure_count = 0

    while True:
        is_healthy = check_app_health()

        if not is_healthy:
            failure_count += 1
            log_alert(f"[WARNING] Failure count: {failure_count}")

            if failure_count >= 2:
                log_alert("[CRITICAL] App failed 2 times - Triggering self-healing!")
                restarted = restart_container()

                if restarted:
                    failure_count = 0
                    log_alert("[SUCCESS] Self-healing successful!")
                else:
                    log_alert("[FAILED] Self-healing failed - Manual intervention needed!")
        else:
            failure_count = 0

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()

