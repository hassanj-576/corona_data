import arrow

from utils.aggregator import aggregate_data
from utils.data import get_previous_all_data, store_json_data_in_db, store_aggregated_data_in_db
from utils.database_connector import create_connection
from utils.parser import parse_data


def hourly_task():
    current_time = arrow.utcnow().floor('hour').strftime('%Y-%m-%d %H:%M:%S')
    previous_time = arrow.utcnow().floor('hour').shift(hours=-1).strftime('%Y-%m-%d %H:%M:%S')
    mydb, mycursor = create_connection()
    current_country_data = parse_data()
    previous_country_data = get_previous_all_data(current_time, mycursor)
    aggregated_data = aggregate_data(current_country_data, previous_country_data, current_time)
    store_aggregated_data_in_db(aggregated_data, mydb, mycursor)
    store_json_data_in_db(current_country_data, current_time, mydb, mycursor)
