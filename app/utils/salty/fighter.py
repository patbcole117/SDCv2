class Fighter:
    def __init__(self, fighter_data):
        if isinstance(fighter_data, dict):
            self.initialize_from_dict(fighter_data)
        else:
            self.name = fighter_data
            self.wins = 0
            self.losses = 0
            self.total_bouts = 0
            self.elo = 2000.00
            self.num_upsets = 0
            self.current_streak = 0
            self.max_streak = 0
            self.date_of_last_bout = 'NO DATE'
            self.date_of_debut = 'NO DATE'

    def compare(self, fighter):
        if fighter is not None:
            if self.name == fighter.name and \
                    self.total_bouts == fighter.total_bouts and \
                    self.date_of_debut == fighter.date_of_debut:
                return True
        return False

    def initialize_from_dict(self, fighter_dict):
        self.name = fighter_dict["name"]
        self.wins = fighter_dict["wins"]
        self.losses = fighter_dict["losses"]
        self.total_bouts = fighter_dict["total_bouts"]
        self.elo = fighter_dict["elo"]
        self.num_upsets = fighter_dict["num_upsets"]
        self.current_streak = fighter_dict["current_streak"]
        self.max_streak = fighter_dict["max_streak"]
        self.date_of_last_bout = fighter_dict["date_of_last_bout"]
        self.date_of_debut = fighter_dict["date_of_debut"]

    def is_victor(self, bout):
        if self.name == bout.winner:
            return True
        else:
            return False

    def to_dict(self):
        return {
            'name': self.name,
            'wins': self.wins,
            'losses': self.losses,
            'total_bouts': self.total_bouts,
            'elo': self.elo,
            'num_upsets': self.num_upsets,
            'current_streak': self.current_streak,
            'max_streak': self.max_streak,
            'date_of_last_bout': self.date_of_last_bout,
            'date_of_debut': self.date_of_debut
        }