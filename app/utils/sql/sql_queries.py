from app.utils.sql.sql_actions import execute_return_none, execute_return_all, execute_return_none_autocommit


def create_bout_table():
    q = '''CREATE TABLE IF NOT EXISTS bout
        (id SERIAL PRIMARY KEY NOT NULL,
        red_fighter TEXT REFERENCES fighter(name) NOT NULL,
        blue_fighter TEXT REFERENCES fighter(name) NOT NULL,
        red_bets INT NOT NULL,
        blue_bets INT NOT NULL,
        winner TEXT NOT NULL,
        bout_type TEXT NOT NULL,
        bout_date TEXT NOT NULL,
        was_upset BOOL NOT NULL
        );'''
    execute_return_none(q)
    print("CREATE TABLE BOUT")


def create_database():
    q = "CREATE DATABASE saltydata TEMPLATE template0;"
    execute_return_none_autocommit(q)
    print("CREATE DATABASE")


def create_fighter_table():
    q = '''CREATE TABLE IF NOT EXISTS fighter
        (id SERIAL PRIMARY KEY NOT NULL,
        name TEXT NOT NULL,
        wins INT NOT NULL,
        losses INT NOT NULL,
        total_bouts INT NOT NULL,
        elo REAL NOT NULL,
        num_upsets INT NOT NULL,
        current_streak INT NOT NULL,
        max_streak INT NOT NULL,
        date_of_last_bout TEXT NOT NULL,
        date_of_debut TEXT NOT NULL,
        UNIQUE(name));
        '''
    execute_return_none(q)
    print("CREATE TABLE FIGHTER")


def drop_database():
    q = "DROP DATABASE IF EXISTS saltydata;"
    execute_return_none_autocommit(q)
    print("DROP DATABASE")


def drop_table(table_name):
    q = "DROP TABLE IF EXISTS %s;"
    v = (table_name,)
    execute_return_none(q, v)
    print(f"DROP TABLE {table_name}")


def insert_bout(bout):
    q = "INSERT INTO bout (red_fighter, blue_fighter, red_bets, blue_bets, winner, bout_type, bout_date, was_upset) " \
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
    v = (bout.red_fighter, bout.blue_fighter, bout.red_bets, bout.blue_bets, bout.winner, bout.bout_type,
         bout.bout_date, bout.was_upset)
    execute_return_none(q, v)
    print(f"INSERT BOUT {bout.bout_date}")


def insert_fighter(fighter):
    q = "INSERT INTO fighter (name, wins, losses, total_bouts, elo, num_upsets, current_streak, max_streak, date_of_last_bout, date_of_debut)" \
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    v = (fighter.name, fighter.wins, fighter.losses, fighter.total_bouts, fighter.elo, fighter.current_streak,
         fighter.max_streak, fighter.num_upsets, fighter.date_of_last_bout, fighter.date_of_debut)
    execute_return_none(q, v)
    print(f"INSERT FIGHTER {fighter.name}")


def select_all_bouts():
    q = "SELECT * FROM bout;"
    r = execute_return_all(q)
    print(f"SELECT * FROM bout")
    return tup_to_dict("bout", r)


def select_all_fighters():
    q = "SELECT * FROM fighter;"
    r = execute_return_all(q)
    print(f"SELECT * FROM fighter")
    return tup_to_dict("fighter", r)


def select_all_fighters_where_name_is(value):
    q = f"SELECT * FROM fighter WHERE name = %s;"
    v = (value,)
    r = execute_return_all(q, v)
    print(f"SELECT fighters WHERE name: \'{value}\'")
    return tup_to_dict("fighter", r)


def select_one_fighter_where_name_is(value):
    q = f"SELECT * FROM fighter WHERE name = %s;"
    v = (value,)
    r = execute_return_all(q, v)
    print(f"SELECT fighter WHERE name: \'{value}\'")
    if tup_to_dict("fighter", r) is not None:
        return tup_to_dict("fighter", r)[0]
    else:
        return None


def select_table_metadata(table):
    q = "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = %s;"
    v = (table,)
    r = execute_return_all(q, v)
    l = []
    for k in r:
        l.append(k[0])
    return l


def tup_to_dict(table, items):
    if len(items) == 0:
        return None
    else:
        ld = []
        d = {}
        keys = select_table_metadata(table)
        for i in items:
            for idx in range(len(keys)):
                d[f"{keys[idx]}"] = i[idx]
            ld.append(d.copy())
        return ld


def update_fighter(fighter):
    q = "UPDATE fighter SET wins=%s, losses=%s, total_bouts=%s, elo=%s, num_upsets=%s, current_streak=%s, " \
        "max_streak=%s, date_of_last_bout=%s WHERE name=%s;"
    v = (fighter.wins, fighter.losses, fighter.total_bouts, fighter.elo, fighter.num_upsets, fighter.current_streak,
         fighter.max_streak, fighter.date_of_last_bout, fighter.name)
    execute_return_none(q,  v)
    print(f"UPDATE FIGHTER {fighter.name}")