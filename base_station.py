from typing import List


class BaseStation:

    def __init__(self, name: str):
        self.name: str = name
        self.score: int = 30
        self.max_crew: int = 6
        self.crew: int = 0
        if type(name) is str:
            self.name: str = name
        else:
            raise ValueError('Station name should be a string')
        self.crew_members: List = []

    def __str__(self):
        return "Welcome to the {}".format(self.name)

    def __repr__(self):
        return "NHLC Enterprise base station"

class MedicalStation(BaseStation):

    def __init__(self,name: str):
        super().__init__(name=name)

    def __repr__(self):
        return "NHLC Enterprise Medical station"

class CommandStation(BaseStation):

    def __init__(self,name: str):
        super().__init__(name=name)

    def __repr__(self):
        return "NHLC Enterprise Command station"

class TacticalStation(BaseStation):

    def __init__(self,name: str):
        super().__init__(name=name)

    def __repr__(self):
        return "NHLC Enterprise Tactical station"

class ScienceStation(BaseStation):

    def __init__(self,name: str):
        super().__init__(name=name)

    def __repr__(self):
        return "NHLC Enterprise Science station"
