s1, s2 = input().split()
arr2 = list(s2)
arr2[0], arr2[1] = s1[0], s1[1]
print(''.join(arr2))