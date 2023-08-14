from unittest import TestCase
from unittest.mock import patch
import testings.blog.app as app
from testings.blog.blog import Blog


class AppTest(TestCase):
    
    def test_print_blog(self):
        b = Blog("Test blog","Edem")
        app.blogs = {"Test":b}
        with patch("builtins.print") as mock_print:
            app.print_blog()
            mock_print.assert_called_with("- Test blog by Edem")