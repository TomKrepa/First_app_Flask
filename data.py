from flask import abort

class Post:

    POSTS = [
        {'id': 1, 'title': 'First Post', 'content': 'My first post'},
        {'id': 2, 'title': 'Second Post', 'content': 'My second post'},
        {'id': 3, 'title': 'Third Post', 'content': 'My third post'},
    ]

    @classmethod
    def all(cls):
        """ Fetch all posts """
        return cls.POSTS

    @classmethod
    def find(cls, id):
        """ Fetch a single post """
        try:
            return cls.POSTS[id - 1]
        except IndexError:
            abort(404)