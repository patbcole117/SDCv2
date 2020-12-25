def calculate_elo(rank_winner, rank_loser, k=40):
    rw = 10**(rank_winner/400)
    rl = 10**(rank_loser/400)

    ew = rw/(rw+rl)
    el = rl/(rw+rl)

    rank_winner += k*(1-ew)
    rank_loser += k*(0-el)

    return {'winner': round(rank_winner, 2), 'loser': round(rank_loser, 2)}