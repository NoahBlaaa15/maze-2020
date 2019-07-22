class Motor:

    enc_1 = 0
    enc_2 = 0

    def __init__(self, e, m):
        self.m = e
        self.m = m
        self.speed = 0              # 0 - 255
        self.direction = 0          # 0 = cw/r || 1 = ccw/l
        self.encoder_value = 0      # 0 - ???

    def get_encoder_value(self):
        return self.encoder_value

    def set_speed(self, x):
        self.speed = x

    def set_direction(self, x):
        if x == 1:
            self.direction = 1
        if x == 0:
            self.direction = 0

    def get_direction(self):
        return self.direction

    def stop(self):
        self.speed = 0

    def reverse(self):
        self.direction = not self.direction
