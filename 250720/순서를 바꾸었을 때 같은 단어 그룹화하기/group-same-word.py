n = int(input())
words = [input() for _ in range(n)]
for i in range(n):
    words[i] = ''.join(sorted(list(words[i])))

d = dict()
word_max = 0
for word in words:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

    if word_max < d[word]:
        word_max = d[word]

print(word_max)