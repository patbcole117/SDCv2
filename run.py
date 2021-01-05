from app import app
from app.utils.conf_parse import get_config
from app.utils.sql import sql_queries

if __name__=='__main__':
    c = get_config()
    if c['SDC_SQL_DROP'] == 'true':
        sql_queries.drop_database(c['SDC_SQL_DB'])
        sql_queries.create_database(c['SDC_SQL_DB'])
        sql_queries.create_fighter_table()
        sql_queries.create_bout_table()
    app.run(debug=False, host=c['SUI_HOST'], port=c['SUI_PORT'])