from sqlalchemy import func
from sqlalchemy.dialects.postgresql import insert


from models import db, Country_json_data, Country_data


def get_previous_all_data(previous_time):
    query = db.session.query(Country_json_data.country, Country_json_data.json_data).filter(
        Country_json_data.time == previous_time)
    myresult = query.all()
    all_country_previous_data = {}
    if len(myresult) == 0:
        return None
    for result in myresult:
        all_country_previous_data[result[0]] = result[1]

    return all_country_previous_data


def store_aggregated_data_in_db(country_aggregated_data):
    for country_data_dict in country_aggregated_data:
        country_data = Country_data(**country_data_dict)
        print("Inserting Data for country: ", country_data.country)
        db.session.add(country_data)
    db.session.commit()


def store_json_data_in_db(current_data, time):
    for country, data in current_data.items():
        insert_stmt = insert(Country_json_data).values(
            country=country,
            time=time,
            json_data=data)

        on_duplicate_key_stmt = insert_stmt.on_conflict_do_update(
            time=time,
            json_data=data
        )

        db.engine.execute(on_duplicate_key_stmt)
    pass


def get_country_latest_data(country):
    return db.session.query(Country_json_data.json_data).filter(Country_json_data.country == country).scalar()


def get_country_detail_data(country, start_time, end_time, trunc):
    query = db.session.query(
        func.date_trunc(trunc, Country_data.time).label('time'),
        func.sum(Country_data.hourly_new_cases).label('new_cases'),
        func.sum(Country_data.hourly_new_deaths).label('new_deaths'),
        func.sum(Country_data.hourly_new_recovered).label('new_recovered'),
        func.max(Country_data.total_deaths).label('total_deaths'),
        func.max(Country_data.total_cases).label('total_cases'),
        func.max(Country_data.total_recovered).label('total_recovered')) \
        .filter(
        Country_data.time >= start_time, Country_data.time <= end_time,
        Country_data.country == country
    ).group_by('time').order_by('time')
    return_list = []
    for result in query.all():
        return_list.append(result._asdict())
    return return_list
