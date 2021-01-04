import json
import os

def get_config():
    config = {'SDC_HOST': os.getenv('SDC_HOST'), 'SDC_PORT': os.getenv('SDC_PORT'), 'SDC_SQL_HOST': os.getenv('SDC_SQL_HOST'), 'SDC_SQL_PORT': os.getenv('SDC_SQL_PORT'), 'SDC_SQL_USER': os.getenv('SDC_SQL_USER'), 'SDC_SQL_SECRET': os.getenv('SDC_SQL_SECRET'), 'SDC_SQL_DEFAULT_DB': os.getenv('SDC_SQL_DEFAULT_DB'), 'SDC_SQL_DB': os.getenv('SDC_SQL_DB'), 'SDC_SQL_DROP': os.getenv('SDC_SQL_DROP')}
    return config