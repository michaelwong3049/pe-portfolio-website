import unittest
from peewee import *
from playhouse.shortcuts import model_to_dict
from app import TimelinePost

MODELS = [TimelinePost]

# Use an in-memory SQLite for tests.
test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        # Bind model classes to test db. Since we have a complete list of
        # all models, we do not need to recursively bind dependencies.
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        # Not strictly necessary since SQLite in-memory databases only live
        # for the duration of the connection, and in the next step we close
        # the connection... but a good practice all the same.
        test_db.drop_tables(MODELS)

        # Close connection to db.
        test_db.close()

    def test_timeline_post(self):
        # Create 2 timeline posts.
        first_post = TimelinePost.create(name='John Doe',
            email='john@example.com', content='Hello world, I\'m John!')
        assert first_post.id == 1

        second_post = TimelinePost.create(name='Jane Doe',
            email='jane@example.com', content='Hello world, I\'m Jane!')
        assert second_post.id == 2

    # TODO: Get timeline posts and assert that they ar
    def test_timeline_get(self):
        first_post = TimelinePost.create(name='John Doe',
            email='john@example.com', content='Hello world, I\'m John!')

        second_post = TimelinePost.create(name='Jane Doe',
            email='jane@example.com', content='Hello world, I\'m Jane!')

        posts = [model_to_dict(p) for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())]

        # the posts[1] correlates to the the id of 1 because it was created earlier, its at the bottom of the stack
        assert posts[1]["id"] == 1
        assert posts[0]["id"] == 2

