class Tile:

    def __init__(self, top, rgt, bot, lft, tpe):
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

        self.type = tpe

    def set_top(self, top):
        self.top = top
        self.top.set_bot(self)

    def set_rgt(self, rgt):
        self.rgt = rgt
        self.rgt.set_lft(self)

    def set_bot(self, bot):
        self.bot = bot
        self.bot.set_top(self)

    def set_lft(self, lft):
        self.lft = lft
        self.lft.set_rgt(self)

    def has_top(self):
        return self.top is not None

    def has_rgt(self):
        return self.rgt is not None

    def has_bot(self):
        return self.bot is not None

    def has_lft(self):
        return self.lft is not None
