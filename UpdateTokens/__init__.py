import os

PG_CONN_INFO = {
    'host': os.environ.get('POSTGRESQL_HOST'),
    'port': os.environ.get('POSTGRESQL_PORT'),
    'user': os.environ.get('POSTGRESQL_USER'),
    'password': os.environ.get('POSTGRESQL_PASSWORD'),
    'database': os.environ.get('POSTGRESQL_DATABASE')
}

PLUGINS = {
    'salesforce': 1,
    'hubspot': 2,
    'google_analytics': 3,
    'xero': 4,
    'google_bigquery': 6
}
