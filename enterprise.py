class Enterprise:

    def __init__(self, name: str):
        self.name : str = name
        self.max_power_level: int = 1000
        self.power_level:int = 1000
        self.max_population: int = 30
        self.population: int = 0
        self.max_shield_level: int = 100
        self.shield_level:int = 100

    def __str__(self):
        return "Welcome to the {}".format(self.name)

    def __repr__(self):
        return "NHLC Enterprise"