def aggregate_data(current_country_data, previous_all_countries_data, time):
    if not previous_all_countries_data:
        previous_country_data = {
            'new_cases': 0,
            'new_deaths': 0,
            'total_recovered': 0,
            'total_cases': 0,
            'total_deaths': 0,
            'total_tests': 0

        }
    all_aggregated_data = []
    for country, country_data in current_country_data.items():
        if previous_all_countries_data and country in previous_all_countries_data:
            previous_country_data = previous_all_countries_data[country]
        country_aggregated_data = {
            'hourly_new_cases': country_data['total_cases'] - previous_country_data['total_cases'],
            'hourly_new_deaths': country_data['total_deaths'] - previous_country_data['total_deaths'],
            'hourly_new_recovered': country_data['total_recovered'] - previous_country_data['total_recovered'],
            'hourly_new_tests': country_data['total_tests'] - previous_country_data['total_tests'],
            'total_cases': country_data['total_cases'],
            'total_deaths': country_data['total_deaths'],
            'total_recovered': country_data['total_recovered'],
            'active_cases': country_data['active_cases'],
            'daily_new_cases': country_data['new_cases'],
            'daily_new_deaths': country_data['new_deaths'],
            'total_tests': country_data['total_tests'],
            'country': country,
            'time': time
        }
        all_aggregated_data.append(country_aggregated_data)

    return all_aggregated_data
