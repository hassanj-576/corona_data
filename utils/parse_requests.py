from utils.data import get_country_latest_data, get_country_detail_data
from utils.parser import parse_time, parse_trunc


def get_latest_data_for_count(country):
    return get_country_latest_data(country)


def get_country_data_for_time(country: str, time: str):
    start_time, end_time = parse_time(time)
    trunc = parse_trunc(time)
    return get_country_detail_data(country, start_time, end_time, trunc)
