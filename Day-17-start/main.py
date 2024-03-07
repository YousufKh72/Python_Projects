class User:

    def __init__(self, user_id, username):
        print("New user being created...")
        self.id = user_id
        self.username = username
        self.follower = 0
        self.following = 0
        print(f"{self.username} has the id '{self.id}' with a current followers of: {self.follower}.\n")

    def follow(self, user):
        user.follower += 1
        self.following += 1


user_1 = User("001", "Angela")
user_2 = User("002", "Mike")

print(user_1.follow(user_2))

print(f"{user_1.username}'s follower: {user_1.follower}")
print(f"{user_1.username} following: {user_1.following}")
print(f"{user_2.username}'s follower: {user_2.follower}")
print(f"{user_2.username} follower: {user_2.following}")
