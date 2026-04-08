p = [31, 37]
m = [int(1e9) + 7, int(1e9) + 9]

input_s = input().rstrip()
target_s = input().rstrip()

target_length = len(target_s)

def to_int(c):
    return ord(c) - ord('a') + 1

p_pow = [[0] * (target_length + 1) for _ in range(2)]
for k in range(2):
    p_pow[k][0] = 1
    for i in range(1, target_length + ):
        p_pow[k][i] = (p_pow[k][i - 1] * p[k]) % m[k]
    
hash_targets = [0] * 2
for k in range(2):
    for i in range(target_length):
        hash_targets[k] = (hash_targets[k] + \
        to_int(target_s[i]) * p_pow[k][target_length - i - 1] + m[k]) % m[k]

hash_inputs = [0] * 2
for k in range(2):
    for i in range(target_length):
        hash_inputs[k] = (hash_inputs[k] + \
        to_int(input_s[i]) * p_pow[k][target_length - i - 1] + m[k]) % m[k]

if hash_targets[0] == hash_inputs[0] and hash_targets[1] == hash_inputs[1]:
    print(0)
else:
    idx = -1
    for i in range(1, len(input_s) - target_length + 1):
        for k in range(2):
            hash_inputs[k] = (hash_inputs[k] * p[k] - to_int(input_s[i - 1]) * p_pow[k][target_length] + \
                to_int(input_s[i + target_length - 1])) % m[k]
            if hash_inputs[k] < 0:
                hash_inputs[k] += m[k]

        if hash_inputs[0] == hash_targets[0] and hash_inputs[1] == hash_targets[1]:
            idx = i
            break      
    print(idx)