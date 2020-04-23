import os
import time

import arrow
import requests
from bs4 import BeautifulSoup

from config import config


def parse_data():
    response = requests.get('https://www.worldometers.info/coronavirus/')
    html = str(response.content)
    soup = BeautifulSoup(html, 'html.parser')
    all_country_data = {}
    table = soup.find('table', id="main_table_countries_today")
    file_name = "table_" + str(time.time()) + ".html"
    file_path = os.path.join(config.RAW_TABLE_FOLDER, file_name)
    with open(file_path, "w") as file:
        file.write(str(table))
    for tr in table.findAll('tr'):
        if 'class' not in tr.attrs or 'total_row_world' not in tr.attrs['class']:
            country_data = {}
            tds = tr.findAll('td')
            if len(tds) > 0:
                country_data['total_cases'] = int(tds[1].get_text().replace(',', '').strip() or 0)
                country_data['new_cases'] = int(
                    tds[2].get_text().replace(',', '').replace('+', '').replace('-', '').strip() or 0)
                country_data['total_deaths'] = int(tds[3].get_text().replace(',', '').strip() or 0)
                country_data['new_deaths'] = int(
                    tds[4].get_text().replace(',', '').replace('+', '').replace('-', '').strip() or 0)
                if tds[5].get_text().replace(',', '').strip() != 'N/A':
                    country_data['total_recovered'] = int(tds[5].get_text().replace(',', '').strip() or 0)
                else:
                    country_data['total_recovered'] = int(0)

                country_data['active_cases'] = int(tds[6].get_text().replace(',', '').strip() or 0)
                country_data['total_tests'] = int(tds[10].get_text().replace(',', '').strip() or 0)
                all_country_data[tds[0].get_text().strip().lower()] = country_data
    return all_country_data


def parse_time(time):
    start_time = None
    end_time = arrow.utcnow().floor('hour')
    if time == 'day':
        start_time = end_time.shift(days=-1).datetime
        end_time = end_time.datetime
    if time == 'week':
        start_time = end_time.shift(days=-7).datetime
        end_time = end_time.datetime
    if time == 'month':
        start_time = end_time.shift(months=-1).datetime
        end_time = end_time.datetime

    return start_time, end_time


def parse_trunc(time):
    if time == 'day':
        return 'hour'
    return 'day'
