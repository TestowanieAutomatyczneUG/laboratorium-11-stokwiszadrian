from src.Friendships import Friendships


class FriendshipsDatabase:
    def __init__(self):
        self.database = Friendships()

    def addFriend(self, person: str, friend: str):
        self.database.addFriend(person, friend)

    def makeFriends(self, person1: str, person2: str):
        self.database.makeFriends(person1, person2)

    def getFriendsList(self, person: str):
        return self.database.getFriendsList(person)

    def areFriends(self, person1: str, person2: str):
        return self.database.areFriends(person1, person2)


c = FriendshipsDatabase()
c.addFriend(12, 13)
print(c.getFriendsList(12))