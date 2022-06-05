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

    # Для данных в json файле
    # with open(f'info_{t_date}.json', 'w', encoding='utf-8') as file:
    #     json.dump(response.json(), file, indent=4, ensure_ascii=False)


    categories = response.json()['categories']
    result = []

    for c in categories:
        c_name = c.get('name').strip()
        c_items = c.get('items')

        for item in c_items:
            item_name = item.get('name').strip()
            item_price = item.get('price')
            item_desc = item.get('description').strip()

        item_wt = item.get('days')
        item_bio = item.get('biomaterial')

        result.append(
            [c_name, item_name, item_bio, item_desc, item_price, item_wt]
        )

    with open(f'result_{t_date}.csv', 'a', encoding='utf-8') as file:
        writer = csv.writer(file)

        writer.writerow(
            (
                'Категория',
                'Анализ',
                'Биоматериал',
                'Описание',
                'Стоимость',
                'Готовность: дней'
            )
        )

        writer.writerows(
            result
        )

def main():
    collect_data()


if __name__ == '__main__':
    main()