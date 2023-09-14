import pytest


class TestMain:
    def test_root_status(self, test_app):
        response = test_app.get('/', follow_redirects=True)
        assert response.status_code == 200, "Status code "
