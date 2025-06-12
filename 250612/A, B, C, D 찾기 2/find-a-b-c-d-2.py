import sys

arr1 = list(map(int, input().split()))

def is_equals(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for e1, e2 in zip(arr1, arr2):
        if e1 != e2:
            return False
    
    return True    

def initialize(abcd):
    init_arr = []

    for i in range(4):
        init_arr.append(abcd[i])
        
        for j in range(i+1, 4):
            init_arr.append(abcd[i] + abcd[j])
            
            for k in range(j+1, 4):
                init_arr.append(abcd[i] + abcd[j] + abcd[k])
                
                for l in range(k+1, 4):
                    init_arr.append(abcd[i] + abcd[j] + abcd[k] + abcd[l])

    return init_arr

for i in range(1, 41):
    for j in range(i, 41):
        for k in range(j, 41):
            for l in range(k, 41):
                init_arr = initialize((i, j, k, l))
                
                if is_equals(arr1, init_arr):
                    print(i, j, k, l)
                    sys.exit()