from unittest import TestCase
from testings.blog.blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog("Test","Test Author")

        self.assertEqual("Test", b.title)
        self.assertEqual("Test Author", b.author)
        self.assertListEqual([],b.post)


    
    def test_repr(self):
        b = Blog("Test blog","Edem")
        b2= Blog("My day","Kofi")

        self.assertEqual(b.__repr__(), "Test blog by Edem (0 posts)")
        self.assertEqual(b2.__repr__(), "My day by Kofi (0 posts)")

    def test_repr_multiple(self):
        b = Blog("Test blog","Edem")
        b.post =["testing"]
        b2= Blog("My day","Kofi")
        b2.post = ["testing","going home"]

        self.assertEqual(b.__repr__(),"Test blog by Edem (1 post)")
        self.assertEqual(b2.__repr__(), "My day by Kofi (2 posts)")


