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
        self.type = 'standard'

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
    #Typisierung der Platte -> Standard, Black, Checkpoint, Debris, Ramp

    def set_top(self, new):
        new.bot = self
        self.top = new
        self.top.x = self.x
        self.top.y = self.y + 1
        self.top.z = self.z

    def set_rgt(self, rgt):
        rgt.lft = self
        self.rgt = rgt
        self.rgt.x = self.x + 1
        self.rgt.y = self.y
        self.rgt.z = self.z

    def set_bot(self, bot):
        bot.top = self
        self.bot = bot
        self.bot.x = self.x
        self.bot.y = self.y - 1
        self.bot.z = self.z

    def set_lft(self, lft):
        lft.rgt = self
        self.lft = lft
        self.lft.x = self.x - 1
        self.lft.y = self.y
        self.lft.z = self.z

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

    def __str__(self):
        return "Tile at " + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "."

    def __repr__(self):
        return "Tile at " + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "."
