id, lv = input().split()

class User:
    def __init__(self, id, lv):
        self.id = id
        self.lv = lv

user1 = User('codetree', 10)
user2 = User(id, lv)

print(f'user {user1.id} lv {user1.lv}')
print(f'user {user2.id} lv {user2.lv}')