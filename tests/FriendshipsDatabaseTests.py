from src.FriendshipsDatabase import FriendshipsDatabase
from src.Friendships import Friendships
from unittest.mock import *
import unittest


class TestFriendshipDatabase(unittest.TestCase):
    def setUp(self):
        self.temp = FriendshipsDatabase()

    def test_addFriend(self):
        self.temp.database.addFriend = MagicMock()
        self.temp.addFriend("Kowal", "Bobek")
        self.temp.database.addFriend.assert_called_with("Kowal", "Bobek")

    def test_makeFriends(self):
        self.temp.database.makeFriends = MagicMock()
        self.temp.makeFriends("Szymański", "Góralski")
        self.temp.database.makeFriends.assert_called_once_with("Szymański", "Góralski")

    def test_getFriendsList(self):
        self.temp.database.getFriendsList = MagicMock(side_effect={"Ziólkowski", "Kucharski"})
        self.temp.getFriendsList("Szymański")
        self.temp.database.getFriendsList.assert_called_once_with("Szymański")

    def test_areFriends(self):
        self.temp.database.areFriends = MagicMock(side_effect=[True])
        self.temp.areFriends("Szymański", "Znyk")
        self.temp.database.areFriends.assert_called_once_with("Szymański", "Znyk")

    def tearDown(self):
        self.temp = None
