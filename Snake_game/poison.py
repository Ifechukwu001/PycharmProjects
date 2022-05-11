from food import Food


class Poison(Food):

    def __init__(self):
        super().__init__()
        self.color("red")