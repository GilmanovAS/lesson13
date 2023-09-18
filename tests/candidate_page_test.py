class TestCandidatesPage:
    def test_candidate_page_status(self, test_app):
        response = test_app.get('http://127.0.0.1:5000/candidates/', follow_redirects=True)
        assert response.status_code == 200, "Status code error"
        response = test_app.get('http://127.0.0.1:5000/candidates/dev', follow_redirects=True)
        assert response.status_code == 200, "Status code error"
        assert "dev" in response.data.decode('UTF-8').lower(), "Error on the candidate page"

