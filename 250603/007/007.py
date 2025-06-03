class Student:
    def __init__(self, secret, location, time):
        self.s = secret
        self.l = location
        self.t = time

arr = input().split()
student1 = Student(arr[0], arr[1], arr[2])
print(f'secret code : {student1.s}\nmeeting point : {student1.l}\ntime : {student1.t}')