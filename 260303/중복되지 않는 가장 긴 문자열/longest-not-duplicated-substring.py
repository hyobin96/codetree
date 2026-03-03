string = input()
n = len(string)
counting_alphabet = [0] * (ord('a') + 26 + 1)
counting_alphabet[ord(string[0])] = 1
j = 0
max_length = 1
for i in range(n):
    while j + 1 < n and counting_alphabet[ord(string[j + 1])] != 1:
        counting_alphabet[ord(string[j + 1])] = 1
        j += 1
    
    counting_alphabet[ord(string[i])] = 0
    max_length = max(max_length, j - i + 1)
        
print(max_length)