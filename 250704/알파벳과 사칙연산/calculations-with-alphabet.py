def select_nums(cnt):
    global alpha_arr, answer
    if cnt == 6:
        answer = max(answer, calculate())
        return

    for i in range(1, 5):
        alpha_arr[ord('a') + cnt] = i
        select_nums(cnt + 1)

def calculate():
    global expr, alpha_arr
    result = alpha_arr[ord(expr[0])]
    for i in range(len(expr)):
        oper = expr[i]
        if oper in ('+', '-', '*'):
            next = alpha_arr[ord(expr[i+1])]
            if oper == '+':
                result += next
            elif oper == '-':
                result -= next
            else:
                result *= next
    return result

expr = list(input())
alpha_arr = [0] * (ord('f') + 1)
nums = []
answer = -10000000000
select_nums(0)

print(answer)