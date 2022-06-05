import requests
import os
import csv
import json
from datetime import datetime


def collect_data():
    # В случае, если используется proxy, добавьте env-файл параметры своего proxy-сервера
    # догин, пароль, после @ введите ip proxy-сервера
    # proxies = {
    #     'https': f'http://{os.getenv("LOGIN")}:{os.getenv("PASSWORD")}@127.0.0.1:8000'
    # }
    t_date = datetime.now().strftime('%d_%m_%Y')

    # При использовании proxy, добавьте аргумент proxies=proxies в requests.get переменной response ниже
    response = requests.get(url='https://www.lifetime.plus/api/analysis2')

    with open(f'info_{t_date}.json', 'w', encoding='utf-8') as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)

def main():
    collect_data()


if __name__ == '__main__':
    main()