import requests
import time
from datetime import datetime

url = "http://localhost:5500/Xciell/EVRs/DDEg/commit/det/fiielwq"


def send_request():
    cur_time = datetime.now().strftime("%d-%m-%Y_%H:%M")
    try:
        response = requests.get(url)
        # You can check the response status code or content if needed
        print(f"{cur_time} Request sent. Status code: {response.status_code}", end="\n\n")
    except requests.RequestException as e:
        print(f"{cur_time} Error sending request: {e}", end="\n\n")


if __name__ == "__main__":
    time.sleep(10)
    while True:
        send_request()
        time.sleep(15)
