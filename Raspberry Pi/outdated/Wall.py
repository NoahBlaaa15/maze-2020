class Wall:

    # victim_type = 'H' | 'S' | 'U' | True | None

    def __init__(self):
        self.victim_type = None

    def set_victim(self, tpe):
        self.victim_type = tpe

    def calculate_rescue_kits(self):
        x = self.victim_type
        if x:
            if x == 'H':
                return 2
            elif x == 'S' or True:
                return 1
            elif x == 'U':
                return 0
        else:
            return 0

    def get_victim(self):
        return [self.victim_type, self.calculate_rescue_kits()]
