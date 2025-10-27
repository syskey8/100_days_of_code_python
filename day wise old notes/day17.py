# creating classes
class Test:
    pass        # pass is a keyword that does nothing but it is used to avoid syntax error

class User:
    def __init__(self):         # this is consturctor of the class
        print("new user is being created...")

user_1 = User() # creating an object of class User
user_1.id = "001" # adding attributes to the object
user_1.username = "user1" # adding attributes to the object

class User2:
    def __init__(self, user_id2, username2):
        self.id = user_id2
        self.username = username2
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1 # this is the user who is being followed
        self.following += 1 # this is the user who is following


user_2 = User2("002", "angela")
print(user_2)

user_3 = User2("003", "jack") # this is more easy to create an user using constructor rather than creating an object and then adding attributs to it
print(user_3.id)

user_2.follow(user_3)
print(user_2.followers)
print(user_2.following)
print(user_3.followers)
print(user_3.following)




