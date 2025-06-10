X, Y = map(int, input().split())

total = 0
for num in range(X, Y+1):
    count_arr1 = [0] * 10
    count_arr2 = [0] * 10
    for n in str(num):
        count_arr1[int(n)] = 1
        count_arr2[int(n)] += 1
    if sum(count_arr1) == 2:
        is_inter = True
        for count in count_arr2:
            if count != 0 and count != 1 and count != len(str(num)) - 1:
                is_inter = False
                break
        if is_inter:
            total += 1

print(total)