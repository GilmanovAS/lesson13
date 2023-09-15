import json


class CandidatesDAO:
    def __init__(self, path: str):
        self.path = path

    def get_all(self):
        with open(self.path, 'r', encoding='UTF-8') as fp:
            return json.load(fp)

    def get_by_skill(self, skill: str):
        candidates_all = self.get_all()
        candidates_by_skill = []
        for candidate in candidates_all:
            if skill.lower() in candidate['position'].lower():
                candidates_by_skill.append(candidate)
        return candidates_by_skill
