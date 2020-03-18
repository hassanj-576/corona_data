import requests
from bs4 import BeautifulSoup


def parse_data():
    response = requests.get('https://www.worldometers.info/coronavirus/')
    html = str(response.content)
    soup = BeautifulSoup(html, 'html.parser')
    all_country_data = {}
    for tr in soup.find('table', id="main_table_countries").findAll('tr'):
        country_data = {}
        tds = tr.findAll('td')
        if len(tds) > 0:
            country_data['total_cases'] = int(tds[1].get_text().replace(',', '').strip() or 0)
            country_data['new_cases'] = int(
                tds[2].get_text().replace(',', '').replace('+', '').replace('-', '').strip() or 0)
            country_data['total_deaths'] = int(tds[3].get_text().replace(',', '').strip() or 0)
            country_data['new_deaths'] = int(
                tds[4].get_text().replace(',', '').replace('+', '').replace('-', '').strip() or 0)
            country_data['total_recovered'] = int(tds[5].get_text().replace(',', '').strip() or 0)
            country_data['active_cases'] = int(tds[6].get_text().replace(',', '').strip() or 0)
            all_country_data[tds[0].get_text().strip().lower()] = country_data
    return all_country_data
