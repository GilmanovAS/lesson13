from app.candidates_bp.dao_candidates.candidates_dao import CandidatesDAO
import pytest
from main_app import app


@pytest.fixture()
def fix_candidates_dao():
    return CandidatesDAO(app.config.get('JSON_LOAD_PATH'))


key_should_be = {"pk", "name", "position"}


class TestCandidatesDAO:

    def test_get_all(self, fix_candidates_dao):
        candidates = fix_candidates_dao.get_all()
        assert type(candidates) == list, "Not list"
        assert len(candidates) > 0, "Empty list"
        assert key_should_be == set(candidates[0].keys()), "Incorrect list"

    def test_by_id(self, fix_candidates_dao):
        candidate = fix_candidates_dao.get_by_skill('Dev')
        assert candidate[0]["pk"] == 2, "Inccorect number"
        assert key_should_be == set(candidate[0].keys()), "Inccorect number"