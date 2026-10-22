# WhatsApp Presence Tracker

A lightweight Python script using Selenium and WebDriver Manager to track and log the online/offline status of a specific WhatsApp contact in real-time.

## Features
- **Persistent Sessions:** Saves your login state locally so you don't need to scan the QR code on every run.
- **Activity Logging:** Automatically logs timestamped online and offline status changes into both the console and a `whatsapp_activity.log` file.

## Prerequisites
- Python 3.8+ installed on your system.
- Google Chrome browser installed.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/whatsapp-presence-tracker.git
   cd whatsapp-presence-tracker
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Open `whatsapp_tracker.py` and update the `TARGET_CONTACT` variable with the exact name of the chat contact you wish to monitor.
2. Run the script:
   ```bash
   python whatsapp_tracker.py
   ```
3. Scan the QR code with your phone when the browser window appears. 

## Disclaimer
This tool is for educational and personal automation purposes only. Excessive automated scraping or tracking can violate WhatsApp's Terms of Service and lead to account restrictions.
