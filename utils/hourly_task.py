import arrow

from utils.aggregator import aggregate_data
from utils.data import get_previous_all_data, store_aggregated_data_in_db, store_json_data_in_db
from utils.parser import parse_data


def hourly_task():
    pass
    current_time = arrow.utcnow().floor('hour').strftime('%Y-%m-%d %H:%M:%S')
    previous_time = arrow.utcnow().floor('hour').shift(hours=-1).strftime('%Y-%m-%d %H:%M:%S')
    current_country_data = parse_data()
    previous_country_data = get_previous_all_data(previous_time)
    aggregated_data = aggregate_data(current_country_data, previous_country_data, current_time)
    store_aggregated_data_in_db(aggregated_data)
    store_json_data_in_db(current_country_data, current_time)
