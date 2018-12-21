# -*- coding:utf-8 -*-

from app.models import User
import unittest


class UserModelCase(unittest.TestCase):

    def test_password_hash_not_none(self):
        user = User(password='cat')
        self.assertTrue(user.password_hash is not None)

    def test_password_readable(self):
        user = User(password='cat')
        with self.assertRaises(AttributeError):
            user.password

    def test_password_not_same(self):
        user = User(password='cat')
        user2 = User(password='dog')
        self.assertFalse(user.password_hash == user2.password_hash)

    def test_password_hash_not_same(self):
        user = User(password='cat')
        user2 = User(password='cat')
        self.assertTrue(user.password_hash != user2.password_hash)


if __name__ == '__main__':
    unittest.main()
