class Card():
    def __init__(self, **kwargs):
        self.color = kwargs['color']
        self.number = kwargs['number']
        self.ability = kwargs['ability']
        