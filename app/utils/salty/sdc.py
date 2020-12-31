from app.utils.salty.bout import Bout
from app.utils.salty.fighter import Fighter
from app.utils.sql import sql_queries


def calculate_elo(rank_winner, rank_loser, k=40):
    # print('CALCULATE ELO')
    rw = 10**(rank_winner/400)
    rl = 10**(rank_loser/400)

    ew = rw/(rw+rl)
    el = rl/(rw+rl)

    rank_winner += k*(1-ew)
    rank_loser += k*(0-el)

    return {'winner': round(rank_winner, 2), 'loser': round(rank_loser, 2)}


def handle_sbo_stream(sbo_stream):
    b = Bout(sbo_stream)
    fighters = [b.red_fighter, b.blue_fighter]
    for fighter in fighters:
        update_fighter_stats(b, fighter)
    update_fighter_elo(b)
    sql_queries.insert_bout(b)


def update_fighter_elo(bout):
    if bout.red_fighter == bout.winner:
        winner = Fighter(sql_queries.select_one_fighter_where_name_is(bout.red_fighter))
        loser = Fighter(sql_queries.select_one_fighter_where_name_is(bout.blue_fighter))
    else:
        winner = Fighter(sql_queries.select_one_fighter_where_name_is(bout.blue_fighter))
        loser = Fighter(sql_queries.select_one_fighter_where_name_is(bout.red_fighter))
    new_ranks = calculate_elo(winner.elo, loser.elo)
    winner.elo = new_ranks['winner']
    loser.elo = new_ranks['loser']
    sql_queries.update_fighter(winner)
    sql_queries.update_fighter(loser)


def update_fighter_stats(bout, fighter_name):
    fighter_dict = sql_queries.select_one_fighter_where_name_is(fighter_name)
    if fighter_dict is not None:
        fighter = Fighter(fighter_dict)
        if fighter.is_victor(bout):
            fighter.wins += 1
            fighter.current_streak += 1
            if fighter.current_streak > fighter.max_streak:
                fighter.max_streak = fighter.current_streak
            if bout.was_upset == "True":
                fighter.num_upsets += 1
        else:
            fighter.losses += 1
            fighter.current_streak = 0
        fighter.total_bouts += 1
        fighter.date_of_last_bout = bout.bout_date
        sql_queries.update_fighter(fighter)
    else:
        new_fighter = Fighter(fighter_name)
        new_fighter.date_of_debut = bout.bout_date
        sql_queries.insert_fighter(new_fighter)
        update_fighter_stats(bout, fighter_name)