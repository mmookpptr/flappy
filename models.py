class Player:

    GRAVITY = 1
    STARTING_VELOCITY = 15
    JUMPING_VELOCITY = 15

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.vy = Player.STARTING_VELOCITY

    def update(self, delta):
        self.y += self.vy
        self.vy -= Player.GRAVITY

    def jump(self):
        self.vy = Player.JUMPING_VELOCITY


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.player = Player(self, width // 2, height // 2)

    def update(self, delta):
        self.player.update(delta)

    def on_key_press(self, key, key_modifiers):
        self.player.jump()
