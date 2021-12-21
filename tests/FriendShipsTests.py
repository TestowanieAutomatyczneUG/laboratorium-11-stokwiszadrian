import unittest
from assertpy import assert_that
from src.Friendships import Friendships


class TestFriendships(unittest.TestCase):
    def setUp(self):
        self.temp = Friendships()

    def test_addFriend(self):
        self.temp.addFriend("Kowalski", "Zieliński")
        assert_that(self.temp.friendships["Kowalski"]).contains("Zieliński")

    def test_makeFriends_oneway(self):
        self.temp.makeFriends("Kowal", "Znyk")
        assert_that(self.temp.friendships["Kowal"]).contains("Znyk")

    def test_makeFriends_theotherway(self):
        self.temp.makeFriends("Kowal", "Znyk")
        assert_that(self.temp.friendships["Znyk"]).contains("Kowal")

    def test_getFriendsList(self):
        self.temp.friendships = {"Kowal": {"Kwiatkowska", "Król"}}
        assert_that(self.temp.getFriendsList("Kowal")).contains_only("Kwiatkowska", "Król")

    def test_areFriends_positive(self):
        self.temp.friendships = {"Kowal": {"Zieliński", "Kwiatkowski"}}
        assert_that(self.temp.areFriends("Kwiatkowski", "Kowal")).is_true()

    def test_areFriends_negative(self):
        self.temp.friendships = {"Kowal": {"Zieliński", "Kwiatkowski"}}
        assert_that(self.temp.areFriends("Kowal", "Kwiatkowski")).is_false()

    def tearDown(self):
        self.temp = None
