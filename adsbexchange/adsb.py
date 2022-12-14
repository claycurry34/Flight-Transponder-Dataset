from typing import List
from .connection.connectionmanager import ConnectionManager
from .persistence.airspace import Airspace

refresh_miliseconds = -1


class Adsbexchange:
    def __init__(self, start: bool) -> None:
        if start:
            self.conn = ConnectionManager()

    def add_airspace(self, airspace: Airspace):
        self.conn.add_airspace(airspace)
            
    def remove_airspace(self, airspace: Airspace):
        self.conn.remove_airspace(airspace)
    
    def list_airspaces(self):
        return self.conn.list_airspaces()


if __name__ == "__main__":
    print("hi")
