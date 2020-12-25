class Bout:
    def __init__(self, bout_data):
        if isinstance(bout_data, dict):
            self.initialize_from_dict(bout_data)
        else:
            self.raw = bout_data
            self.red_fighter = self.raw['p1name']
            self.blue_fighter = self.raw['p2name']
            self.red_bets = int(self.raw['p1total'].replace(',', ''))
            self.blue_bets = int(self.raw['p2total'].replace(',', ''))
            self.winner = 'WINNER NOT INITIALIZED'
            self.bout_type = 'BOUT TYPE NOT INITIALIZED'
            self.bout_date = self.raw['bout_date']
            self.was_upset = 'UPSET NOT INITIALIZED'

        self.initialize_bout_type()
        self.initialize_winner()
        self.initialize_upset()

    def compare(self, bout):
        if bout is not None:
            if self.red_fighter == bout.red_fighter and \
                    self.blue_fighter == bout.blue_fighter and \
                    self.red_bets == bout.red_bets and \
                    self.blue_bets == bout.blue_bets and \
                    self.winner == bout.winner and \
                    self.bout_type == bout.bout_type and \
                    self.was_upset == bout.was_upset:
                return True
        return False

    def initialize_bout_type(self):
        remaining = self.raw['remaining']
        alert = self.raw['alert']
        if 'bracket' in remaining or 'FINAL ROUND' in remaining or 'Exhibition mode start!' in alert:
            if 'Tournament mode start!' in alert:
                self.bout_type = 'NORMAL MATCHMAKING'
            else:
                self.bout_type = 'TOURNAMENT MODE'
        elif 'exhibition' in remaining:
            self.bout_type = 'EXHIBITION MODE'
        else:
            self.bout_type = 'NORMAL MATCHMAKING'

    def initialize_from_dict(self, bout_data):
        self.raw = bout_data
        self.red_fighter = self.raw['p1name']
        self.blue_fighter = self.raw['p2name']
        self.red_bets = int(self.raw['p1total'].replace(',', ''))
        self.blue_bets = int(self.raw['p2total'].replace(',', ''))
        self.winner = 'WINNER NOT INITIALIZED'
        self.bout_type = 'BOUT TYPE NOT INITIALIZED'
        self.bout_date = self.raw['bout_date']
        self.was_upset = 'UPSET NOT INITIALIZED'

    def initialize_upset(self):
        if self.red_bets > self.blue_bets and self.winner == self.blue_fighter:
            self.was_upset = 'True'
        elif self.blue_bets > self.red_bets and self.winner == self.red_fighter:
            self.was_upset = 'True'
        elif self.red_bets == self.blue_bets:
            self.was_upset = 'Tie'
        else:
            # print('UPSET NO')
            self.was_upset = 'False'

    def initialize_winner(self):
        if self.raw['status'] == '1':
            self.winner = self.red_fighter
        elif self.raw['status'] == '2':
            self.winner = self.blue_fighter

    def to_dict(self):
        return {
            'red_fighter': self.red_fighter,
            'blue_fighter': self.blue_fighter,
            'red_bets': self.red_bets,
            'blue_bets': self.blue_bets,
            'winner': self.winner,
            'bout_type': self.bout_type,
            'bout_date': self.bout_date,
            'was_upset': self.was_upset
        }