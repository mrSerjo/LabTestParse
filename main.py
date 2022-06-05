import requests
import os
import csv
import json
from datetime import date


def collect_data():
    # В случае, если используется proxy, добавьте env-файл параметры своего proxy-сервера
    # догин, пароль, после @ введите ip proxy-сервера
    # proxies = {
    #     'https': f'http://{os.getenv("LOGIN")}:{os.getenv("PASSWORD")}@127.0.0.1:8000'
    # }
    pass

def main():
    collect_data()


if __name__ == '__main__':
    main()