from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_posts_in_blog(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test Post', 'Test Content')

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, 'Test Post')
        self.assertEqual(b.posts[0].content, 'Test Content')

    def test_json_no (self):
        b = Blog('Test', 'Test Author')
        expected = {'title': 'Test','author': 'Test Author', 'posts':[]}

    def test_json (self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test Post', 'Test Content')

        expected = {'title': 'Test',
            'author': 'Test Author',
            'post': [
                {
                    'title': 'Test Post',
                    'content': 'Test Content'}]}

        self.assertDictEqual(expected, b. json())
