import unittest
from app.models import Post, User, Comment

class TestPost(unittest.TestCase):
    
    def setUp(self):
        self.user_joy = User(username="eleganece",password = "joy123",email = "developerjojoo@gmail.com")
        self.new_post = Post(title = "Fabric",content = "Types of fabrics used in fashion",user_id = self.user_joy.id)
        self.new_comment = Comment(comment = "Great piece",post_id = self.new_post.id,user_id = self.user_joy.id)

    def test_instance(self):
        self.assertTrue(isinstance(self.user_joy, User))
        self.assertTrue(isinstance(self.new_post, Post))
        self.assertTrue(isinstance(self.new_comment, Comment))