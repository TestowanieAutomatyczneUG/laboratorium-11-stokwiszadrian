class Friendships:
    def __init__(self):
        self.friendships = {}

    def addFriend(self, person: str, friend: str):
        self.addIfDoesntExist(person)
        self.addIfDoesntExist(friend)
        self.friendships[person].add(friend)

    def makeFriends(self, person1: str, person2: str):
        self.addIfDoesntExist(person1)
        self.addIfDoesntExist(person2)
        self.addFriend(person1, person2)
        self.addFriend(person2, person1)

    def getFriendsList(self, person: str):
        self.addIfDoesntExist(person)
        return self.friendships[person]

    def areFriends(self, person1: str, person2: str):
        self.addIfDoesntExist(person2)
        if person1 in self.friendships[person2]:
            return True
        else:
            return False

    def addIfDoesntExist(self, person: str):
        if person not in self.friendships:
            self.friendships[person] = set()