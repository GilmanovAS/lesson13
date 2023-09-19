"""This is vacation DAO"""
import json


class VacanciesDAO:
    def __init__(self, path):
        self.path = path

    def get_all(self):
        with open(self.path, 'r', encoding='UTF-8') as fp:
            return json.load(fp)

    def get_by_position(self, position: str):
        position_return = []
        positions_all = self.get_all()
        for position_one in positions_all:
            if position.lower() in position_one['position'].lower():
                position_return.append(position_one)
        return position_return


