from app import app
from app.utils.conf_parse import get_config
from app.utils.sql import sql_queries

c = get_config()

if c["db_drop"]:
    sql_queries.drop_database(c["sql_db"])
    sql_queries.create_database(c["sql_db"])
    sql_queries.create_fighter_table()
    sql_queries.create_bout_table()

app.run(debug=False, host=c['l_addr'], port=c['l_port'])