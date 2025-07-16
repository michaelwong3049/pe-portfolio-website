# tests/test_app.py

import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>MLH Fellow</title>" in html
        assert "1"
        assert "<strong>About Me!</strong>" in html
        assert "<strong>backlight-simulator</strong>" in html
        # TODO Add more tests relating to the home page

    def test_timeline(self):
        post_response = self.client.get("/api/timeline_post")
        assert post_response.status_code == 200
        assert post_response.is_json
        post_json = post_response.get_json()

        print("GET: ", post_json)

        # if json is null, then we should throw False assertion
        if not post_json:
            assert False, "No post_json?"

        assert "timeline_posts" in post_json
        # assert len(json["timeline_posts"]) == 0

        get_response = self.client.get("/api/timeline_post")
        assert get_response.status_code == 200
        assert get_response.is_json
        get_json = get_response.get_json()

        print("GET: ", get_json)

        # if json is null, then we should throw False assertion
        if not get_json:
            assert False, "No get_json?"

        assert "timeline_posts" in get_json
        
        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<h2>Timeline Posts</h2>" in html
        assert "<h2>Timeline Posts</h2>" in html
        assert "<h2>Leave a Timeline Post</h2>" in html
        
