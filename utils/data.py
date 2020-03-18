import json


def get_previous_all_data(previous_time, cursor):
    sql = "SELECT country,json_data FROM country_json_data WHERE  time = %s"
    cursor.execute(sql, (previous_time,))
    myresult = cursor.fetchall()
    all_country_previous_data = {}
    if len(myresult) == 0:
        return None
    for result in myresult:
        all_country_previous_data[result[0]] = json.loads(result[1])

    return all_country_previous_data


def store_aggregated_data_in_db(country_aggregated_data, mydb, cursor, ):
    for country_data in country_aggregated_data:
        print("Inserting Data for country")
        placeholders = ', '.join(['%s'] * len(country_data))
        columns = ', '.join(country_data.keys())
        sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % ('country_data', columns, placeholders)
        # valid in Python 3
        cursor.execute(sql, list(country_data.values()))
    mydb.commit()


def store_json_data_in_db(current_data, time, mydb, cursor):
    for country, data in current_data.items():
        sql = """
        INSERT INTO country_json_data (country, time, json_data)
        VALUES (%s,%s,%s)
        ON DUPLICATE KEY UPDATE time =%s, json_data =%s
        """
        val = (country, time, json.dumps(data), time, json.dumps(data))
        cursor.execute(sql, val)
    mydb.commit()
    pass
