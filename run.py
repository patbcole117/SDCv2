from app import app
from app.utils.conf_parse import get_config
from app.utils.sql import sql_queries

c = get_config()
if c['SDC_SQL_DROP'] == 'true':
        sql_queries.drop_database(c['SDC_SQL_DB'])
        sql_queries.create_database(c['SDC_SQL_DB'])
        sql_queries.create_fighter_table()
        sql_queries.create_bout_table()

if __name__=='__main__':
    app.run(debug=False, host=c['SDC_HOST'], port=c['SDC_PORT'])