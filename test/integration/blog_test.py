from unittest import TestCase
from testings.blog.blog import Blog

class BlogTest(TestCase):
    
    def test_create_post_blog(self):
        b = Blog("Test Post","Test Content")
        b.create_post("Test Post","Test Content")

        b.create_post(len(b.post),1)
        b.create_post(b.post[0].title,"Test Post")
        b.create_post(b.post[0].content, "Test Content")
        
    
    def test_json_nopost(self):
        b = Blog("Test blog","Edem")

        expected = {"title":"Test blog","author":"Edem","post":[]}
        self.assertDictEqual(expected,b.json())


    def test_json(self):
        b = Blog("Test blog","Edem")
        b.create_post("Test Post","Test Content")

        expected = {"title":"Test blog","author":"Edem","post":[{"title":"Test Post","content":"Test Content"}]}
        self.assertDictEqual(expected,b.json())