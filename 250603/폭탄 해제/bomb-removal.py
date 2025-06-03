class Info:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

code, color, second = input().split()
info = Info(code, color, second)
print(f'code : {info.code}')
print(f'color : {info.color}')
print(f'second : {info.second}')