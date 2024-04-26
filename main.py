import requests
from datetime import datetime
import time

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org')
        if response.status_code == 200:
            return response.text
        else:
            return "Failed to fetch"
    except requests.RequestException as e:
        return str(e)

def save_to_file(ip):
    now = datetime.now()
    current_date = now.strftime("%d/%m/%Y")
    current_time = now.strftime("%H:%M")

    with open("ip_log.txt", "r+") as file:
        # Check if the current date is different from the last logged date
        lines = file.readlines()
        if len(lines) == 0 or not lines[-1].startswith("["):
            file.write(f"[{current_date}]\n")
        else:
            last_line = lines[-1].strip()  # Read the last line (date)
            last_logged_date = last_line[1:-1]  # Extract date without brackets
            if last_logged_date != current_date:
                file.write(f"[{current_date}]\n")
        file.write(f"[{current_time}] {ip}\n")
    print("IP logged")

def main():
    while True:
        public_ip = get_public_ip()
        save_to_file(public_ip)
        time.sleep(60)  # Wait for 1 minute

if __name__ == "__main__":
    main()

