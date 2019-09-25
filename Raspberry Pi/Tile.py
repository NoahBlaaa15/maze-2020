class Tile:
    global counter
    size = 50
    counter = 0

    def __init__(self, top, rgt, bot, lft):
        global counter
        self.id = counter + 1
        counter += 1

        self.x = None
        self.y = None
        self.z = None

        self.top = top
        if top is not None:
            self.top.bot = self

        self.rgt = rgt
        if rgt is not None:
            self.rgt.lft = self

        self.bot = bot
        if bot is not None:
            self.bot.top = self

        self.lft = lft
        if lft is not None:
            self.lft.rgt = self

        self.type = None
        self.visited = False
        self.neighbours = [self.top, self.rgt, self.bot, self.lft]

    def set_type(self, tpe):
        self.type = tpe

    def set_top(self, new):
        new.bot = self
        self.top = new

    def set_rgt(self, rgt):
        rgt.lft = self
        self.rgt = rgt

    def set_bot(self, bot):
        bot.top = self
        self.bot = bot

    def set_lft(self, lft):
        lft.rgt = self
        self.lft = lft

    def set_wall(self, orientation, status):
        if orientation == 'top':
            self.top = status
        if orientation == 'rgt':
            self.rgt = status
        if orientation == 'bot':
            self.bot = status
        if orientation == 'lft':
            self.lft = status
        # 0 = keine Wand
        # 1 = Wand

    def has_top(self):
        return self.top is not None

    def has_rgt(self):
        return self.rgt is not None

    def has_bot(self):
        return self.bot is not None

    def has_lft(self):
        return self.lft is not None

    def get_neighbours(self):
        return [self.top, self.rgt, self.bot, self.lft]

    def set_coordinates(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def get_coordinates(self):
        return [self.x, self.y, self.z]
