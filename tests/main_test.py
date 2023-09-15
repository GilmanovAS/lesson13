class TestMain:
    def test_root_status(self, test_app):
        response = test_app.get('/', follow_redirects=True)
        assert response.status_code == 200, "Status code "

    def test_root_content(self, test_app):
        response = test_app.get('/', follow_redirects=True)
        assert "It's main page" in response.data.decode('UTF-8'), "Error on the main page"
