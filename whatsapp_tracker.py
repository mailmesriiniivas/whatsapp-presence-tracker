import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Configuration
TARGET_CONTACT = "Target Contact Name"  # Exact contact name as saved in chat
LOG_FILE = "whatsapp_activity.log"

def setup_driver():
    options = Options()
    options.add_argument("user-data-dir=./whatsapp_session")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"
    print(log_entry.strip())
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)

def main():
    driver = setup_driver()
    driver.get("https://web.whatsapp.com")
    
    print("[*] Waiting for WhatsApp Web to load...")
    print("[*] Please scan the QR code on the browser window if prompted.")
    
    while True:
        try:
            driver.find_element(By.ID, "pane-side")
            print("[+] Successfully logged into WhatsApp Web!")
            break
        except Exception:
            time.sleep(3)

    print(f"[*] Searching for chat: {TARGET_CONTACT}")
    try:
        chat_box = driver.find_element(By.XPATH, f"//span[@title='{TARGET_CONTACT}']")
        chat_box.click()
        print(f"[+] Opened chat with {TARGET_CONTACT}")
    except Exception as e:
        print(f"[-] Could not find contact '{TARGET_CONTACT}'.")
        driver.quit()
        return

    last_status = "UNKNOWN"
    print(f"[*] Starting live presence monitor for {TARGET_CONTACT}...\n")

    while True:
        try:
            header_status = driver.find_element(By.CSSSelector, "header span._ao3e, header div._a1wx")
            status_text = header_status.text.lower()

            if "online" in status_text and last_status != "ONLINE":
                last_status = "ONLINE"
                log_event(f"{TARGET_CONTACT} is ONLINE")

            elif "online" not in status_text and last_status == "ONLINE":
                last_status = "OFFLINE"
                log_event(f"{TARGET_CONTACT} went OFFLINE")

        except Exception:
            pass

        time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Monitoring stopped by user. Exiting...")
