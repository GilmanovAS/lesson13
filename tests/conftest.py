import pytest
import main_app

@pytest.fixture()
def test_app():
    return main_app.app.test_client()
