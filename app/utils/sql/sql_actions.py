from app.utils.conf_parse import get_config
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import psycopg2


def get_default_connection():
    c = get_config()
    # print(f"Connecting to {c['sql_default_db']}")
    conn = psycopg2.connect(database=c['SDC_SQL_DEFAULT_DB'], user=c['SDC_SQL_USER'], password=c['SDC_SQL_SECRET'], host=c['SDC_SQL_HOST'],
                            port=c['SDC_SQL_PORT'])
    return conn


def get_connection():
    c = get_config()
    # print(f"Connecting to {c['sql_db']}")
    conn = psycopg2.connect(database=c['SDC_SQL_DB'], user=c['SDC_SQL_USER'], password=c['SDC_SQL_SECRET'], host=c['SDC_SQL_HOST'],
                            port=c['SDC_SQL_PORT'])
    return conn


def execute_return_all(query, values=None):
    con = get_connection()
    cur = con.cursor()
    # print(query, values)
    cur.execute(query, values)
    items = cur.fetchall()
    try:
        return items
    finally:
        con.close()


def execute_return_none(query, values=None):
    con = get_connection()
    cur = con.cursor()
    print(query, values)
    cur.execute(query, values)
    con.commit()
    con.close()


def execute_return_none_autocommit(query,  values=None):
    con = get_default_connection()
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()
    print(query, values)
    cur.execute(query, values)
    con.commit()
    con.close()