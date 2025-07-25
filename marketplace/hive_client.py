# appname/utils/hive.py

from django.conf import settings
from pyhive import hive

def get_hive_connection():
    return hive.Connection(
        host=settings.HIVE_CONFIG['host'],
        port=settings.HIVE_CONFIG['port'],
        username=settings.HIVE_CONFIG['username'],
        password=settings.HIVE_CONFIG['password'],
        database=settings.HIVE_CONFIG['database'],
        auth=settings.HIVE_CONFIG['auth'],
    )

def fetch_hive_data(limit=100):
    conn = get_hive_connection()
    cursor = conn.cursor()

    # 👇 Customize your Hive query here
    query = f"SELECT * FROM accounts LIMIT {limit}"
    cursor.execute(query)

    data = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    conn.close()

    return columns, data
