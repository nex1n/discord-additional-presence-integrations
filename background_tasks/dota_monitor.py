import time
import requests
import psutil

CHECK_INTERVAL = 5  # секунд между проверками


def is_dota_running():
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] and proc.info['name'].lower() == "dota2.exe":
            return True
    return False

def main():
    dota_was_running = False
    while True:
        running = is_dota_running()
        if dota_was_running and not running:
            # Дота была запущена, но сейчас не запущена — отправляем запрос end_activity
            print("Dota2 не запущена, отправляем end_activity")
            try:
                url = 'http://localhost:2222/api/activity_end'
                payload = {'type': 'dota'}
                headers = {'Content-Type': 'application/json'}
                response = requests.post(url, json=payload, headers=headers)
            except Exception as e:
                print(f"Ошибка при отправке запроса: {e}")
        dota_was_running = running
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
